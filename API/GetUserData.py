import boto3

import json

def lambda_handler(event, context):
    # Passing the UserID to the server side
    if 'testing' in event['queryStringParameters']:
        client = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:  # pragma: no cover
        client = boto3.resource('dynamodb')
    user_table = client.Table('user')

    # Search the user table with UserID
    user_id = event['queryStringParameters']['UserID']
    response = user_table.get_item(Key={'UserID': user_id})
    
    
    # If the UserID already exists, return false
    if 'Item' not in response:
        body = {
            "isFirstTime": True
        }
    else:
        user_record = response['Item']
        body = {
            "isFirstTime": False,
            "Ingredients": user_record['Ingredients'],
            "Preferences": user_record['Preferences'],
            "Vegetarian": user_record['Vegetarian'],
        }
    
    return {
       'statusCode': 200,
       'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin" : "*", # Required for CORS support to work
            "Access-Control-Allow-Headers" : "Content-Type",
        },
       'body': json.dumps(body)
    }