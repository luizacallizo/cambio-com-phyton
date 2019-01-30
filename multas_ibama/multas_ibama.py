import requests
import json
import pandas as pd

print("\nEstabelecendo conexão com o link...")
response = requests.get("http://dadosabertos.ibama.gov.br/dados/SICAFI/AC/Quantidade/multasDistribuidasBensTutelados.json")

if response.status_code == 200:
    print("\nConexão com sucesso!")

    #CRIA A LIST_OF_PROCESS PARA COLOCAR CADA LISTA EM UM "LUGAR" - ELE EQUIVALE O JSON COMPLETO EM FORMATO DE LISTA
    list_of_process = response.json()

    amount = len (list_of_process ['data'])
    print("Foram encontrados %d processos" %amount)

#variaveis
    list_municipio =[]
    list_nomeRazaoSocial = []
    list_valorAuto = []
    list_dataAtuo = []
    list_situcaoDebito = []


    categories = ["Fauna", "Flora", "Pesca", "Outras"]
    for category in categories:
        print("Acessando multas sobre %s..." %category)

        for process in list_of_process['data']:
            if process["tipoInfracao"] == category:
                list_municipio.append(process["municipio"])
                list_nomeRazaoSocial.append(process["nomeRazaoSocial"])
                list_valorAuto.append(process["valorAuto"])
                list_dataAtuo.append(process["dataAuto"])
                list_situcaoDebito.append(process["situcaoDebito"])

        row = {'municipio':list_municipio,'nomeRazaoSocial':list_nomeRazaoSocial,'valorAuto':list_valorAuto,'dataAuto': list_dataAtuo, 'situcaoDebito': list_situcaoDebito}

        df = pd.DataFrame (row, columns =['municipio', 'nomeRazaoSocial', 'valorAuto', 'dataAuto', "situcaoDebito"])
        df.to_csv('%s.csv'%category)
        print("Multas relacionadas a %s foram salvas na tabela!" %category)
        list_municipio.clear()
        list_nomeRazaoSocial.clear()
        list_valorAuto.clear()
        list_dataAtuo.clear()
        list_situcaoDebito.clear()

else:
    print("\nSite com algum problema!")