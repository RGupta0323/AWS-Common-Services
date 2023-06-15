# can rename this file later.
from constructs import Construct
import boto3
from aws_cdk import (Stack, Duration, aws_lambda, aws_dynamodb, aws_kms,
                     aws_ec2 as ec2, aws_route53 as route53, aws_apigateway as apigw,
                     aws_certificatemanager as acm, aws_wafv2 as aws_wafv2, aws_waf as aws_waf,
                     aws_wafregional as wafregional, aws_route53_targets as targets
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
                      nat_gateways=0,  # make sure this stays at 0. These are spendy!
                      subnet_configuration=[
                          {'cidrMask': 24, 'name': 'public', 'subnetType': ec2.SubnetType.PUBLIC},
                          {'cidrMask': 24, 'name': 'private', 'subnetType': ec2.SubnetType.PRIVATE_ISOLATED}
                      ]
                      )

        ### Route53 Domain Name ###
        domain_name = "thebrohan.net"
        domain_name_ns_servers = ["ns-1918.awsdns-47.co.uk", "ns-278.awsdns-34.com", "ns-1507.awsdns-60.org",
                                  "ns-686.awsdns-21.net"]
        public_hosted_zone_id = "Z081614924Y6OKJ2LG5JH"
        public_hosted_zone = route53.HostedZone.from_hosted_zone_attributes(self, "PublicHostedZone",
                                                                            zone_name=domain_name,
                                                                            hosted_zone_id=public_hosted_zone_id
                                                                            )
        route53.NsRecord(self, "NSRecord",
                         zone=public_hosted_zone,
                         record_name="BrohanNSRecord",
                         values=domain_name_ns_servers,
                         ttl=Duration.minutes(30)
                         )

        acm_cert = acm.Certificate(self, f"{domain_name}_ACM_Certificate",
                                   domain_name=domain_name,
                                   certificate_name=f"{domain_name}_ACM_Certificate",
                                   validation=acm.CertificateValidation.from_dns(public_hosted_zone)
                                   )

        ### Generic Status Lambda to make sure api gateway is up and running ###
        status_lambda = aws_lambda.Function(self, id="AWS-Common-Services-Status-Lambda",
                                            code=aws_lambda.Code.from_asset("./software/src/lambda_functions/"),
                                            handler="status_lambda.lambda_handler",
                                            runtime=aws_lambda.Runtime.PYTHON_3_9)

        ### API Gateway ###
        api = apigw.LambdaRestApi(self, "APIGateway",
                                  domain_name=apigw.DomainNameOptions(
                                      certificate=acm_cert,
                                      domain_name=domain_name
                                  ),
                                  handler=status_lambda,
                                  default_cors_preflight_options=apigw.CorsOptions(
                                      allow_origins=apigw.Cors.ALL_ORIGINS,
                                      allow_methods=apigw.Cors.ALL_METHODS
                                  )
                                  )
        api_endpoint = api.root
        api_endpoint.add_method("GET", apigw.LambdaIntegration(status_lambda))

        # A record for route53
        route53.ARecord(self, "AliasRecord",
                        zone=public_hosted_zone,
                        target=route53.RecordTarget.from_alias(targets.ApiGateway(api))
                        )
