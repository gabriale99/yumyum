import boto3
import simplejson as json
import pandas as pd

def lambda_handler(event, context):
    if event:
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
    
    favorite_recipes = []
    if users:
        for u in users:
            favorite_recipes.extend(u['FavoriteRecipes'])

        unique_recipes = list(set(favorite_recipes))
        len_recipes = len(unique_recipes)

        recipes = recipe_table.scan(
            FilterExpression=f"ID in ({','.join([':val' + str(i) for i in range(len_recipes)])})",
            ExpressionAttributeValues={f":val{i}": r for i, r in enumerate(unique_recipes)}
        )['Items']

        recipes = [
            {
                'ID': int(r['ID']),
                'CookingTime': r['CookingTime'],
                'Serving': r['Serving'],
                'Region': r['Region'],
                'TypeOfMeal': r['TypeOfMeal'],
            } for r in recipes
        ]

        recipes = pd.DataFrame(recipes)
        counter = [{ 'ID': int(i), 'Count': favorite_recipes.count(i) } for i in unique_recipes]
        counter = pd.DataFrame(counter)
        recipes = recipes.merge(counter, on=['ID'])
        recipes = recipes.nlargest(10, 'ID', 'first')
        body = {
            "data": recipes.to_dict(orient="records")
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
