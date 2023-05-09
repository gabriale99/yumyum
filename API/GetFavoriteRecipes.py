import boto3
import simplejson as json

def lambda_handler(event, context):
    user_id = event['queryStringParameters']['UserID']
    dynamodb = boto3.resource('dynamodb')
    user_table = dynamodb.Table('user')
    user_record = user_table.get_item(Key={'UserID': str(user_id)})['Item']
    fav_recipes = user_record['FavoriteRecipes']
    
    if not fav_recipes:
        status_code = 404
        body = {
            'message': 'The favorite recipe list is empty'
        }
    else:
        # Build the batch_params
        keys_to_get = [{'ID': r} for r in fav_recipes]
        batch_params = {
            'RequestItems': {
                'recipe': {
                    'Keys': keys_to_get
                }
            }
        }
    
        try:
            response = dynamodb.batch_get_item(**batch_params)
            status_code = 200
            body = response['Responses']['recipe']
            body = [{            'ID': b['ID'],
                'Name': b['Name'],
                'Region': b['Region'],
                'TypeOfMeal': b['TypeOfMeal'],
                'Thumbnail': b['Thumbnail'],
                'Serving': b['Serving'],
                'CookingTime': b['CookingTime'],
                'Credit': b['Credit']
            } for b in body]
        except Exception as e:
            status_code = 400
            message = "Unable to retreive the favorite recipes"
            body = {
                'error': e.response['Error']['Message'],
                'message': message
            }
    
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps(body)
    }
