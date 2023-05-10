import simplejson as json

from ..GetTop10CuisinePreference import lambda_handler as get_top_10_cuisine

class TestLambdaHandler():

    def test_get_resource(self):
        event = {
            "queryStringParameters": {
                "testing": True
            }
        }

        expected_output = {
            'French': 4,
            'Italian': 4,
            'Thai': 3,
            'Vietnamese': 3,
            'British': 2,
            'Chinese': 2,
            'Croatian': 2,
            'Dutch': 2,
            'Japanese': 2,
            'Indian': 1,
        }

        # Getting top 10 preferred cuisines
        response = get_top_10_cuisine(event, None)

        assert response['statusCode'] == 200
        res_body = json.loads(response['body'])
        assert res_body == expected_output
