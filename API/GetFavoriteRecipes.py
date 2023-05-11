import boto3
import simplejson as json

def lambda_handler(event, context):
    if 'testing' in event['queryStringParameters']:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:  #  pragma: no cover
        dynamodb = boto3.resource('dynamodb')

    user_id = event['queryStringParameters']['UserID']
    user_table = dynamodb.Table('user')
    try:
        user_record = user_table.get_item(Key={'UserID': user_id})
        user_record = user_record['Item']
        fav_recipes = user_record['FavoriteRecipes']
    
        if not fav_recipes:
            status_code = 404
            body = {
                'message': 'The favorite recipe list is empty',
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
    
            response = dynamodb.batch_get_item(**batch_params)
            status_code = 200
            body = response['Responses']['recipe']
            body = [
                {
                    'ID': b['ID'],
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
        body = {
            'error': e.__str__() if isinstance(e, KeyError) else e.response['Error']['Message'] ,
            'message': "Unable to retrieve the favorite recipes"
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
