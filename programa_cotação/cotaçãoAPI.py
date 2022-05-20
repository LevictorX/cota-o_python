import requests


class cotacaoAPI():
    # Request API cotação
    def cotacaoAtual(moeda01, moeda02):
        requisicao_api = requests.get(f'http://economia.awesomeapi.com.br/json/last/{moeda01}-{moeda02}')
        requisicao_api_dic = requisicao_api.json()
        cotação = requisicao_api_dic[f"{moeda01}{moeda02}"]['bid']
        return print(f'A cotação de {moeda01} e {moeda02} é: {cotação}')
    # Conversão de moeda
    def conversão(moeda01, moeda02, valor):
        requisicao_api = requests.get(f'http://economia.awesomeapi.com.br/json/last/{moeda01}-{moeda02}')
        requisicao_api_dic = requisicao_api.json()
        try:
            cotação = float(requisicao_api_dic[f"{moeda01}{moeda02}"]['bid'])
            converter = valor / cotação
            return print(f'O valor convertido de {valor} {moeda01} para {moeda02} é de {converter:.2f}')
        except:
            print(f'Moeda {cotação} não encontrada')