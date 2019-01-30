
import requests
import jsons
import pandas as pd

def main():
    dollar = cambio_dollar()
    print("O valor do cambio do Dólar é%.2f" %dollar)

    euro = cambio_euro()
    print("O valor do cambio do Euro é%.2f" %euro)

    bitcoin = cambio_bitcoin()
    print("O valor do cambio do Bitcoin é%.2f" %bitcoin)

    exportar_cvs(dollar, euro, bitcoin)

def cambio_dollar(url= "http://data.fixer.io/api/latest?access_key=0b9ce29cb294d073455736036d8be676&format=1"):

    response = requests.get(url)
    if response.status_code == 200:
        print("\nConexão com sucesso!")
        d= response.json()

    taxa_brl = d['rates']['BRL']
    taxa_usd = d['rates']['USD']
    real_d = taxa_brl / taxa_usd
    real_d = round (real_d,2)
    return real_d

def cambio_euro(url= "http://data.fixer.io/api/latest?access_key=0b9ce29cb294d073455736036d8be676&format=1"):

    response = requests.get(url)
    if response.status_code == 200:
        print("\nConexão com sucesso!")
        dd = response.json()

    taxa_brl = dd['rates']['BRL']

    taxa_eur = dd['rates']['EUR']
    real_e = taxa_brl / taxa_eur
    real_e = round(real_e, 2)
    return real_e

def cambio_bitcoin(url = "http://data.fixer.io/api/latest?access_key=0b9ce29cb294d073455736036d8be676&format=1"):

    response = requests.get(url)
    if response.status_code == 200:
        print("\nConexão com sucesso!")
        ds = response.json()

    taxa_brl = ds['rates']['BRL']
    taxa_btc = ds['rates']['BTC']
    real_b = taxa_brl / taxa_btc
    real_b = round(real_b, 2)
    return real_b

def exportar_cvs(dollar, euro, bitcoin):

    linha = {'Dollar - USD': [dollar], 'Euro - EUR': [euro], 'Bitcoin - BTC': [bitcoin]}
    frame = pd.DataFrame (linha, columns= ['Dollar - USD', 'Euro - EUR'])
    frame.to_csv('moeda.csv')
    print("\nDados salvo na tabela!")

if __name__ == '__main__':
    main()
