import requests, json
from pprint import pprint


urls = [
    f'https://akabab.github.io/superhero-api/api/id/332.json',
    f'https://akabab.github.io/superhero-api/api/id/149.json',
    f'https://akabab.github.io/superhero-api/api/id/655.json',
]  # список адресов

dict = {}
hero_intellect = {}
for url in urls:
    response = requests.get(url)
    dict = response.json()
    hero_intellect[dict['name']] = dict['powerstats']['intelligence']

print(hero_intellect)
print('Самый умный из нероев Марвел: ', max(hero_intellect, key=hero_intellect.get))