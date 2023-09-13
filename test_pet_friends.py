from api import PetFriends
from settings import valid_email, valid_password
import os
pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_create_pet_simple(name='Ушастик', animal_type='Кот', age='5'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.post_api_create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_post_add_photo(pet_photo='images/kot.jpg'):
    """Проверяем что можно добавить фото питомца"""

     # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

      # Запрашиваем ключ api и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.post_add_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

        print('my_pets')

        assert status == 200
        assert result[pet_photo] == pet_photo


