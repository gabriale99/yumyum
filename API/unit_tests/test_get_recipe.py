import boto3
from datetime import date
from decimal import Decimal
import simplejson as json

from .populate_db import prepoulate_recipe

from ..GetRecipe import lambda_handler as get_recipe
from ..PutUserPreference import lambda_handler as put_user_preference

class TestLambdaHandler():

    def test_get_recipe_based_on_preference_without_ingredients(self):
        put_user_event = {
            "body": "{\"UserID\": \"dummy\",\"Ingredients\": [],\"Preferences\": [\"Thai\"],\"Vegetarian\": false, \"testing\": \"\"}",
        }
        put_user_preference(put_user_event, None)

        event = {
            "queryStringParameters": {
                "UserID": "dummy",
                "testing": True
            }
        }

        expected_output = {
            "recipe": prepoulate_recipe[1],
            "favorited": False
        }

        # Getting new user data
        response = get_recipe(event, None)

        assert response['statusCode'] == 200
        res_body = json.loads(response['body'])
        assert res_body == expected_output

        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        user_table = dynamodb.Table('user')
        user = user_table.get_item(Key={'UserID': 'dummy'})['Item']
        recipe_id = str(prepoulate_recipe[1]['ID'])
        assert user['PreviousRecipes'][recipe_id] == Decimal(date.today().strftime('%Y%m%d'))

        # check if the same recipe is returned
        response = get_recipe(event, None)
        assert response['statusCode'] == 200
        res_body = json.loads(response['body'])
        assert res_body == expected_output

    def test_get_recipe_based_on_recipe_id(self):

        event = {
            "queryStringParameters": {
                "UserID": "dummy",
                "RecipeID": 1,
                "testing": True
            }
        }

        expected_output = {
            "recipe": prepoulate_recipe[0],
            "favorited": False
        }

        # Getting new user data
        response = get_recipe(event, None)

        assert response['statusCode'] == 200
        res_body = json.loads(response['body'])
        assert res_body == expected_output

    def test_get_recipe_based_on_vegetarian_status(self):
        put_user_event = {
            "body": "{\"UserID\": \"dummy1\",\"Ingredients\": [],\"Preferences\": [\"Croatian\"],\"Vegetarian\": true, \"testing\": \"\"}",
        }
        put_user_preference(put_user_event, None)

        event = {
            "queryStringParameters": {
                "UserID": "dummy1",
                "testing": True
            }
        }

        expected_output = {
            "recipe": prepoulate_recipe[4],
            "favorited": False
        }

        # Getting new user data
        response = get_recipe(event, None)

        assert response['statusCode'] == 200
        res_body = json.loads(response['body'])
        assert res_body == expected_output

    def test_get_recipe_based_on_preference_and_ingredient(self):
        put_user_event = {
            "body": "{\"UserID\": \"dummy2\",\"Ingredients\": [\"Beef\",\"Carrot\",\"Tomato\"],\"Preferences\": [\"Italian\"],\"Vegetarian\": false, \"testing\": \"\"}",
        }
        put_user_preference(put_user_event, None)

        event = {
            "queryStringParameters": {
                "UserID": "dummy2",
                "testing": True
            }
        }

        expected_output = {
            "recipe": prepoulate_recipe[7],
            "favorited": False
        }

        # Getting new user data
        response = get_recipe(event, None)

        assert response['statusCode'] == 200
        res_body = json.loads(response['body'])
        assert res_body == expected_output

    def test_get_recipe_based_on_preference_with_ingredients(self):
        put_user_event = {
            "body": "{\"UserID\": \"dummy3\",\"Ingredients\": [\"Beef\",\"Carrot\",\"Parsley\"],\"Preferences\": [\"Italian\"],\"Vegetarian\": false, \"testing\": \"\"}",
        }
        put_user_preference(put_user_event, None)

        event = {
            "queryStringParameters": {
                "UserID": "dummy3",
                "testing": True
            }
        }

        # Getting new user data
        response = get_recipe(event, None)

        assert response['statusCode'] == 200
        assert 'recipe' in response['body']

    def test_get_recipe_based_on_nothing(self):
        put_user_event = {
            "body": "{\"UserID\": \"dummy4\",\"Ingredients\": [\"Cheese\"],\"Preferences\": [\"Japanese\"],\"Vegetarian\": false, \"testing\": \"\"}",
        }
        put_user_preference(put_user_event, None)

        event = {
            "queryStringParameters": {
                "UserID": "dummy4",
                "testing": True
            }
        }

        # Getting new user data
        response = get_recipe(event, None)

        assert response['statusCode'] == 200
        assert 'recipe' in response['body']