import requests #подгрузить библиотеку

token = '1111' #переменная для токена
host = 'https://api.pokemonbattle.me:9104' #переменная для хоста

'''response_generate = requests.post(f'{host}/pokemons', json= {
    "name": "Питонпокемон",
    "photo": "https://dolnikov.ru/pokemons/albums/034.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_generate.text)'''

'''response_change = requests.put(f'{host}/pokemons', json= {
    "pokemon_id": "5992",
    "name": "Пипидастр",
    "photo": "https://dolnikov.ru/pokemons/albums/034.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_change.text)'''

response_pokeball = requests.post(f'{host}/trainers/add_pokeball', json= {
    "pokemon_id": "5992"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_pokeball.text)



'''print(response.status_code)'''

'''if response.status_code == 200:
    print('ok!')
else:
    print('not ok!')'''