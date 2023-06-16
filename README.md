
# AWS Common Services Repo 
This repo creates multiple common services that will be used across my repos going forward. 
This prevents code from being duplicated across repositories and makes setting up new repositories simpler and easier since you most of the basic 
services have been already created for you. 


## Services Created 
## VPC 
> 
> A VPC has been created with 6 total subnets (3 public and 3 private). 
> The subnets are spread across 3 AZs and each subnet has their own route table attached. 
> Internet gateway has been created for the public subnet's route table. 

## Route53 Domain name 
> 
> Domain name: thebrohan.net (Fun fact people in high school used to call me this!) 
> This domain name has been created with the needed public hosted zone, NS records & A records. 
> It has been linked to API gateway. 

## ACM 
> 
> Created appropriate ACM cert to attach to API gateway. 

## API Gateway 
> 
> This has been created with one endpoint (thebrohan.net/) will return a 200 status code and a "success!" message. This is just the status lambda to get the health of api gateway. 

## Status Lambda 
> 
> Lambda function is been created to return a 200 status code to ensure that the api gateway is up and running. 



The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
