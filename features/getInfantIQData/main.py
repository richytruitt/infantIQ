
import json
from decimal import Decimal

import boto3


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)


def lambda_handler(event, context):
    session = boto3.session.Session()
   
    resource = session.resource('dynamodb')
    table = resource.Table('actions')

    response = table.scan()

    print(f"Response Object: {response}")
    print(f"=================")
    print(f"Length of response: {len(response)}")
    


    responseObject = {}
    responseBody = {}

    responseObject["statusCode"] = 200
    responseBody["data"] = {
        "Name": "Richy",
        "LastName": "Truitt"
    }

    responseObject["headers"] = {}
    responseObject["headers"]["Content-Type"] = "application/json"
    responseObject["body"] = json.dumps(responseBody, cls=DecimalEncoder)




    return responseObject

