import pandas as pd
import requests
from string import ascii_lowercase

api_url = 'https://www.themealdb.com/api/json/v1/1/search.php?f='

meals = pd.DataFrame()

for a in ascii_lowercase:
    api = api_url + a
    # print(api)
    response = requests.get(api)

    if response.status_code == 200:
        data = response.json()

        # Here, `data` is the extracted response from the API
        # print(data)
        data = data['meals']
        if not data:
            continue
        df = pd.DataFrame(data)
        meals = pd.concat([meals, df])

    else:
        print(f"Error: {response.status_code}")

meals.to_csv('meals.csv')
