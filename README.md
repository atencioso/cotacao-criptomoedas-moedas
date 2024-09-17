# Cotação de Criptomoedas e Moedas

Este projeto é um script em Python que consulta a cotação de moedas e criptomoedas utilizando a API AwesomeAPI e exibe os resultados no terminal. Ele também salva os resultados em arquivos com a data da consulta para referência futura.

## Funcionalidades

- **Cotação de Moedas**:
  - Consulta as cotações do Dólar (USD) e do Euro (EUR) em relação ao Real (BRL).

- **Cotação de Criptomoedas**:
  - Consulta as cotações do Bitcoin (BTC) e do Litecoin (LTC) em relação ao Real (BRL).

- **Salvamento de Resultados**:
  - Salva os resultados das consultas em arquivos na pasta `results` com a data da consulta no nome do arquivo.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python: `requests`

## Instalação

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/atencioso/cotacao-criptomoedas-moedas.git
    cd cotacao-criptomoedas-moedas
    ```

2. **Instale as dependências**:

    Você pode instalar as dependências utilizando o `pip`:

    ```bash
    pip install requests
    ```

## Uso

1. **Execute o script**:

    ```bash
    python pesquisa.py
    ```

2. **Selecione uma opção no menu**:

    - **1** - Cotação de Moedas
    - **2** - Cotação de Criptomoedas
    - **0** - Sair

    Dependendo da opção escolhida, o script irá buscar as cotações e exibi-las no terminal. As informações também serão salvas em arquivos na pasta `results`.

## Estrutura do Projeto

- `pesquisa.py` - O script principal que realiza as consultas e salva os resultados.
- `results/` - Pasta onde os arquivos de resultados são salvos. O nome do arquivo inclui a data da consulta.

## Exemplo de Saída no Terminal

```bash
Cotação de Criptomoedas:

BTC para Real (BRL):

Compra: 332373
Venda: 332413

Último preço negociado não disponível para BTC.

LTC para Real (BRL):

Compra: 348.85
Venda: 349.64

Último preço negociado não disponível para LTC.
