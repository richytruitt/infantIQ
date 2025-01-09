import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    print("HERE THIS WORKED")
    
    return{
        "Name": "Richy",
        "test": "Testing"
    }