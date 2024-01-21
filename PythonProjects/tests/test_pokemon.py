import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
header = {'Content-Type': 'application/json'}

def test_status_code():
    
 response = requests.get(url=f'{URL}/trainers')
 assert response.status_code == 200

def test_trainers_id():
    
 response = requests.get(url=f'{URL}/trainers',params={'trainer_id':4337})
 assert response.json()['trainer_name'] == 'валера'


