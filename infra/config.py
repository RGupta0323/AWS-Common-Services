from aws_cdk import (aws_ec2 as ec2)

# basic VPC configs
VPC = 'AWS-Common-Services-VPC'.lower()

INTERNET_GATEWAY = 'aws-common-services-internet-gateway'

KEY_PAIR_NAME = 'aws-common-services-us-east-1-key'

REGION = 'us-east-1'

# route tables
PUBLIC_ROUTE_TABLE = 'aws-common-services-public-route-table'

ROUTE_TABLES_ID_TO_ROUTES_MAP = {
    PUBLIC_ROUTE_TABLE: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'gateway_id': INTERNET_GATEWAY,
            'router_type': ec2.RouterType.GATEWAY
        }
    ],
}

# security groups
SECURITY_GROUP = 'aws-common-services-wordpress-security-group'

SECURITY_GROUP_ID_TO_CONFIG = {
    SECURITY_GROUP: {
        'group_description': 'aws-common-services SG of the Wordpress servers',
        'group_name': SECURITY_GROUP,
        'security_group_ingress': [
            # Rule for HTTP (IPV4)
            ec2.CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ip='0.0.0.0/0', from_port=80, to_port=80
            ),
            # Rule for HTTP (IPv6)
            ec2.CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ipv6='::/0', from_port=80, to_port=80
            ),
            # Rule for HTTPS (IPV4)
            ec2.CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ip='0.0.0.0/0', from_port=443, to_port=443
            ),
            # RUle for HTTPS (IPV6)
            ec2.CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ipv6='::/0', from_port=443, to_port=443
            ),
            # Rule for SSH (IPV4)
            ec2.CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ip='0.0.0.0/0', from_port=22, to_port=22
            ),
            # RUle for SSH (ipv6)
            ec2.CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ipv6='::/0', from_port=22, to_port=22
            ),
        ],
        'tags': [{'key': 'Name', 'value': SECURITY_GROUP}]
    },
}

# subnets and instances
PUBLIC_SUBNET = 'aws-common-services-public-subnet'
PRIVATE_SUBNET = 'aws-common-services-private-subnet'

PUBLIC_INSTANCE = 'aws-common-services-public-instance'
PRIVATE_INSTANCE = 'aws-common-services-private-instance'

# AMI ID of the WordPress by Bitnami
AMI = 'ami-0c00935023a833df1'

SUBNET_CONFIGURATION = {
    PUBLIC_SUBNET: {
        'availability_zone': 'us-east-1a', 'cidr_block': '10.0.0.0/25', 'map_public_ip_on_launch': True,
        'route_table_id': PUBLIC_ROUTE_TABLE,
        'instances': {
            PUBLIC_INSTANCE: {
                'disable_api_termination': False,
                'key_name': KEY_PAIR_NAME,
                'image_id': AMI,
                'instance_type': 't2.micro',
                'security_group_ids': [SECURITY_GROUP],
                'tags': [
                    {'key': 'Name', 'value': PUBLIC_INSTANCE},
                ],
            },
        }
    },
    PRIVATE_SUBNET: {
        'availability_zone': 'us-east-1b', 'cidr_block': '10.0.0.128/25', 'map_public_ip_on_launch': False,
        'route_table_id': PUBLIC_ROUTE_TABLE,
        'instances': {
            PRIVATE_INSTANCE: {
                'disable_api_termination': False,
                'key_name': KEY_PAIR_NAME,
                'image_id': AMI,
                'instance_type': 't2.micro',
                'security_group_ids': [SECURITY_GROUP],
                'tags': [
                    {'key': 'Name', 'value': PRIVATE_INSTANCE},
                ],
            },
        }
    }
}