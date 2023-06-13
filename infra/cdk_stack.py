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
                      nat_gateways=0, # make sure this stays at 0. These are spendy!
                      subnet_configuration=[
                            {'cidrMask': 24, 'name': 'public', 'subnetType': ec2.SubnetType.PUBLIC},
                            {'cidrMask': 24, 'name': 'private', 'subnetType': ec2.SubnetType.PRIVATE_ISOLATED}
                        ]
                    )


        ### Route53 Domain Name ###


        ### API Gateway (Used to host applications) ###