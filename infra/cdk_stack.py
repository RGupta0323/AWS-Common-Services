# can rename this file later. 
import os 
from constructs import Construct
from . import config
from aws_cdk import (Stack, aws_lambda, aws_dynamodb, aws_kms,
                     aws_ec2 as ec2,
                     )

class AwsCommonServicesStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None: 
        super().__init__(scope, id, **kwargs)

        ### VPC CODE HERE ###

        ### Create a VPC ###
        # vpc cidr range = 10.0.0.0/16
        vpc = ec2.Vpc(self, "AWS-Common-Services-VPC",
                      cidr="192.168.0.0/16",
                      vpc_name="AWS-Common-Services-VPC",
                      nat_gateways=0,
                      subnet_configuration=[
                            {'cidrMask': 24, 'name': 'ingress', 'subnetType': ec2.SubnetType.PUBLIC},
                            {'cidrMask': 24, 'name': 'application', 'subnetType': ec2.SubnetType.PRIVATE_ISOLATED}
                        ]
                    )

        ### Create a Public Subnet ###
        # subnet cidr range = 10.0.0.0/25
        """
        public_subnet_id = "aws-common-services-public-subnet"
        subnet_config = config.SUBNET_CONFIGURATION[public_subnet_id]
        public_subnet = ec2.CfnSubnet(
            self, public_subnet_id, vpc_id=vpc.vpc_id, cidr_block="192.168.0.127/25",
            availability_zone=subnet_config["availability_zone"], tags=[{'key': 'Name', 'value': "aws-common-services-public-subnet"}],
            map_public_ip_on_launch=subnet_config['map_public_ip_on_launch'],
        )
        """

        ### Create a Private Subnet ###
        # subnet cidr range = 10.0.0.128/25
        """
        private_subnet_id = "aws-common-services-private-subnet"
        subnet_config = config.SUBNET_CONFIGURATION[private_subnet_id]
        private_subnet = ec2.CfnSubnet(
            self, private_subnet_id, vpc_id=vpc.vpc_id, cidr_block="192.168.0.128/25",
            availability_zone=subnet_config["availability_zone"],
            tags=[{'key': 'Name', 'value': "aws-common-services-private-subnet"}],
            map_public_ip_on_launch=subnet_config['map_public_ip_on_launch'],
        )
        """
        ### Create an internet gateway and attach to the vpc
        '''
        igw = ec2.CfnInternetGateway(self, config.INTERNET_GATEWAY)
        ec2.CfnVPCGatewayAttachment(self, 'aws-common-services-igw', vpc_id=vpc.vpc_id,
                                    internet_gateway_id=igw.ref)
        '''


        ### Route Tables ###
        route_table_id_to_route_table_map = {}

        # public route table for public subnet
        '''
        public_rt_id = config.PUBLIC_ROUTE_TABLE
        public_rt = ec2.CfnRouteTable(self, id=public_rt_id, vpc_id=vpc.vpc_id,
                                      tags=[{"key":"Name", "value":"aws-common-services-public-route-table"}]
                                    )
        ec2.CfnSubnetRouteTableAssociation(self, "aws-common-services-public-rt-subnet-association",
                                           route_table_id=public_rt.ref,
                                           subnet_id=public_subnet_id
                                           )
        '''
        # Create routes for public route table

        # setting a route for internet gateway to hit the internet - this enables the public subnet to hit the
        # internet via the internet gateway
        '''
        ec2.CfnRoute(self, "public-rt-route", route_table_id=public_rt_id, destination_cidr_block="0.0.0.0/0",
                        gateway_id=igw.ref
                     )'''


        # Create a private route table for private subnet
        '''
        private_rt_id = "rtb-aws-common-services-private-route-table"
        private_rt = ec2.CfnRouteTable(self, id=private_rt_id, vpc_id=vpc.vpc_id,
                                        tags=[{"key":"Name", "value":private_rt_id}]
                                       )
        ec2.CfnSubnetRouteTableAssociation(self, "aws-common-services-private-rt-subnet-association",
                                            route_table_id=private_rt.ref,
                                           subnet_id=private_subnet_id
                                        )
        '''
        ### Route53 Domain Name ###


        ### API Gateway (Used to host applications) ###