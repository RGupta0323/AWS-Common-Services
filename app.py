#!/usr/bin/env python3
import os

import aws_cdk as cdk
from infra.cdk_stack import AwsCommonServicesStack

env = cdk.Environment(account="783978466054", region="us-east-1")
app = cdk.App()
AwsCommonServicesStack(app, "aws-common-services-stack", env=env)

app.synth()
