"""
test_pokemon_api
"""
import requests
URL = 'https://api.pokemonbattle.me:9104'
header = {
         'Content-Type': 'application/json',
         'trainer_token': '2cb9690d4ade6d4aec44d5a63a564e07'
        }


body =  {
          "name": "Feri",
          "photo": "https://dolnikov.ru/pokemons/albums/001.png"
                }

response = requests.post(url=f'{URL}/pokemons', json=body, headers=header)
print(f'статус код: {response.status_code}. сообщение: {response.text}')

body = {
       "pokemon_id": "28181",
       "name": "Geri",
       "photo": "https://dolnikov.ru/pokemons/albums/555.png"
              }

response = requests.put(url=f'{URL}/pokemons', json=body, headers=header)
print(f'статус код: {response.status_code}. сообщение: {response.text}')

body = {
          "pokemon_id": "28181"
              }

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=header)
print(f'статус код: {response.status_code}. сообщение: {response.text}')


