import boto3
from collections import Counter
import heapq
import json

def sort_key(x):
    return x[1], -ord(x[0][0])

def lambda_handler(event, context):
    if event:
        client = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:  #  pragma: no cover
        client = boto3.resource('dynamodb')

    user_table = client.Table('user')
    
    filter_expression = 'size(Preferences) > :num'
    
    users = user_table.scan(
        FilterExpression=filter_expression,
        ExpressionAttributeValues={':num' : 0}
    )['Items']
    
    preferences = []
    for u in users:
        preferences.extend(u['Preferences'])

    unique_prefs = list(set(preferences))
    counter = { i: preferences.count(i) for i in unique_prefs }
    top_10 = heapq.nlargest(10, Counter(counter).items(), key=sort_key)
    top_10 = dict(top_10)
    
    return {
       'statusCode': 200,
       'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin" : "*", # Required for CORS support to work
            "Access-Control-Allow-Headers" : "Content-Type",
        },
       'body': json.dumps(top_10)
    }
