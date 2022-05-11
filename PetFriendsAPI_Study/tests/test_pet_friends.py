
'''----------Автотесты всяки разны и не очень-------'''
import os.path

from api import Pet_friends
from settings import email, password

'''-------Сами автотесты------'''
pf = Pet_friends()

'''-----Тест получения ключа пользователя-----'''
def test_get_api_for_user(email=email,password=password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

'''-----Тест получения списка жЫвотных пустого-----'''
def test_get_list_pets(filter = ''):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.get_list_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) >0

'''-----Тест получения списка моих жЫвотных-----'''
def test_get_Mylist_pets(filter = ''):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.get_list_mypets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) >0

'''-----Тест создания нового жЫвотного без фото-----'''
def test_add_pet_bez_foto(name = 'Кот',animal_type= 'Кот', age = 3.5):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.add_pet_without_foto(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

'''-----Тест создания нового жЫвотного-----'''
def test_add_pet(name = 'Шоггот',animal_type= 'божество', age = '3.5', pet_photo= 'images/Шоггот.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.add_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

'''-----Тест удаления жЫвотного-----'''
def test_delete_pet():
    _, auth_key = pf.get_api_key(email, password)
    _, my_pets = pf.get_list_mypets(auth_key, "")

    if len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][0]['id']
        status, _ = pf.delete_pet(auth_key, pet_id)

        _, my_pets = pf.get_list_mypets(auth_key, "")

        assert status == 200
        assert pet_id not in my_pets.values()

    else:
        raise Exception("There is no my pets")

    '''pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_mypets(auth_key, "")

    assert status == 200
    assert pet_id not in my_pets.values()'''

'''-----Тест обновления информации жЫвотного-----'''
def test_update_pet(name = 'Изменен',animal_type= 'Изменен', age = 3.6):
    _, auth_key = pf.get_api_key(email, password)
    _, my_pets = pf.get_list_mypets(auth_key, "")

    if len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][0]['id']
        status,result = pf.update_pet(auth_key, pet_id, name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")