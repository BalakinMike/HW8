from typing import Union
from pathlib import Path

import requests


class YandexDisk:
    URL_UPLOAD_LINK: str = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    @property
    def header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, ya_disk_path: str) -> str:
        params = {"path": ya_disk_path, 'overwrite': 'true'}
        response = requests.get(self.URL_UPLOAD_LINK, headers=self.header, params=params)

        if response.status_code != 200:
            raise requests.exceptions.RequestException

        upload_url = response.json().get('href')
        return upload_url
    
    @staticmethod
    def __get_info_from_status_code(status_code: int) -> str:
        if status_code == 201:
            return 'Успешно загрузили'
        elif status_code == 412:
            return 'При дозагрузке файла был передан неверный диапазон в заголовке Content-Range'
        elif status_code == 413:
            return 'Размер файла больше допустимого.\n' \
                   'Если у вас есть подписка на Яндекс 360, можно загружать файлы размером до 50 ГБ,\n' \
                   'если подписки нет — до 1 ГБ.'
        elif status_code == 507:
            return 'Для загрузки файла не хватает места на Диске пользователя.'
        return 'Ошибка сервера.'

    def upload(self, path_to_file: Union[str, 'Path']) -> str:
        upload_link = self._get_upload_link(path_to_file.name)
        with open(path_to_file, 'rb') as file_obj:
            response = requests.put(upload_link, data=file_obj)
            return self.__get_info_from_status_code(response.status_code)



def main():
    base_dir = Path(__file__).resolve().parent
    files_name = "sort_text.txt"
    path_to_file = base_dir.joinpath(files_name)
    token = ''
    uploader = YandexDisk(token)
    result = uploader.upload(path_to_file=path_to_file)
    print(result)


if __name__ == '__main__':
    main()