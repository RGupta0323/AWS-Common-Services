def lambda_handler(event, context):
    headers = {
                "Access-Control-Allow-Origin" : "*", #  Required for CORS support to work
                "Access-Control-Allow-Credentials" : True # Required for HTTPS
            }
    return {"statusCode": 200, "body": "Success!", "headers":headers}