# SPDX-License-Identifier: GPL-3.0-or-later

import requests
import json

def main():
    funcao = input('Selecione o número:\n\t[1] Ver valor médio atual\n\t[2] Plotar gráfico: ')
    if funcao == '1':
        fetchValor()
    elif funcao == '2':
        plotPrice()
    else:
        print('Função inválida : (')

def fetchValor():
    marcas = fetch('marcas')
    printValores()
    selected_maker = input('Select the car maker by number: ')

def fetch(objeto):
    if objeto == 'marcas':
        marcas = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas', headers={"user-agent": "curl/7.72.0"})
        maker = json.loads(marcas.text)
        return maker
    elif objeto == 'modelos':


def printValores(tupla):
    for obj in tupla:
        try:
            print("[" + obj['codigo'] + "] " + obj['nome'])
        except TypeError:
            print("[" + str(obj['codigo']) + "] " + obj['nome'])

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

selected_year = input('Select the model year by number: ').split('-')

info = {
        "codigoTabelaReferencia": "262",
        "codigoMarca": str(selected_maker),
        "codigoModelo": str(selected_car),
        "codigoTipoVeiculo": "1",
        "anoModelo": str(selected_year[0]),
        "codigoTipoCombustivel": str(selected_year[1]),
        "tipoVeiculo": "carro",
        "modeloCodigoExterno": "",
        "tipoConsulta": "tradicional"
}

fipe = requests.post('https://veiculos.fipe.org.br/api/veiculos//ConsultarValorComTodosParametros', data=info)

print(fipe.text)
