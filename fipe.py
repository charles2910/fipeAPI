# SPDX-License-Identifier: GPL-3.0-or-later

import requests
import json

def main():
    funcao = input('Selecione o número:\n\t[1] Ver valor médio atual\n\t[2] Plotar gráfico\n> ')
    if funcao == '1':
        fetchValor()
    elif funcao == '2':
        plotPrice()
    else:
        print('Função inválida : (')

def fetchValor():
    car = {
            'maker': None,
            'model': None,
            'year': None
        }
    marcas = fetch('marcas', None)
    printValores(marcas)
    car['maker'] = input('Select the car maker by number: ')

    modelos = fetch('modelos', car)
    printValores(modelos)
    car['model'] = input('Select the car by number: ')

    anos = fetch('anos', car)
    printValores(anos)
    car['year'] = input('Select the model year by number: ').split('-')

    info = {
        "codigoTabelaReferencia": "262",
        "codigoMarca": car['maker'],
        "codigoModelo": car['model'],
        "codigoTipoVeiculo": "1",
        "anoModelo": car['year'][0],
        "codigoTipoCombustivel":car['year'][1],
        "tipoVeiculo": "carro",
        "modeloCodigoExterno": "",
        "tipoConsulta": "tradicional"
    }

    fipe = requests.post('https://veiculos.fipe.org.br/api/veiculos//ConsultarValorComTodosParametros', data=info)
    print(fipe.text)

def fetch(tipo, objeto):
    if tipo == 'marcas':
        marcas = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas', \
                headers={"user-agent": "curl/7.72.0"})
        maker = json.loads(marcas.text)
        return maker
    elif tipo == 'modelos':
        carros = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas/' \
                + objeto['maker'] + '/modelos', headers={"user-agent": "curl/7.72.0"})
        cars = json.loads(carros.text)
        cars = cars['modelos']
        return cars
    elif tipo == 'anos':
        anos = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas/' \
                + objeto['maker'] + '/modelos/' + objeto['model'] + '/anos', \
                headers={"user-agent": "curl/7.72.0"})
        years = json.loads(anos.text)
        return years

def printValores(tupla):
    for obj in tupla:
        try:
            print("[" + obj['codigo'] + "] " + obj['nome'])
        except TypeError:
            print("[" + str(obj['codigo']) + "] " + obj['nome'])

main()
