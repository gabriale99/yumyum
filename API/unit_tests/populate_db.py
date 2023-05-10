import boto3

def populate_data():
    dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

    region_table = dynamodb.Table('region')
    with region_table.batch_writer() as region_batch:

        for item in ['British', 'Chinese', 'Vietnamese']:
            region_batch.put_item(
                Item={'Name': item}
            )

    user_table = dynamodb.Table('user')
    with user_table.batch_writer() as user_batch:
        for item in prepoulate_user:

            user_batch.put_item(
                Item=item
            )

    recipe_table = dynamodb.Table('recipe')
    with recipe_table.batch_writer() as recipe_batch:
        for item in prepoulate_recipe:

            recipe_batch.put_item(
                Item=item
            )

prepoulate_user = [
    {
        "UserID": "predummy1",
        "FavoriteRecipes": [1, 2, 3, 4],
        "Ingredients": [
            'Beef', 'Carrot', 'Apple', 'Onion', 'Cheese', 
            'Peanuts', 'Yogurt', 'Turkey'
        ],
        "Preferences": [
            'British', 'Chinese', 'Vietnamese', 'Jamaican', 'Dutch', 'French',
            'Croatian', 'Italian', 'Thai', 'Japanese'
        ],
        "PreviousRecipes": {
            "1": 20230405,
            "2": 20230406,
            "3": 20230407,
            "4": 20230408
        },
        "Vegetarian": False,
    },
    {
        "UserID": "predummy2",
        "FavoriteRecipes": [2, 3, 4, 5],
        "Ingredients": [
            'Beef', 'Onion', 'Cheese', 'Peanuts', 'Yogurt', 'Turkey'
        ],
        "Preferences": [
            'Vietnamese', 'French', 'Italian', 'Thai'
        ],
        "PreviousRecipes": {
            "2": 20230405,
            "3": 20230406,
            "4": 20230407,
            "5": 20230408
        },
        "Vegetarian": False,
    },
    {
        "UserID": "predummy3",
        "FavoriteRecipes": [3, 4, 5, 6],
        "Ingredients": [
            'Beef', 'Carrot', 'Apple', 'Onion'
        ],
        "Preferences": [
            'Chinese', 'Vietnamese', 'Thai', 'Japanese'
        ],
        "PreviousRecipes": {
            "3": 20230405,
            "4": 20230406,
            "5": 20230407,
            "6": 20230408
        },
        "Vegetarian": False,
    },
    {
        "UserID": "predummy4",
        "FavoriteRecipes": [4, 5, 6, 7],
        "Ingredients": [
            'Onion', 'Cheese', 'Peanuts', 'Yogurt', 'Turkey'
        ],
        "Preferences": [
            'French', 'Croatian', 'Italian'
        ],
        "PreviousRecipes": {
            "4": 20230405,
            "5": 20230406,
            "6": 20230407,
            "7": 20230408
        },
        "Vegetarian": False,
    },
    {
        "UserID": "predummy5",
        "FavoriteRecipes": [5, 6, 7, 8],
        "Ingredients": [
            'Carrot', 'Apple', 'Onion', 'Cheese', 'Peanuts', 'Yogurt'
        ],
        "Preferences": [
            'British', 'Dutch', 'French', 'Italian'
        ],
        "PreviousRecipes": {
            "5": 20230405,
            "6": 20230406,
            "7": 20230407,
            "8": 20230408
        },
        "Vegetarian": True,
    },
    {
        "UserID": "predummy6",
        "FavoriteRecipes": [],
        "Ingredients": [
        ],
        "Preferences": [
            'Indian'
        ],
        "PreviousRecipes": {
            "9": 20230405,
        },
        "Vegetarian": False,
    },
]

prepoulate_recipe = [
    {
        "ID": 1,
        "Name": "Dish 1",
        "Region": "Vietnamese",
        "TypeOfMeal": "Main Dish",
        "Thumbnail": "Thumbnail1.jpg",
        "Serving": "3 servings",
        "CookingTime": "1 Hour 30 Minutes",
        "Ingredients": [
            {"Name": "Beef", "Portion": "2"},
            {"Name": "Onion", "Portion": "4"},
            {"Name": "Turkey", "Portion": "3 pounds" }
        ],
        "Instructions": ["Step1", "Step2", "Step3"],
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
        "Ingredients": [
            {"Name": "Beef", "Portion": "2"},
            {"Name": "Carrot", "Portion": "4"},
            {"Name": "Onion", "Portion": "" }
        ],
        "Instructions": ["Step1", "Step2", "Step3"],
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
        "Ingredients": [
            {"Name": "Beef", "Portion": "1"}
        ],
        "Instructions": ["Step1", "Step2", "Step3"],
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
        "Ingredients": [
            {"Name": "Apple", "Portion": "2"},
            {"Name": "Yogurt", "Portion": "4"}
        ],
        "Instructions": ["Step1", "Step2", "Step3"],
        "Credit": "Credit4.com"
    },
    {
        "ID": 5,
        "Name": "Dish 5",
        "Region": "Croatian",
        "TypeOfMeal": "Vegetarian",
        "Thumbnail": "Thumbnail5.jpg",
        "Serving": "1 servings",
        "CookingTime": "30 Minutes",
        "Ingredients": [
            {"Name": "Carrot", "Portion": "2"},
            {"Name": "Apple", "Portion": "4"}
        ],
        "Instructions": ["Step1", "Step2", "Step3"],
        "Credit": "Credit5.com"
    },
    {
        "ID": 6,
        "Name": "Dish 6",
        "Region": "Croatian",
        "TypeOfMeal": "Main Dish",
        "Thumbnail": "Thumbnail6.jpg",
        "Serving": "1 servings",
        "CookingTime": "45 Minutes",
        "Ingredients": [
            {"Name": "Carrot", "Portion": "2"},
            {"Name": "Apple", "Portion": "4"}
        ],
        "Instructions": ["Step1", "Step2", "Step3"],
        "Credit": "Credit6.com"
    },
    {
        "ID": 7,
        "Name": "Dish 7",
        "Region": "Italian",
        "TypeOfMeal": "Main Dish",
        "Thumbnail": "Thumbnail7.jpg",
        "Serving": "3 servings",
        "CookingTime": "45 Minutes",
        "Ingredients": [
            {"Name": "Beef", "Portion": "2"},
            {"Name": "Carrot", "Portion": "2"},
            {"Name": "Apple", "Portion": "4"}
        ],
        "Instructions": ["Step1", "Step2", "Step3"],
        "Credit": "Credit7.com"
    },
    {
        "ID": 8,
        "Name": "Dish 8",
        "Region": "Italian",
        "TypeOfMeal": "Main Dish",
        "Thumbnail": "Thumbnail8.jpg",
        "Serving": "4 servings",
        "CookingTime": "45 Minutes",
        "Ingredients": [
            {"Name": "Beef", "Portion": "2"},
            {"Name": "Carrot", "Portion": "2"},
            {"Name": "Tomato", "Portion": ""}
        ],
        "Instructions": ["Step1", "Step2", "Step3"],
        "Credit": "Credit8.com"
    },
]