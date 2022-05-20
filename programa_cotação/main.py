import requests
from bs4 import BeautifulSoup
from cotaçãoAPI import cotacaoAPI
#==============SCRAP==============#

# url
url = "https://www.iban.com/currency-codes"

# lista para armazenar o codigo dos paises
currency_codes = []

# request + soup

requisicao = requests.get(url)
html_doc = requisicao.text
soup = BeautifulSoup(html_doc, 'html.parser')
# filtrando tabela

tabela = soup.find('table')
rows = tabela.find_all('tr')[1:]

# loop em cada row

for row in rows:
    # crixandoo uma lista usando find_all
    items = row.find_all('td')
    # armazenando os valores
    nome_pais = items[0].text
    moeda_nome = items[1].text
    moeda_codigo = items[2].text
    # verificando se No universal currency
    if moeda_nome != 'No universal currency':
        # criando um dicionario e adicionando ela a lista
        currency_dic ={
            'pais' : nome_pais,
            'codigo' : moeda_codigo
        }
        currency_codes.append(currency_dic)

#==============MAIN==============#
# Criação de menu
def menu():
    try:
        opção = int(input('''
    [1] Listar paises disponiveis e seus codigos
    [2] Cotação atual
    [3] Conversor de moedas
    [4] Encerrar
     
                >>>'''))
    except:
        print('Escolha uma opção listada')
        menu()
    # função numero 01 do menu
 
    if opção == 1:
        for pos, currency_dic in enumerate(currency_codes):
            print(f"[{pos}] -- {currency_dic['pais']} -- {currency_dic['codigo']}")
        menu()
    # função numero 02 do menu
    elif opção == 2:
        print('Defina as duas moedas para verificar a cotação atual')
        moeda01 = str(input('>>>')).upper()
        print('-'*8)
        moeda02 = str(input('>>>')).upper()
        cotacaoAPI.cotacaoAtual(moeda01, moeda02)
        inverter = str(input('Deseja inverter as moedas ?[S/N]')).lower()
        if inverter == 's':
            moeda_aux = moeda01
            moeda01 = moeda02
            moeda02 = moeda_aux
            cotacaoAPI.cotacaoAtual(moeda01,moeda02)
            menu()
    # função numero 03 do menu
    elif opção == 3:
        print('Defina as duas moedas para verificar a cotação atual')
        moeda01 = str(input('>>>')).upper()
        print('-'*8)
        moeda02 = str(input('>>>')).upper()
        print('-'*8)
        try:
            valor = int(input('Qual o valor que deseja converter\n>>>'))
        except:
            print('Selecione um valor valido.')
        cotacaoAPI.conversão(moeda01, moeda02, valor)
        menu()
    # função numero 04 do menu
    elif opção == 4:
        return
menu()