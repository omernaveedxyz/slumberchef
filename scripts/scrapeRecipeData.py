import requests
from enum import Enum
from bs4 import BeautifulSoup

class Ingredient(Enum):
    LARGE_LEEK = 1
    TASTY_MUSHROOM = 2
    FANCY_EGG = 3
    SOFT_POTATO = 4
    FANCY_APPLE = 5
    FIERY_HERB = 6
    BEAN_SAUSAGE = 7
    MOOMOO_MILK = 8
    HONEY = 9
    PURE_OIL = 10
    WARMING_GINGER = 11
    SNOOZY_TOMATO = 12
    SOOTHING_CACAO = 13
    SLOWPOKE_TAIL = 14
    GREENGRASS_SOYBEANS = 15
    GREENGRASS_CORN = 16

response = requests.get('https://bulbapedia.bulbagarden.net/wiki/Cooking_(Sleep)')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    count = 1

    def handleTable(table):
        global count
        rows = table.find('tbody').find_all('tr')[1:]
        for row in rows:
            ingredients = [[Ingredient[y[0].upper().replace(' ', '_')].value, int(y[1])] for y in [x.find_next_sibling(string=True).strip().split(' ×') for x in row.find_all('td')[2].find_all('a')]]
            previous = 1
            for ingredient in sorted(ingredients, key=lambda x: x[0]):
                while ingredient[0] > previous:
                    print("{{ dishId: {}, ingredientId: {}, quantity: {}}},".format(count, previous, 0))
                    previous += 1
                print("{{ dishId: {}, ingredientId: {}, quantity: {}}},".format(count, ingredient[0], ingredient[1]))
                previous += 1
            while previous <= 16:
                print("{{ dishId: {}, ingredientId: {}, quantity: {}}},".format(count, previous, 0))
                previous += 1
            count += 1

    # Curries
    table = soup.find('h3').find_next_sibling('table')
    handleTable(table)

    # Salads
    table = table.find_next_sibling('table')
    handleTable(table)

    # Desserts
    table = table.find_next_sibling('table')
    handleTable(table)
else:
    print("Failed to retrieve page:", response.status_code)