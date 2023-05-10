import boto3
import simplejson as json
from .table_structures import user_conf

from ..GetTop10CuisineByFavoriteRecipe import lambda_handler as get_top_10_from_favorite_recipe

class TestLambdaHandler():

    def test_get_top_10_from_favorite_recipe(self):
        event = {
            "queryStringParameters": {
                "testing": True
            }
        }

        expected_data = [
            {
                'CookingTime': '1 Hour 30 Minutes',
                'Count': 1,
                'ID': 1,
                'Region': 'Vietnamese',
                'Serving': '3 servings',
                'TypeOfMeal': 'Main Dish'
            },
            {
                'CookingTime': '30 Minutes',
                'Count': 2,
                'ID': 2,
                'Region': 'Thai',
                'Serving': '2 servings',
                'TypeOfMeal': 'Main Dish'
            },
            {
                'CookingTime': '20 Minutes',
                'Count': 3,
                'ID': 3,
                'Region': 'French',
                'Serving': '1 servings',
                'TypeOfMeal': 'Appetizer'
            },
            {
                'CookingTime': '30 Minutes',
                'Count': 4,
                'ID': 4,
                'Region': 'Italian',
                'Serving': '2 servings',
                'TypeOfMeal': 'Dessert'
            },
            {
                'CookingTime': '30 Minutes',
                'Count': 4,
                'ID': 5,
                'Region': 'Croatian',
                'Serving': '1 servings',
                'TypeOfMeal': 'Vegetarian'
            },
            {
                'CookingTime': '45 Minutes',
                'Count': 3,
                'ID': 6,
                'Region': 'Croatian',
                'Serving': '1 servings',
                'TypeOfMeal': 'Main Dish'
            },
            {
                'CookingTime': '45 Minutes',
                'Count': 2,
                'ID': 7,
                'Region': 'Italian',
                'Serving': '3 servings',
                'TypeOfMeal': 'Main Dish'
            },
            {
                'CookingTime': '45 Minutes',
                'Count': 1,
                'ID': 8,
                'Region': 'Italian',
                'Serving': '4 servings',
                'TypeOfMeal': 'Main Dish'
            },
        ]

        # Getting top 10 preferred cuisines
        response = get_top_10_from_favorite_recipe(event, None)

        assert response['statusCode'] == 200
        res_body = json.loads(response['body'])
        data = res_body['data']
        data.sort(key=lambda d: d['ID'])
        assert data == expected_data

    def test_get_nothing_favorite_recipe(self):
        client = boto3.client('dynamodb', endpoint_url="http://localhost:8000")
        client.delete_table(TableName="user")
        client.create_table(**user_conf)

        event = {
            "queryStringParameters": {
                "testing": True
            }
        }

        expected_body = {
            "message": "No results are returned"
        }

        # Getting top 10 preferred cuisines
        response = get_top_10_from_favorite_recipe(event, None)

        assert response['statusCode'] == 200
        res_body = json.loads(response['body'])
        assert res_body == expected_body