
import os.path

from api import Pet_friends
from settings import email, password, neg_email, neg_password

'''-------Сами автотесты------'''
pf = Pet_friends()

'''-----Тест получения ключа пользователя c неверным паролем-----'''
def test_get_api_for_user(email=email,password=neg_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

'''-----Тест получения ключа пользователя с пустым E-mail-----'''
def test_get_api_for_user_neg_email(email=neg_email,password=password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

'''-----Тест создания нового жЫвотного без фото без имени и типа -----'''
def test_add_pet_bez_foto(name = '',animal_type= '', age = 3.5):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.add_pet_without_foto(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

'''-----Тест создания нового жЫвотного, нет фото в папке-----'''
def test_add_pet(name = 'Шоггот',animal_type= 'божество', age = '3.5', pet_photo= 'images/1Шоггот.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.add_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

'''-----Тест обновления информации жЫвотного не в списке-----'''
def test_update_pet(name = 'Изменен',animal_type= 'Изменен', age = 3.6):
    _, auth_key = pf.get_api_key(email, password)
    _, my_pets = pf.get_list_mypets(auth_key, "")

    if len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][99]['id']
        status,result = pf.update_pet(auth_key, pet_id, name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

'''-----Тест удаления жЫвотного не в списке-----'''
def test_delete_pet():
    _, auth_key = pf.get_api_key(email, password)
    _, my_pets = pf.get_list_mypets(auth_key, "")

    if len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][100]['id']
        status, _ = pf.delete_pet(auth_key, pet_id)

        _, my_pets = pf.get_list_mypets(auth_key, "")

        assert status == 200
        assert pet_id not in my_pets.values()

    else:
        raise Exception("There is no my pets")