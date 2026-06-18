""" Leitura e Escrita de Arquivos """

# importando metodo ou classe
import csv

# 1. Arquivos de texto (.txt)

# Defina arquivo_nome = "exemplo.txt"
# Use with open() no modo "w" (write) para escrever no arquivo
# Escreva "linha 1\n" e "linha 2\n" no arquivo
# Use with open() no modo "a" (append) para adicionar ao final
# Escreva "linha 3 (append)\n" no arquivo
# Use with open() no modo "r" (read) com encoding="utf-8" para ler o arquivo
# Use um for com enumerate para ler cada linha e imprimir cada linha numerada
# # (use rstrip() para remover quebras de linha)

ARQUIVO_NOME = "exemplo.txt"

with open(ARQUIVO_NOME, "w", encoding="utf-8") as arquivo:
    arquivo.write("linha 1\n")
    arquivo.write("linha 2\n")

with open(ARQUIVO_NOME, "a", encoding="utf-8") as arquivo:
    arquivo.write("Esta é uma nova linha.")

with open(ARQUIVO_NOME, "r", encoding="utf-8") as arquivo:
    for i, linha in enumerate(arquivo, start=1):
        print(f"{i}: {linha.rstrip()}")

arquivo = open("exemplo.txt", "r", encoding="utf-8")
for linha in arquivo:
    print(linha.rstrip())

arquivo.close()

###############################################################################

# 2. Arquivos CSV

# Importe o módulo csv
# Crie uma lista de dicionários chamada dados com informações de pessoas
# Cada dicionário deve ter as chaves "Nome", "Idade" e "Cidade"
# Crie uma lista campos = ["Nome", "Idade", "Cidade"] com os nomes das colunas

lista_dic = [
    {"Nome": "João", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Maria", "Idade": 30, "Cidade": "Rio de Janeiro"},
]

campos = ["Nome", "Idade", "Cidade"]

# Use with open() para criar um arquivo "pessoas.csv" no modo "w"
# Crie um csv.DictWriter passando o arquivo e fieldnames=campos
# Use writeheader() para escrever o cabeçalho do CSV
# Use writerows(dados) para escrever todos os dados
# Imprima uma mensagem confirmando que o arquivo foi criado

NOME_FILE = "pessoas.csv"
with open(NOME_FILE, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerows(lista_dic)


# Use with open() para ler o arquivo "pessoas.csv" no modo "r"
# Crie um csv.DictReader passando o arquivo
# Converta o reader para uma lista chamada pessoas
# Imprima o total de pessoas lidas
# Use um laço for para imprimir cada pessoa no formato "Nome, Idade anos"

with open(NOME_FILE, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    pessoas = list(reader)


# Use uma compreensão de lista para filtrar pessoas com idade >= 18
# Converta a idade para int antes de comparar
# Use with open() para criar um arquivo "pessoas_maiores.csv" no modo "w"
# Crie um csv.DictWriter passando o arquivo e fieldnames=campos
# Use writeheader() para escrever o cabeçalho
# Use writerows() para escrever os dados filtrados
# Imprima uma mensagem com o número de registros criados

maiores = [pessoa for pessoa in pessoas if int(pessoa["Idade"]) >= 28]
with open("pessoas_maiores.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerows(maiores)

###############################################################################

# 3. Boas práticas

# Defina nome_arquivo = "exemplo.txt"
# Use um bloco try/except para tratar erros ao ler o arquivo
# Dentro do try, use with open() no modo "r" para ler o arquivo
# Use read() para ler todo o conteúdo e imprima
# No except, com FileNotFoundError, imprima a mensagem: Arquivo não encontrado.

NOME_ARQUIVO = "exemplo2.txt"

try:
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Arquivo não encontrado.")


###############################################################################

# 4. Exercício

# Use with open() para criar um arquivo "notas.txt" no modo "w"
# Escreva 4 linhas no formato:
# # "Nome:Nota" (ex: "Maria:8.5\n", "João:7.0\n", etc.)
# Crie uma lista vazia chamada notas
# Use with open() para ler o arquivo "notas.txt" no modo "r"
# Use um laço for para ler cada linha do arquivo
# Para cada linha, use strip() e split(":") para separar nome e nota
# Converta a nota para float e adicione à lista notas
# Imprima cada nome e nota
# Após o laço, calcule a média das notas (soma dividida pelo tamanho)
# Se houver notas, imprima a média formatada com 2 casas decimais


# Criar arquivo com notas
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Maria:8.5\n")
    f.write("João:7.0\n")
    f.write("Pedro:9.0\n")
    f.write("Ana:6.5\n")

# Ler arquivo e calcular média
notas = []
with open("notas.txt", "r", encoding="utf-8") as f:
    for linha in f:
        nome, nota_str = linha.strip().split(":")
        nota = float(nota_str)
        notas.append(nota)
        print(f"{nome}: {nota}")

# Calcular média
if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia das notas: {media:.2f}")
