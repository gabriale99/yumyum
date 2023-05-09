import boto3
import simplejson as json

from ..PutUserPreference import lambda_handler as put_user_preference
from ..PutFavoriteRecipe import lambda_handler as put_favorite_recipe

class TestLambdaHandler():
    event = {
        "body": "{\"UserID\": \"dummy\",\"ID\": 1, \"testing\": \"\"}",
    }

    def test_put_new_favorite_recipe(self):
        put_user_event = {
            "body": "{\"UserID\": \"dummy\",\"Ingredients\": [],\"Preferences\": [\"British\"],\"Vegetarian\": \"false\", \"testing\": \"\"}",
        }

        # Put new user
        response = put_user_preference(put_user_event, None)

        assert response['statusCode'] == 200

        expected_response = {
            'statusCode': 200,
                'headers': {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Headers" : "Content-Type",
                'Content-Type': 'application/json'
            },
            'body':  json.dumps({'message': "Recipe 1 is added to user dummy favorite recipe list"})
        }

        response = put_favorite_recipe(self.event, None)

        assert response == expected_response

        # Check the item is actually in the database
        db_client = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
        feedback_table = db_client.Table('user')
        res = feedback_table.get_item(Key={"UserID": "dummy"})
        assert 'Item' in res
        assert 1 in res['Item']['FavoriteRecipes']


    def test_put_existing_favorite_recipe(self):

        expected_response = {
            'statusCode': 400,
                'headers': {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Headers" : "Content-Type",
                'Content-Type': 'application/json'
            },
            'body':  json.dumps({'message': "The conditional request failed"})
        }

        response = put_favorite_recipe(self.event, None)

        assert response == expected_response
