import requests
import jsons

def main():
    cambio_dollar()
    cambio_euro()
    cambio_bitcoin()

def cambio_dollar():
    response = requests.get("http://data.fixer.io/api/latest?access_key=0b9ce29cb294d073455736036d8be676&format=1")
    if response.status_code == 200:
        print("\nConexão com sucesso!")
        d= response.json()

    taxa_brl = d['rates']['BRL']
    taxa_usd = d['rates']['USD']
    real_d = taxa_brl / taxa_usd
    print("\nO dólar está custando %.2f reais" % real_d)

def cambio_euro():
    response = requests.get("http://data.fixer.io/api/latest?access_key=0b9ce29cb294d073455736036d8be676&format=1")
    if response.status_code == 200:
        print("\nConexão com sucesso!")
        dd = response.json()

    taxa_brl = dd['rates']['BRL']

    taxa_eur = dd['rates']['EUR']
    real_e = taxa_brl / taxa_eur
    print("\nO euro está custando %.2f reais" % real_e)

def cambio_bitcoin():
    response = requests.get("http://data.fixer.io/api/latest?access_key=0b9ce29cb294d073455736036d8be676&format=1")
    if response.status_code == 200:
        print("\nConexão com sucesso!")
        ds = response.json()

    taxa_brl = ds['rates']['BRL']
    taxa_btc = ds['rates']['BTC']
    real_b = taxa_brl / taxa_btc
    print("\nO bitcoin está custando %.2f reais" % real_b)

#PEDE PARA QUE O PROGRAMA EXECUTE A NOSSA FUNÇÃO OU MÉTODO MAIN
if __name__ == '__main__':
    main()
