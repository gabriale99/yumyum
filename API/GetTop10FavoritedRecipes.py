keys_to_get = [{'ID': p} for p in unique_prefs]
    batch_params = {
        'RequestItems': {
            'recipe': {
                'Keys': keys_to_get
            }
        }
    }
    
    body = {
        "items": response['Items']
    }
    
    try:
        response = dynamodb.batch_get_item(**batch_params)
        status_code = 200
        body = response['Responses']['recipe']
        body = [{            'ID': b['ID'],
            'Name': b['Name'],
            'Region': b['Region'],
            'TypeOfMeal': b['TypeOfMeal'],
            'Thumbnail': b['Thumbnail'],
            'Serving': b['Serving'],
            'CookingTime': b['CookingTime'],
            'Credit': b['Credit']
        } for b in body]
    except Exception as e:
        status_code = 400
        message = "Unable to retreive the favorite recipes"
        body = {
            'error': e.response['Error']['Message'],
            'message': message
        }