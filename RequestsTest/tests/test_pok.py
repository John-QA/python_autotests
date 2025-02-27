import requests
import pytest

base_url = 'https://api.pokemonbattle.ru/v2'##Основной URL.
token = 'trainer_token' ##Ввести свой токен.
base_header = {'Content-Type':'application/json', 'trainer_token':token} ##Базовые заголовки.
trainer_id = requests.get(url = f'{base_url}/me', headers = base_header).json()["data"][0]["id"] ##Получение id тренера, привязанного к токену
trainer_name = requests.get(url = f'{base_url}/me', headers = base_header).json()["data"][0]["trainer_name"] ##Получение имени тренера, привязанного к токену

def test_my_trainer_info_without_token_status_code ():
    res_my_trainer_info=requests.get(url = f'{base_url}/trainers', params= {'trainer_id':trainer_id}) ##запрос к общему списку с фильтром по id
    assert res_my_trainer_info.status_code == 200 ##Проверка, что запрос возвращает статус код 200

def test_my_trainer_info_without_token_trainer_name ():
    res_my_trainer_info=requests.get(url = f'{base_url}/trainers', params= {'trainer_id':trainer_id})##запрос к общему списку с фильтром по id
    assert res_my_trainer_info.json()["data"][0]["trainer_name"] == trainer_name ##Проверка, что запрос возвращает JSON-ответ, содержащий массив с ключом 
    ##"data", первый элемент которого содержит строку с ключом "name", значение которой совпадает с именем соответствующейго id тренера.