from itertools import count
import pprint
import requests, json

dict = {}
hero_intellect = {}
response = requests.get(f'https://akabab.github.io/superhero-api/api/all.json')
#dict = response.json()
if response.status_code == 200:
        dict = response.json()
else:
    print('Ошибка: ',response.status_code)
for count in range (1,len(dict)):
    if dict[count]['name'] == 'Hulk' or dict[count]['name'] == 'Captain America' or dict[count]['name'] == 'Thanos':
        hero_intellect[dict[count]['name']] = dict[count]['powerstats']['intelligence'] # Делаем ещё один словарик с именем и интеллектом
    

print('\n', hero_intellect)
print('Самый умный из героев Марвел: ', max(hero_intellect, key=hero_intellect.get)) # Выбор ключа по максимальному значению