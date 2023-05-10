import simplejson as json

from ..GetResource import lambda_handler as get_resource

class TestLambdaHandler():

    def test_get_resource(self):
        event = {
            "queryStringParameters": {
                "table": "region",
                "testing": True
            }
        }

        expected_output = ['British', 'Chinese', 'Vietnamese']

        # Getting new user data
        response = get_resource(event, None)

        assert response['statusCode'] == 200
        res_body = json.loads(response['body'])
        assert 'output' in res_body
        # The order of the output is ordered by the partition key in Hash
        # Therefore, requires manual sorting in test
        assert sorted(res_body['output']) == expected_output
