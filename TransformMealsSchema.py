from math import ceil, floor
import pandas as pd
import random


def transform_ingredients(ser):
    res = []
    for i in range(1, 21):
        res.append({
            'Name': ser['strIngredient{0}'.format(i)],
            'Portion': ser['strMeasure{0}'.format(i)]
        })
    return res

def random_serving(sd):
    random.seed(sd)
    serving = ceil(random.random() * 4) + 1
    return '{0} people'.format(serving)

def random_cooking_time(sd):
    random.seed(sd)
    rd = random.random()
    if rd * 100 < 50:
        cook_time = "{0} minutes".format(floor(rd * 5) * 10)
    else:
        cook_time = "{0} hours".format(round(rd * 3, 1) + 1)
    return cook_time

meals = pd.read_csv("meals.csv")

# print(meals.head(5))

meals = meals.rename(columns={
    'idMeal': 'ID',
    'strMeal': 'Name',
    'strArea': 'Region',
    'strCategory': 'TypeOfMeal',
    'strMealThumb': 'Thumbnail',
    'strInstructions': 'Instructions',
    'strSource': 'Credit',
    'strYoutube': 'VideoLink'
})

meals['Instructions'] = meals['Instructions'].apply(lambda x: x.split('\r\n'))

meals['Ingredients'] = meals.apply(transform_ingredients, axis=1)

meals = meals[['ID', 'Name', 'Region', 'TypeOfMeal', 'Thumbnail', 'Ingredients', 'Instructions', 'Credit', 'VideoLink']]

while len(meals) <= 100000:
    temp = meals.copy()
    meals = pd.concat([meals, temp])

meals['Serving'] = meals['ID'].apply(lambda x: random_serving(x))
meals['CookingTime'] = meals['ID'].apply(lambda x: random_cooking_time(x))
meals = meals.drop(columns=['ID']).reset_index(names=['ID'])

meals.to_csv("transformed_meals.csv")