import simplejson as json

from ..GetFavoriteRecipes import lambda_handler as get_favorite_recipes

class TestLambdaHandler():

    def test_get_existing_user_fav_recipe(self):
        event = {
            "queryStringParameters": {
                "UserID": "predummy1",
                "testing": True
            }
        }

        expected_output = [
            {
                "ID": 1,
                "Name": "Dish 1",
                "Region": "Vietnamese",
                "TypeOfMeal": "Main Dish",
                "Thumbnail": "Thumbnail1.jpg",
                "Serving": "3 servings",
                "CookingTime": "1 Hour 30 Minutes",
                "Credit": "Credit1.com"
            },
            {
                "ID": 2,
                "Name": "Dish 2",
                "Region": "Thai",
                "TypeOfMeal": "Main Dish",
                "Thumbnail": "Thumbnail2.jpg",
                "Serving": "2 servings",
                "CookingTime": "30 Minutes",
                "Credit": "Credit2.com"
            },
            {
                "ID": 3,
                "Name": "Dish 3",
                "Region": "French",
                "TypeOfMeal": "Appetizer",
                "Thumbnail": "Thumbnail3.jpg",
                "Serving": "1 servings",
                "CookingTime": "20 Minutes",
                "Credit": "Credit3.com"
            },
            {
                "ID": 4,
                "Name": "Dish 4",
                "Region": "Italian",
                "TypeOfMeal": "Dessert",
                "Thumbnail": "Thumbnail4.jpg",
                "Serving": "2 servings",
                "CookingTime": "30 Minutes",
                "Credit": "Credit4.com"
            }
        ]

        # Getting new user data
        response = get_favorite_recipes(event, None)

        assert response['statusCode'] == 200
        res_body = json.loads(response['body'])
        res_body.sort(key=lambda r: r['ID'])
        assert res_body == expected_output

    def test_get_existing_user_no_fav_recipe(self):
        event = {
            "queryStringParameters": {
                "UserID": "predummy6",
                "testing": True
            }
        }

        expected_output = {
            'message': 'The favorite recipe list is empty',
        }

        # Getting new user data
        response = get_favorite_recipes(event, None)

        assert response['statusCode'] == 404
        res_body = json.loads(response['body'])
        assert res_body == expected_output

    def test_get_invalid_user_fav_recipe(self):
        event = {
            "queryStringParameters": {
                "UserID": 1,
                "testing": True
            }
        }

        expected_output = {
                'message': 'Unable to retreive the favorite recipes',
                'error': 'One or more parameter values were invalid: Type mismatch for key'
            }

        # Getting new user data
        response = get_favorite_recipes(event, None)

        assert response['statusCode'] == 400
        res_body = json.loads(response['body'])
        assert res_body == expected_output
