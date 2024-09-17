import requests
import os
from datetime import datetime

# Cores ANSI para terminal
VERDE = '\033[92m'
AMARELO = '\033[93m'
RESET = '\033[0m'

def salvar_resultado(nome_arquivo, conteudo):
    """Salva o conteúdo em um arquivo na pasta results com codificação UTF-8"""
    pasta = 'results'
    # Verifica se a pasta 'results' existe e a cria se não existir
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
    print(f"Resultados salvos em: {caminho_arquivo}")

def obter_cotacao_moedas():
    print("\nCotação de Moedas:")
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL'
    response = requests.get(url)

    conteudo = ""
    if response.status_code == 200:
        data = response.json()
        conteudo += "Dólar (USD) para Real (BRL):\n"
        conteudo += f"Compra: {data['USDBRL']['bid']}\n"
        conteudo += f"Venda: {data['USDBRL']['ask']}\n\n"
        
        conteudo += "Euro (EUR) para Real (BRL):\n"
        conteudo += f"Compra: {data['EURBRL']['bid']}\n"
        conteudo += f"Venda: {data['EURBRL']['ask']}\n"
        
        print("\nDólar (USD) para Real (BRL):")
        print(f"\n{VERDE}Compra:{RESET} {data['USDBRL']['bid']}")
        print(f"{AMARELO}Venda:{RESET} {data['USDBRL']['ask']}")
        
        print("\nEuro (EUR) para Real (BRL):")
        print(f"\n{VERDE}Compra:{RESET} {data['EURBRL']['bid']}")
        print(f"{AMARELO}Venda:{RESET} {data['EURBRL']['ask']}")
    else:
        conteudo += f"Erro ao fazer a requisição: {response.status_code}\n"
        print("Erro ao fazer a requisição:", response.status_code)
    
    return conteudo

def obter_cotacao_criptomoedas():
    print("\nCotação de Criptomoedas:")
    
    # URLs da API para obter a cotação das criptomoedas
    urls = {
        'BTC': 'https://economia.awesomeapi.com.br/json/last/BTC-BRL',
        'LTC': 'https://economia.awesomeapi.com.br/json/last/LTC-BRL'
    }
    
    conteudo = ""
    
    for moeda, url in urls.items():
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            cotacao = data[f'{moeda}BRL']
            conteudo += f"\n{moeda} para Real (BRL):\n"
            conteudo += f"Compra: {cotacao['bid']}\n"
            conteudo += f"Venda: {cotacao['ask']}\n"
            if 'last' in cotacao:
                conteudo += f"Último preço negociado: {cotacao['last']}\n"
            else:
                conteudo += f"Último preço negociado não disponível para {moeda}.\n"
            
            print(f"\n{moeda} para Real (BRL):")
            print(f"\n{VERDE}Compra:{RESET} {cotacao['bid']}")
            print(f"{AMARELO}Venda:{RESET} {cotacao['ask']}")
            if 'last' in cotacao:
                print(f"\nÚltimo preço negociado: {cotacao['last']}")
            else:
                print(f"\nÚltimo preço negociado não disponível para {moeda}.")
        else:
            conteudo += f"Erro ao fazer a requisição para {moeda}: {response.status_code}\n"
    
    return conteudo

def main():
    while True:
        print("\nMenu:")
        print("1 - Cotação de Moedas")
        print("2 - Cotação de Criptomoedas")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            resultado = obter_cotacao_moedas()
            data_atual = datetime.now().strftime("%d-%m-%Y")
            nome_arquivo = f"cotacao_moedas_{data_atual}.txt"
            salvar_resultado(nome_arquivo, resultado)
        elif escolha == '2':
            resultado = obter_cotacao_criptomoedas()
            data_atual = datetime.now().strftime("%d-%m-%Y")
            nome_arquivo = f"cotacao_criptomoedas_{data_atual}.txt"
            salvar_resultado(nome_arquivo, resultado)
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
