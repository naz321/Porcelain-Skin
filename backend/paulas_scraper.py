import requests
import json
from bs4 import BeautifulSoup

response = requests.get('https://www.paulaschoice.com/ingredient-dictionary')

soup = BeautifulSoup(response.text, 'html.parser')

data = {}

ingredients = soup.find_all(class_='ingredient-result')
#print(el)
for ingredient in ingredients: 
    my_ingredient = str(ingredient.find(class_='name').get_text()).replace('\n', '')
    if (ingredient.find(class_='description') is None):
        description = 'N/A to this ingredient'
    else: 
        description = ingredient.find(class_='description').get_text().replace('\n', '')
    data[my_ingredient] = []
    data[my_ingredient].append({
        'Rating': str(ingredient.find(class_='col-rating').get_text()),
        'Description': str(description)
    })

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)    

