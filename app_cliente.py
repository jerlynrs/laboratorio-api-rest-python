import requests

url = 'http://127.0.0.1:5000/api/datos'

respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()
    for d in datos:
        print(d)
else:
    print("Error al conectar con el API")

