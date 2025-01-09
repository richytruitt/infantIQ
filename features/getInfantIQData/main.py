
import json
from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)


def lambda_handler(event, context):
    print("#######################WARM START CODE STARTED #####################")
    
    responseObject = {}
    responseBody = {}

    responseObject["statusCode"] = 200
    responseBody["token"] = {
        "Name": "Richy",
        "LastName": "Truitt"
    }

    responseObject["headers"] = {}
    responseObject["headers"]["Content-Type"] = "application/json"
    responseObject["body"] = json.dumps(responseBody, cls=DecimalEncoder)




    return responseObject

