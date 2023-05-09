import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime
import random
import simplejson as json

def lambda_handler(event, context):
    date_today = int(datetime.today().strftime('%Y%m%d'))
    client = boto3.resource('dynamodb')
    user_table = client.Table('user')
    user_id = event['queryStringParameters']['UserID']
    user_record = user_table.get_item(Key={'UserID': str(user_id)})['Item']
    recipe_table = client.Table('recipe')
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
                if recipe:
                    break
                recipes = recipe_table.query(
                    IndexName='Region-index',
                    KeyConditionExpression=Key('Region').eq(p))
                recipes = recipes['Items']

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
                
            # If no recipe matches the ingredient 
            if not recipe:
                recipe_id = random.randrange(1, 50000, 1)
                recipe = recipe_table.get_item(Key={'ID': int(recipe_id)})
                recipe = recipe['Item']
        
            # leave history on previous recipe
            user_table.update_item(
                Key={"UserID": str(user_id)},
                UpdateExpression='set PreviousRecipes.#key=:val1',
                ExpressionAttributeValues={':val1': int(date_today)},
                ExpressionAttributeNames={'#key': str(recipe['ID'])}
            )
   
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps(recipe)
    }