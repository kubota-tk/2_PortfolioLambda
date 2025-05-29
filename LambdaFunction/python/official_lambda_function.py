import json
import boto3

# DynamoDB クライアントの作成
dynamodb = boto3.client('dynamodb')
table_name = 'lambda-apigateway'


def lambda_handler(event, context):
    method = event["httpMethod"]
    
    if method == "GET":
        return get(event, context)
    elif method == "POST":
        return post(event, context)
    elif method == "PUT":
        return put(event, context)
    elif method == "DELETE":
        return delete(event, context)
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Unsupported method"})
        }
        
def get(event, context):
    id = event["queryStringParameters"]["id"]
    Item = {
        'TableName': table_name,
        'Key': {
            'id': {'S': id},
        }
    }
    response = dynamodb.get_item(**Item)
    
    if 'Item' in response:
        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Item not found"})
        }
