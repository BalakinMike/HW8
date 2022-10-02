import requests, json
from pprint import pprint


urls = [
    f'https://akabab.github.io/superhero-api/api/id/332.json',
    f'https://akabab.github.io/superhero-api/api/id/149.json',
    f'https://akabab.github.io/superhero-api/api/id/655.json',
]  # список адресов

dict = {}
hero_intellect = {}
response = requests.get('https://akabab.github.io/superhero-api/api/id/332.json')
dict = response.json()
pprint(dict)
hero_intellect[dict['powerstats']['intelligence']] = dict['name']



# requests_get('https://akabab.github.io/superhero-api/api/id/332.json')

            
pprint(hero_intellect)