import boto3
import simplejson as json

def lambda_handler(event, context):
    if event["queryStringParameters"]:
        client = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:  #  pragma: no cover
        client = boto3.resource('dynamodb')

    user_table = client.Table('user')
    recipe_table = client.Table('recipe')
    
    filter_expression = 'size(FavoriteRecipes) > :num'
    
    users = user_table.scan(
        FilterExpression=filter_expression,
        ExpressionAttributeValues={':num' : 0}
    )['Items']
    
    if users:
        favorite_recipes = []
        for u in users:
            favorite_recipes.extend(u['FavoriteRecipes'])

        unique_recipes = list(set(favorite_recipes))
        counter = { int(i): favorite_recipes.count(i) for i in unique_recipes }
        len_recipes = len(unique_recipes)
        
        recipes = []
        for r in unique_recipes:
            recipe = recipe_table.get_item(Key={'ID': r})
            recipes.append(recipe['Item'])


        recipes = [
            {
                'ID': int(r['ID']),
                'CookingTime': r['CookingTime'],
                'Serving': r['Serving'],
                'Region': r['Region'],
                'TypeOfMeal': r['TypeOfMeal'],
            } for r in recipes
        ]

        res = []
        for recipe in recipes:
            count = counter.get(recipe['ID'])
            recipe['Count'] = count
            res.append(recipe)


        body = {
            "data": res
        }
    else:
        body = {
            "message": "No results are returned"
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
