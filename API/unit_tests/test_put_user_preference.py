import simplejson as json

from ..PutUserPreference import lambda_handler as put_user_preference

class TestLambdaHandler():
    good_event = {
        "body": "{\"UserID\": \"dummy\",\"Ingredients\": [],\"Preferences\": [\"British\"],\"Vegetarian\": false, \"testing\": \"\"}",
    }

    bad_event = {
        "body": "{\"UserID\": 1,\"Ingredients\": [],\"Preferences\": [\"British\"],\"Vegetarian\": false, \"testing\": \"\"}",
    }

    headers = {
        "Access-Control-Allow-Origin" : "*",
        "Access-Control-Allow-Headers" : "Content-Type",
        'Content-Type': 'application/json'
    }

    good_response = {
        'statusCode': 200,
        'headers': headers
    }

    bad_response = {
        'statusCode': 400,
        'headers': headers
    }


    def test_put_new_user(self):
        
        expected_response = self.good_response.copy()
        expected_response['body'] = json.dumps({'message': "User dummy is added"})

        # Put new user
        response = put_user_preference(self.good_event, None)

        assert response == expected_response

    def test_put_existing_user(self):
        
        expected_response = self.good_response.copy()
        expected_response['body'] = json.dumps({'message': "User dummy's preferences are updated"})

        # Put existing user
        response = put_user_preference(self.good_event, None)

        assert response == expected_response

    def test_put_bad_user(self):
        
        expected_response = self.bad_response.copy()
        expected_response['body'] = json.dumps({
            'message': 'User 1 is not added to the database',
            'error': 'One or more parameter values were invalid: Type mismatch for key'
        })

        # Put existing user
        response = put_user_preference(self.bad_event, None)

        assert response == expected_response
