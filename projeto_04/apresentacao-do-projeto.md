# Projeto - Extração de dados e geração de relatório

## Apresentação do Projeto

Este projeto integra todos os tópicos estudados:
- Leitura de arquivos CSV
- Processamento de dados com listas e dicionários
- Compreensões de listas e dicionários
- Geração de relatórios formatados
- Trabalho com arquivos de texto

<br>

## Objetivo do Projeto

construir um pipeline simples:
1. **Ler** `vendas.csv`
2. **Processar** (totais, médias, destaques)
3. **Agrupar** por produto
4. **Gerar** e salvar um relatório `.txt`

<br>

## Parte 1: Carregar dados do CSV

Leitura o arquivo CSV e conversão dos tipos de dados. Usei `csv.DictReader` para ler o arquivo como dicionário, facilitando o acesso aos dados por nome de coluna.

## Parte 2: Validar dados

Verificar se há erros nos dados carregados, como produtos vazios, quantidades ou preços inválidos. Isso garante que estamos trabalhando com dados consistentes.

## Parte 3: Calcular valores totais

Adicionar o valor total de cada venda e calcular estatísticas gerais:
- Total de registros
- Total de unidades vendidas
- Valor total das vendas
- Valor médio por venda

## Parte 4: Agrupar por produto

Agrupar as vendas por produto e encontrar os destaques:
- Produto com maior quantidade vendida
- Produto com maior faturamento

## Parte 5: Gerar relatório

Montar o texto do relatório formatado com:
- Cabeçalho
- Estatísticas gerais
- Destaques
- Detalhamento por produto (ordenado por faturamento)

## Parte 6: Visualizar e salvar relatório
Ver uma prévia do relatório e salvá-lo em arquivo de texto.

<br>

## Resumo

Apliquei:
- leitura de CSV (`csv.DictReader`)
- listas/dicionários para organizar e agrupar
- compreensões de listas
- geração e escrita de relatório `.txt`
- validação de dados