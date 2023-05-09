import boto3
import json

def lambda_handler(event, context):

    body = json.loads(event['body'])

    if 'testing' in event['body']:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:  # pragma: no cover
        dynamodb = boto3.resource('dynamodb')

    user_table = dynamodb.Table('user')

    update_expression = 'SET #attrName = list_append(#attrName, :attrValue)'
    condition_expression = 'not contains(#attrName, :val)'
    expression_attribute_names = {'#attrName': 'FavoriteRecipes'}
    expression_attribute_values = {':attrValue': [body['ID']], ':val': body['ID']}

    try:
        user_table.update_item(
            Key={"UserID": str(body['UserID'])},
            ConditionExpression=condition_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values,
            UpdateExpression=update_expression
        )
        
        message = f"Recipe {body['ID']} is added to user {body['UserID']} favorite recipe list"
        status_code = 200
    except Exception as e:
        message = e.response['Error']['Message']
        status_code = 400

    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps({'message': message})
    }