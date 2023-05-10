import boto3
import json

def lambda_handler(event, context):


  body = json.loads(event['body'])
  item_body = {
    'UserID': body['UserID'],
    'Ingredients': body['Ingredients'],
    'Preferences': body['Preferences'],
    'Vegetarian': body['Vegetarian'],
  }
    
  if 'testing' in event['body']:
    client = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
  else:  # pragma: no cover
    client = boto3.resource('dynamodb')
  user_table = client.Table('user')

  try:
    user_record = user_table.get_item(Key={'UserID': body['UserID']})
    if 'Item' not in user_record:
      item_body['PreviousRecipes'] = {}
      item_body['FavoriteRecipes'] = []
    
      user_table.put_item(Item=item_body)
      
      status_code = 200
      body = {'message': f'User {body["UserID"]} is added'}
    else:
        update_expression = 'SET #i = :i, #p = :p, #v = :v'
        expression_attribute_names = {
          '#i': 'Ingredients',
          '#p': 'Preferences',
          '#v': 'Vegetarian'
        }
        expression_attribute_values = {
          ':i': body['Ingredients'],
          ':p': body['Preferences'],
          ':v': body['Vegetarian']
        }
        
        # update the item
        user_table.update_item(
            Key={"UserID": body['UserID']},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )
        
        status_code = 200
        body = {'message': f"User {body['UserID']}'s preferences are updated"}
  except Exception as e:
    status_code = 400
    body = {
      'message': f"User {body['UserID']} is not added to the database",
      'error': e.response['Error']['Message']
    }
    
  return {
    'statusCode': status_code,
    'headers': {
      "Access-Control-Allow-Origin" : "*",
      "Access-Control-Allow-Headers" : "Content-Type",
      'Content-Type': 'application/json'
    },
    'body':  json.dumps(body)
  }
