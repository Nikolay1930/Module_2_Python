# var_1 = True
# var_2 = False
# print(type(var_1))
# var_3 = 3 > 1
# if var_3:
#     pass
# else:
#     print('условие ложное')
#
# if not var_3:
#     print('условие ложное')

# hour = 24
# if 12 <= hour <= 16:
#     print('День')
# elif 16 < hour <= 21:
#     print('Вечер')
# elif hour >= 6 and hour < 12:
#     print('Утро')
# else:
#     print('Ночь')


import requests
from pprint import pprint

url = 'https://swapi.dev/api/'
response = requests.get(url).json()
# print(response)


def check_people(url):
    for i in range(1, 6):
        response = requests.get(f'{url}/{i}').json()
        print(response)


def check_planets(url):
    diameters_list = []
    for i in range(1, 6):
        response = requests.get(f'{url}/{i}').json()
        diameters_list.append({response.get('name'): response.get('diameter')})
    print(diameters_list)

people_api =response.get('people')
planet_api = response.get('planets')
# print(planet_api)
# check_planets(planet_api)
starships_api = response.get('starships')
response = requests.get(starships_api).json()
pprint(response)
# check_planets(starships_api)
# check_people(starships_api)
# check_people(people_api)
