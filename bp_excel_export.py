import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []

url_padrao = 'https://lista.mercadolivre.com.br/'

produto_usuario = input("Qual produto você deseja? ")

response = requests.get(url_padrao + produto_usuario)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.find_all('div', attrs={'class': 'ui-search-result__content'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'})
    link = produto.find('a', attrs={'class': 'ui-search-item__group__element shops__items-group-details ui-search-link'})

    preco = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})
    
    lista_produtos.append([titulo.text, preco.text, link['href']])
    
planilha = pd.DataFrame(lista_produtos, columns=['Titulo', 'Preco (R$)', 'Link'])

planilha.to_excel('produtos_pesquisa.xlsx', index=False)