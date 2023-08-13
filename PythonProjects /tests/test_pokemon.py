import requests
import pytest

token = '1111' 
host = 'https://api.pokemonbattle.me:9104'

#проверяю статус код 200 
def test_status_code():
    response_trainers = requests.get(f'{host}/trainers', params= { 'trainer_id' : 1401 })
    assert response_trainers.status_code == 200 

#проверяю имя тренера
def test_name_trainer():
    response_trainers = requests.get(f'{host}/trainers', params= { 'trainer_id' : 1401 })
    assert response_trainers.json()['trainer_name'] == 'Devajsi'

#содержание полей в ответе по тренеру
@pytest.mark.parametrize('key,value', [('city', 'Copengagen'),
                                         ('trainer_name', 'Devajsi'),
                                         ('level', '1')])

def test_parts_of_answer(key, value):
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1401})
    assert response.json()[key] == value


