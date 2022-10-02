import requests
urls = [
    f'https://akabab.github.io/superhero-api/api/id/332.json',
    f'https://akabab.github.io/superhero-api/api/id/149.json',
    f'https://akabab.github.io/superhero-api/api/id/655.json',
]  # список адресов
def requests_get(url_all):
    # принимает список адресов
    r = (requests.get(url) for url in url_all)
    return r
def parser():
    # функция парсинга интелекта
    super_man = []
    for item in requests_get(urls):
        intelligence = item.json()
        print(intelligence)
        try:
            for power_stats in intelligence['results']:
                super_man.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print(f"Проверте ссылки urls: {urls}")
    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']
    print(f"Самый интелектуальный {name}, интелект: {intelligence_super_hero}")
parser()