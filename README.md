# Trabalho Avaliativo de Análise de Dados
### Instituição: Universidade Federal do Piauí
---

## Proposta:
Durante a disciplina de Análise de Dados ministrada pelo professor Arlino Magalhães, foi-se abordado a prática de *Web Scraping*, traduzindo para o português *Raspagem de Dados*, que em resumo trata-se de uma técnica utilizada para coletar dados de plataformas onlines, sites, redes sociais e afins.

Para o meu trabalho, o foco foi voltado para a plataforma de comércio eletrônico **Mercado Livre**. Fundada em 1999 e tendo sede em Montevidéu Uruguai, a empresa oferece soluções de comércio virtual, onde pessoas e empresas possam comprar, vender, negociar, anunciar e enviar produtos pela internet.

**O objetivo foi o seguinte**: Criar uma interação entre o usuário e a prática do Web Scraping, onde seja possível o usuário pesquisar por um determinado produto e receber um arquivo em formato xlsx(Excel) os dados organizados em uma planilha detalhada com nome, preço e endereço da página.

# Os arquivos .py estão divididos da seguinte maneira:

## 1. buscador_produto.py
Este algoritmo é simples, utilizando da biblioteca 'request' e 'BeautifulSoup', foi-se extraído dados apenas de um único produto na página

## 2. bp_dataframe.py
Aqui introduzi a biblioteca do 'Pandas' para criar um DataFrame de vários produto já carregados na página. **O resultado é mostrado apenas no terminal.**

## 1. bp_excel_export.py
Por fim, o algoritmo defitivo do objetivo do trabalho. Aqui todo o processo é realizado, desde a raspagem, passando pela coleta e organização dos dados em um DataFrame para no final, através do método 'to_excel' o DataFrame seja exportado para um arquivo xlsx
