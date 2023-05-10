import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime
import logging
import random
import simplejson as json

def lambda_handler(event, context):
    if 'testing' in event['queryStringParameters']:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
        client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    else:  #  pragma: no cover
        dynamodb = boto3.resource('dynamodb')
        client = boto3.client('dynamodb')

    date_today = int(datetime.today().strftime('%Y%m%d'))
    user_table = dynamodb.Table('user')
    user_id = event['queryStringParameters']['UserID']
    user_record = user_table.get_item(Key={'UserID': str(user_id)})['Item']
    recipe_table = dynamodb.Table('recipe')
    recipe_sameday = None
    
    if 'RecipeID' in event['queryStringParameters']:
        recipe_id = event['queryStringParameters']['RecipeID']
        recipe = recipe_table.get_item(Key={'ID': int(recipe_id)})['Item']
    
    else:
        if 'PreviousRecipes' in user_record:
            
            prev_recipes = user_record['PreviousRecipes']
            # get today's date, and chech if there is a recipe with same date
            if prev_recipes:
                recipe_sameday = [key for key, val in prev_recipes.items() if val == date_today]
       
        # if there is a recipe on the same day, return it
        if recipe_sameday:
            recipe = recipe_table.get_item(Key={'ID': int(recipe_sameday[0])})
            recipe = recipe['Item']
          
        else:
            # filtering regarding region
            recipe = None
            recipes = []
            preference = user_record['Preferences']
            
            # Start with a different preference every time
            random.shuffle(preference)

            # try to select a recipe by preference to reduce the time
            for p in preference:
                if recipe:  #  pragma: no cover
                    break

                recipes = recipe_table.query(
                    IndexName='Region-index',
                    KeyConditionExpression=Key('Region').eq(p))
                recipes = recipes['Items']
                if not recipes:
                    continue

                if user_record['Vegetarian']:
                    recipes = list(filter(lambda r: r['TypeOfMeal'] == 'Vegetarian', recipes))

                # filtering regarding ingredient
                filtered_recipes = []
                ingredients = user_record['Ingredients']
                # if the user has insufficient ingredients, randomly pick a
                # recipe based on his preference
                if len(ingredients) < 3:
                    recipe = random.choice(recipes)
                else:
                    for r in recipes:
                        count = 0
                        for i in r['Ingredients']:
                            if i['Name'].title() in ingredients:
                                count += 1
                            if count >= 3:
                                filtered_recipes.append(r)
                                break
                    
              
                    # if no recipes is in the list after filter, randomly pick a
                    # recipe based on preference
                    if not filtered_recipes:
                        recipe = random.choice(recipes)
                    else:
                        recipe = random.choice(filtered_recipes)
                
            # If no recipe matches the ingredient and the cuisine preferences
            if not recipe:
                table_detail = client.describe_table(TableName='recipe')
                table_detail = table_detail['Table']
                recipe_id = random.randrange(1, table_detail['ItemCount'], 1)
                recipe = recipe_table.get_item(Key={'ID': int(recipe_id)})
                recipe = recipe['Item']

            # leave history on previous recipe
            user_table.update_item(
                Key={"UserID": str(user_id)},
                UpdateExpression='set PreviousRecipes.#key=:val1',
                ExpressionAttributeValues={':val1': int(date_today)},
                ExpressionAttributeNames={'#key': str(recipe['ID'])}
            )

    favorited = recipe['ID'] in user_record['FavoriteRecipes']
    
    body = {
        "recipe": recipe,
        "favorited": favorited
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps(body)
    }