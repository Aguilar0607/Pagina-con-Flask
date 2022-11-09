import requests

url = 'https://rickandmortyapi.com/api/character'

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
# print(response.json())
respuesta_json = response.json()
print(respuesta_json['info'])
#print(respuesta_json['results'])
info = respuesta_json['info']
personajes = respuesta_json['results']
#for item respuesta_json['info']:
#    print(item['name'])

for personaje in personajes:
    print(f"The character {personaje['name']} is {personaje['status']}")

