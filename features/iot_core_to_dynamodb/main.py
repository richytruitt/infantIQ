import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('actions')
    response = table.put_item(
        Item={
            'timestamp': str(event["timestamp"]),
            'deviceID': str(event["deviceID"]),
            'action': str(event["action"])
        }
    )
    status_code = response['ResponseMetadata']['HTTPStatusCode']
    print(status_code)
    print("Execution FInished")