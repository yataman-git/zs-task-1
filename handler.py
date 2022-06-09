import json
import boto3

def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    cf_client = boto3.client('cloudformation')
    cf_client.create_stack(
        StackName='zs-task1-ec2',
        TemplateBody='ec2.json'
    )

    return response
