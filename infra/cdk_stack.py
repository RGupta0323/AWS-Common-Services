# can rename this file later. 
import os 
from constructs import Construct
from . import config
from aws_cdk import (Stack, Duration, aws_lambda, aws_dynamodb, aws_kms,
                     aws_ec2 as ec2, aws_route53 as route53
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
        """domain_name = "thebrohan.net"
        domain_name_ns_servers = ["ns-1918.awsdns-47.co.uk", "ns-278.awsdns-34.com", "ns-1507.awsdns-60.org",
                                    "ns-686.awsdns-21.net"]
        public_hosted_zone = route53.PublicHostedZone(self, "PublicHostedZone",
                                 zone_name=domain_name
                                 )
        route53.NsRecord(self, "NSRecord",
                         zone=public_hosted_zone,
                         record_name="BrohanNSRecord",
                         values=domain_name_ns_servers,
                         ttl=Duration.minutes(30)
                         )"""

        ### API Gateway ###

        # domain name is going to hit this api gateway.
        # the api gateway then will have links to all the apps you would like others to see (not all the apps need to dhave this)
        # once this is done.
