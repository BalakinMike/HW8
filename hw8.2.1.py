from itertools import count
import requests, json
import time
from progress.bar import IncrementalBar

dict = {}
hero_intellect = {}
bar = IncrementalBar('Исследовано', max = 732, suffix = '%(percent).1f%%')
for count in range (1,732):
    response = requests.get(f'https://akabab.github.io/superhero-api/api/id/{count}.json')
    bar.next()
    if response.status_code == 200:
        dict = response.json()
        if dict['name'] == 'Hulk' or dict['name'] == 'Captain America' or dict['name'] == 'Thanos':
            hero_intellect[dict['name']] = dict['powerstats']['intelligence'] # Делаем ещё один словарик с именем и интеллектом
bar.finish()

print('\n', hero_intellect)
print('Самый умный из героев Марвел: ', max(hero_intellect, key=hero_intellect.get)) # Выбор ключа по максимальному значению