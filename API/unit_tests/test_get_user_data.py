import simplejson as json

from ..PutUserPreference import lambda_handler as put_user_preference
from ..GetUserData import lambda_handler as get_user_data

class TestLambdaHandler():

    def test_get_new_user(self):

        event = {
            "queryStringParameters": {
                "UserID": "dummy",
                "testing": True
            },
        }

        expected_response = {
            'statusCode': 200,
                'headers': {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Headers" : "Content-Type",
                'Content-Type': 'application/json'
            },
            'body':  json.dumps({'isFirstTime': True})
        }

        # Getting new user data
        response = get_user_data(event, None)

        assert response == expected_response

    def test_get_existing_user(self):

        # Put a user into the user table
        put_event = {
            "body": "{\"UserID\": \"dummy\",\"Ingredients\": [\"Beef\"],\"Preferences\": [\"British\"],\"Vegetarian\": false, \"testing\": \"\"}"
        }
        response = put_user_preference(put_event, None)
        assert response['statusCode'] == 200


        expected_response = {
            'statusCode': 200,
                'headers': {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Headers" : "Content-Type",
                'Content-Type': 'application/json'
            },
            'body':  json.dumps({
                'isFirstTime': False,
                'Ingredients': ['Beef'],
                'Preferences': ['British'],
                'Vegetarian': False
            })
        }

        event = {
            "queryStringParameters": {
                "UserID": "dummy",
                "testing": True
            },
        }

        # Getting existing user data
        response = get_user_data(event, None)

        assert response == expected_response
