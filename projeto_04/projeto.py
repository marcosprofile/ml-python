""" Extração de Dados e Geração de Relatório """
# Objetivo do projeto
# 1. Ler vendas.csv
# 2. Processar (totais, médias, destaques)
# 3. Agrupar por produto
# 4. Gerar e salvar um relatório .txt


import csv

# 1. Carregar dados do CSV
# Carregue vendas.csv, converta tipos e armazene em uma lista
CAMINHO = "vendas.csv"
vendas = []

with open(CAMINHO, "r", encoding="utf-8", newline="") as arquivo:
    reader = csv.DictReader(arquivo)
    for linha in reader:
        linha["Quantidade"] = int(linha["Quantidade"])
        linha["Preco"] = float(linha["Preco"])
        vendas.append(linha)

print(f"Total de vendas carregadas: {len(vendas)}")

###############################################################################

# 2. Validar dados
# Veja se vendas está vazia, se Produto é válido, Quantidade > 0 e Preco > 0
erros = []

if not vendas:
    erros.append("Erro: Nenhuma venda foi carregada.")
else:
    for indice, venda in enumerate(vendas):
        produto = venda.get("Produto", "").strip()
        quantidade = venda.get("Quantidade")
        preco = venda.get("Preco")

        if not produto:
            erros.append(f"Linha {indice + 1}: Produto inválido.")
        if not isinstance(quantidade, int):
            erros.append(f"Linha {indice + 1}: Quantidade inválida.")
        elif quantidade <= 0:
            erros.append(f"Linha {indice + 1}: Quantidade deve ser > 0.")
        if not isinstance(preco, float):
            erros.append(f"Linha {indice + 1}: Preço inválido.")
        elif preco <= 0:
            erros.append(f"Linha {indice + 1}: Preço deve ser > 0.")

if erros:
    for erro in erros:
        print(erro)
    raise SystemExit(1)
else:
    print("Validação concluída: Nenhum erro encontrado!")

###############################################################################

# 3. Calcular valores totais e estatísticas
# Calcule ValorTotal para cada venda e as estatísticas gerais
# # total_registros, total_unidades, valor_total, valor_medio
for venda in vendas:
    quantidade = int(venda["Quantidade"])
    preco = float(venda["Preco"])
    venda["ValorTotal"] = quantidade * preco

TOTAL_REGISTROS = len(vendas)
total_unidades = sum(int(venda["Quantidade"]) for venda in vendas)
valor_total = sum(float(venda["ValorTotal"]) for venda in vendas)
VALOR_MEDIO = valor_total / TOTAL_REGISTROS if TOTAL_REGISTROS > 0 else 0

print(f"Total de registros: {TOTAL_REGISTROS}")
print(f"Total de unidades: {total_unidades}")
print(f"Valor total: R$ {valor_total:,.2f}")
print(f"Valor médio: R$ {VALOR_MEDIO:,.2f}")

###############################################################################

# 4. Agrupar por produto
# Agrupe as vendas por produto, somando quantidade_total e valor_total
por_produto = {}

for venda in vendas:
    produto = venda["Produto"]
    quantidade = int(venda["Quantidade"])
    valor_total = float(venda["ValorTotal"])
    if produto not in por_produto:
        por_produto[produto] = {"quantidade_total": 0, "valor_total": 0.0}
    por_produto[produto]["quantidade_total"] += quantidade
    por_produto[produto]["valor_total"] += valor_total

print(f"Total de produtos: {len(por_produto)}")

# Encontre o produto com maior quantidade_total e o com maior valor_total
# # (sem usar lambda)
produto_maior_quantidade = None
maior_qtd = 0
for produto, dados in por_produto.items():
    if dados["quantidade_total"] > maior_qtd:
        maior_qtd = int(dados["quantidade_total"])  # garantir tipo inteiro
        produto_maior_quantidade = (produto, dados)

produto_maior_valor = None
maior_valor = 0.0
for produto, dados in por_produto.items():
    if dados["valor_total"] > maior_valor:
        maior_valor = dados["valor_total"]
        produto_maior_valor = (produto, dados)

if produto_maior_quantidade:
    p_qtd, d_qtd = produto_maior_quantidade
    print(f"Maior quantidade: {p_qtd} ({d_qtd['quantidade_total']} unidades)")

if produto_maior_valor:
    p_valor, d_valor = produto_maior_valor
    print(f"Maior faturamento: {p_valor} (R$ {d_valor['valor_total']:,.2f})")

###############################################################################

# 5. Gerar relatório
# Crie o cabeçalho do relatório, adicione estatísticas gerais e destaques

linhas = []
linhas.append("=" * 60)
linhas.append("RELATÓRIO DE VENDAS")
linhas.append("=" * 60)
linhas.append("")
linhas.append("ESTATÍSTICAS GERAIS")
linhas.append("-" * 60)
linhas.append(f"Total de registros: {TOTAL_REGISTROS}")
linhas.append(f"Total de unidades: {total_unidades}")
linhas.append(f"Valor total: R$ {valor_total:,.2f}")
linhas.append(f"Valor médio: R$ {VALOR_MEDIO:,.2f}")
linhas.append("")
linhas.append("DESTAQUES")
linhas.append("-" * 60)
linhas.append(f"Produto com maior quantidade: {p_qtd} ({d_qtd['quantidade_total']} unidades)")
linhas.append(f"Produto com maior faturamento: {p_valor} (R$ {d_valor['valor_total']:,.2f})")
linhas.append("")

# Adicione o detalhamento por produto (ordenado por faturamento) e finalize o relatório
linhas.append("DETALHAMENTO POR PRODUTO (por faturamento)")
linhas.append("-" * 6)
produtos_ordenados = sorted([(dados["valor_total"], produto, dados) for produto, dados in por_produto.items()], reverse=True)
for valor_total, produto, dados in produtos_ordenados:
    linhas.append(f"{produto}: {dados['quantidade_total']} unidades – R$ {dados['valor_total']:,.2f}")
linhas.append("")
linhas.append("=" * 60)
linhas.append("Fim do relatório")
linhas.append("=" * 60)
TEXTO_RELATORIO = "\n".join(linhas)

###############################################################################

# 6. Visualizar e salvar relatório
# Mostre uma prévia das primeiras 20 linhas do relatório
for linha_texto in linhas:
    print(linha_texto)

# Salve o relatório em "relatorio_vendas.txt"
with open("relatorio_vendas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(TEXTO_RELATORIO)
print("Relatório salvo em: relatorio_vendas.txt")

###############################################################################

# Resumo do Projeto

# Apliquei:
# - leitura de CSV (csv.DictReader)
# - listas/dicionários para organizar e agrupar
# - compreensões de listas
# - geração e escrita de relatório .txt
# - validação de dados
