import boto3
from datetime import datetime
import simplejson as json

def lambda_handler(event, context):
    
    body = json.loads(event['body'])
    if 'testing' in body:
        client = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:  # pragma: no cover
        client = boto3.resource('dynamodb')
    feedback_table = client.Table('feedback')
    date_today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
    item_body = {
        'UserID': body['UserID'],
        'Category': body['Category'],
        'Feedback': body['Feedback'],
        'RecipeID': body['RecipeID'],
        'FeedbackDateTime': date_today
    }
    
    try:
        feedback_table.put_item(
            Item=item_body
        )
        
        status_code = 200
        body = {
            "message": f"User {body['UserID']}'s feedback is uploaded"
        }
    except Exception as e:
        status_code = 400
        body = {
            "message": "Feedback upload failed",
            "error": e.response['Error']['Message']
        }
    
    return {
       'statusCode': status_code,
       'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin" : "*", # Required for CORS support to work
            "Access-Control-Allow-Headers" : "Content-Type",
        },
       'body': json.dumps(body)
    }
