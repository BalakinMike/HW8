import requests
import os

class YandexDisk:
    URL_UPLOAD_LINK: str = "https://cloud-api.yandex.net/v1/disk/resources/upload"


    def __init__(self, token: str):
        self.token = token

    @property
    def header(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def _get_upload_link(self, ya_disk_path: str):
        params = {"path": ya_disk_path, "overwrite": "true"}
        response = requests.get(self.URL_UPLOAD_LINK, headers=self.header, params=params)
        upload_url = response.json().get("href")

        return upload_url

    def uploader(self, ya_disk_path: str, file_path: str):
        upload_link = self._get_upload_link(ya_disk_path)
        with open(file_path, 'rb') as file_obj:
            response = requests.put(upload_link, data=file_obj)
            if response.status_code == 201:
                print("Успешно загрузили")
        return response.status_code

if __name__ == '__main__':
    BASE_DIR = os.getcwd()
    FILES_NAME = 'test1.py'
    file_path = os.path.join(BASE_DIR, FILES_NAME)
    TOKEN = 'y0_AgAAAAAMU5B4AADLWwAAAADQXDXFdBHPAWnrSai5pHFFKdIWfWAhyNQ'
    uploader = YandexDisk(TOKEN)
    uploader.uploader('test1.py', file_path)
