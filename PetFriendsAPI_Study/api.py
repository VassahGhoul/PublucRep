
'''-------Пишем всяки методы взаимодействия с REST API -------'''
import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class Pet_friends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email: str, password: str):
        '''Получаем ключ по API'''
        headers = {'email': email,
                   'password': password}
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_pets(self, auth_key: json, filter: str=""):
        '''-----Тест получения списка жЫвотных пустого-----'''
        headers = {'auth_key': auth_key ['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url+'api/pets', headers = headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_mypets(self, auth_key: json, filter: str="my_pets"):
        '''-----Тест получения списка моих жЫвотных-----'''
        headers = {'auth_key': auth_key ['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url+'api/pets', headers = headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_pet_without_foto(self, auth_key: json, name: str, animal_type: str, age: float):
        '''-----Тест создания жЫвотного без фото-----'''
        data ={'name' :name,
               'animal_type': animal_type,
               'age': age}
        headers = {'auth_key': auth_key ['key']}

        res = requests.post(self.base_url+'api/create_pet_simple', headers = headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str):
        '''-----Тест создания жЫвотного с фото-----'''
        data =MultipartEncoder(fields={
            'name' :name,
            'animal_type': animal_type,
            'age': age,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')})
        headers = {'auth_key': auth_key ['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url+'api/pets', headers = headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str):
        '''-----Тест удаления  жЫвотного -----'''

        headers = {'auth_key': auth_key ['key']}

        res = requests.delete(self.base_url+'api/pets/'+ pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_pet(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: float):
        '''-----Тест изменения информации  жЫвотного -----'''
        data = {'name': name,
                'animal_type': animal_type,
                'age': age}

        headers = {'auth_key': auth_key ['key']}

        res = requests.put(self.base_url+'api/pets/'+ pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result