# can rename this file later. 
import os 
from constructs import Construct
import config
from aws_cdk import (Stack, aws_lambda, aws_dynamodb, aws_kms,
                     aws_ec2 as ec2,
                     )

class CdkStack(Stack): 
    def __init__(self, scope: Construct, id: str, **kwargs) -> None: 
        super().__init__(scope, id, **kwargs)

        ### VPC CODE HERE ###

        ### Create a VPC ###
        # vpc cidr range = 10.0.0.0/16
        vpc = ec2.Vpc(self, "AWS-Common-Services-VPC", cidr="10.0.0.0/16",
                      vpc_name="AWS-Common-Services-VPC")

        ### Create a Public Subnet ###
        # subnet cidr range = 10.0.0.0/25
        subnet_config = config.SUBNET_CONFIGURATION["aws-common-services-public-subnet"]
        public_subnet = ec2.CfnSubnet(
            self, "aws-common-services-public-subnet", vpc_id=vpc.vpc_id, cidr_block=subnet_config['cidr_block'],
            availability_zone=subnet_config["availability_zone"], tags=[{'key': 'Name', 'value': "aws-common-services-public-subnet"}],
            map_public_ip_on_launch=subnet_config['map_public_ip_on_launch'],
        )


        ### Create a Private Subnet ###
        # subnet cidr range = 10.0.0.128/25

        ### Create an internet gateway adn attach to the vpc


        ### Create a public route table for public subnet

        ### Create a private route table for private subnet
