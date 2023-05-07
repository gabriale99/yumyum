#!/usr/bin/env python
# coding: utf-8

# In[28]:


from math import ceil, floor, isnan
import pandas as pd
import random
import boto3


def transform_ingredients(ser):
    res = []
    for i in range(1, 21):
        col = 'strIngredient{0}'.format(i)
        portion = 'strMeasure{0}'.format(i)
        if isinstance(ser[col], str) and ser[col] != '':
            res.append({
                'Name': ser[col],
                'Portion': ser[portion] if isinstance(ser[portion], str) else 'By user preference'
            })
        else:
            continue
            
    return res

def random_serving(sd):
    random.seed(sd)
    serving = ceil(random.random() * 4) + 1    
    return '{0} servings'.format(serving)

def random_cooking_time(sd):
    random.seed(sd)
    rd = random.uniform(0.2, 1)
    if rd * 100 < 50:
        cook_time = "{0} Minutes".format(random.choice([20, 30, 40, 45]))
    else:
        hours = floor(round(rd * 2, 1))
        minute = random.choice([0, 15, 20, 30, 40, 45])
        if hours == 1:
            if int(minute) == 0:
                cook_time = str(hours) + " Hour"
            else:
                cook_time = str(hours) + " Hour " + str(minute) + " Minutes"
        else:
            if int(minute) == 0:
                cook_time = str(hours) + " Hours"
            else:
                cook_time = str(hours) + " Hours " + str(minute) + " Minutes"
            
    return cook_time

meals = pd.read_csv("meals.csv", encoding='latin1')

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

remove = ['STEP 1', 'STEP 2', 'STEP 3', 'STEP 4', 'STEP 5', 'STEP 6', 'STEP 7', 'STEP 8', 'STEP 9',
         'Step 1', 'Step 2', 'Step 3', 'Step 4', 'Step 5', 'Step 6', 'Step 7', 'Step 8', 'Step 9',
         '0. ', '1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ',
         '01.', '02.', '03.', '04.', '05.', '06.', '07.', '08.', '09.',
         '1) ', '2) ', '3) ', '4) ', '5) ', '6) ', '7) ', '8) ', '9) ']

for i in remove:
    meals['Instructions'] = meals['Instructions'].apply(lambda x: x.replace(i, '\n'))
meals['Instructions'] = meals['Instructions'].apply(lambda x: list(filter(None, x.splitlines())))

meals['Ingredients'] = meals.apply(transform_ingredients, axis=1)
meals['Ingredients'] = meals['Ingredients'].apply(lambda x: list(filter(lambda y: isinstance(y['Name'], str) 
                                                                        or not isnan(y['Name']), x)))


meals = meals[['ID', 'Name', 'Region', 'TypeOfMeal', 'Thumbnail', 'Ingredients', 'Instructions', 'Credit', 'VideoLink']]

meals = meals.fillna('')

while len(meals) <= 50000:
    temp = meals.copy()
    meals = pd.concat([meals, temp])

meals['Serving'] = meals['ID'].apply(lambda x: random_serving(x))
meals['CookingTime'] = meals['ID'].apply(lambda x: random_cooking_time(x))

meals = meals[['Name', 'Region', 'TypeOfMeal', 'Thumbnail', 'Serving', 'CookingTime', 
               'Ingredients', 'Instructions', 'Credit', 'VideoLink']]

meals = meals.reset_index(drop=True).reset_index()
meals = meals.rename(columns={'index': 'ID'})
meals['ID'] = meals['ID'] + 1

# meals.to_csv("transformed_meals.csv", index=False)

dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
table_name = 'recipe'
table = dynamodb.Table(table_name)

for idx, row in meals.iterrows():
    data = row.to_dict()
    try:
        print(idx)    
        response = table.put_item(Item=data)
    
    except Exception as e:
        print(e)
        break


# In[ ]:




