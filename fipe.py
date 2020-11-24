# SPDX-License-Identifier: GPL-3.0-or-later

import requests
import json

print('oi')

marcas = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas', headers={"user-agent": "curl/7.72.0"})

maker = json.loads(marcas.text)


for obj in maker:
    print("[" + obj['codigo'] + "] " + obj['nome'])

selected_maker = input('Select the car maker by number: ')

carros = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas/'+selected_maker+'/modelos', headers={"user-agent": "curl/7.72.0"})

cars = json.loads(carros.text)
cars = cars['modelos']


for obj in cars:
    try:
        print("[" + obj['codigo'] + "] " + obj['nome'])
    except TypeError:
        print("[" + str(obj['codigo']) + "] " + obj['nome'])

selected_car = input('Select the car by number: ')

anos = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas/'+selected_maker+'/modelos/'+selected_car+'/anos', headers={"user-agent": "curl/7.72.0"})

years = json.loads(anos.text)

for obj in years:
    print("[" + obj['codigo'] + "] " + obj['nome'])

selected_year = input('Select the model year by number: ')

