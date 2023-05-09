import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime, date
import simplejson as json

# Import the Lambda function to be tested
from ..PutFeedback import lambda_handler as put_feedback

class TestLambdaHandler():
    headers = {
        "Access-Control-Allow-Origin" : "*",
        "Access-Control-Allow-Headers" : "Content-Type",
        'Content-Type': 'application/json'
    }

    body = {
        'UserID': 'dummy',
        'Category': 'Recipe',
        'Feedback': 'The app sucks',
        'RecipeID': 1
    }

    def test_put_feedback(self):

        event_body = self.body.copy()
        event_body['testing'] = True
        event = {
            "body": json.dumps(event_body),
        }

        expected_response = {
            'statusCode': 200,
            'headers': self.headers,
            'body':  json.dumps({'message': "User dummy's feedback is uploaded"})
        }

        # Put feedback
        response = put_feedback(event, None)

        assert response == expected_response

        # Check the item is actually in the database
        db_client = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
        feedback_table = db_client.Table('feedback')
        res = feedback_table.query(KeyConditionExpression=Key('UserID').eq('dummy'))
        assert 'Items' in res
        res_item = res['Items'].pop()
        res_date_time = res_item['FeedbackDateTime']
        del res_item['FeedbackDateTime']
        # Check attributes without the time
        assert res_item == self.body
        # Check the date
        res_date_time = datetime.strptime(res_date_time, '%Y-%m-%d %H:%M:%S').date()
        assert date.today() == res_date_time

    def test_put_invalid_feedback(self):
        bad_body = self.body.copy()
        bad_body['UserID'] = 1

        event_body = bad_body.copy()
        event_body['testing'] = True
        event = {
            "body": json.dumps(event_body),
        }

        expected_response = {
            'statusCode': 400,
            'headers': self.headers,
            'body':  json.dumps({
                'message': 'Feedback upload failed',
                'error': 'One or more parameter values were invalid: Type mismatch for key'
            })
        }

        # Put feedback
        response = put_feedback(event, None)

        assert response == expected_response
