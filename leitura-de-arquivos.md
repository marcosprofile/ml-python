# Leitura e escrita de arquivos

## Arquivos de texto (.txt) — o essencial

O que você precisa dominar:
- abrir/fechar corretamente com `with open(...)`
- modos mais usados: `"r"` (ler), `"w"` (sobrescrever), `"a"` (adicionar)
- ler com `read()` ou iterando linha a linha

A regra de ouro: use with + encoding="utf-8".

### Formas comuns de leitura
- `f.read()` para pegar tudo de uma vez
- `for linha in f` para ler de forma eficiente
- `f.readlines()` quando você realmente precisa de uma lista de linhas

### Modos mais usados
- `"r"`: ler
- `"w"`: escrever (sobrescreve)
- `"a"`: adicionar ao final

Os demais existem, mas estes três resolvem a maioria dos casos.

<br>

## Arquivos CSV — o essencial

CSV é muito comum em dados tabulares. Em Python, o caminho mais seguro é usar o módulo csv (evita bugs de vírgula/escape).

### Ler e escrever com o módulo csv (recomendado)
- Use csv.DictReader para ler CSV como dicionário (acesso por nome da coluna)
- Use csv.DictWriter para escrever CSV a partir de dicionários

> **Importante**: use newline="" ao escrever CSV

### Observação

Use `newline=""` no `open(...)` ao escrever CSV (boa prática, especialmente no Windows).

<br>

## Boas práticas (curto e útil)
- use `with` (fecha automático)
- defina `encoding="utf-8"`
- trate `FileNotFoundError` quando o arquivo pode não existir
- evite "engolir" exceções genéricas sem necessidade

<br>

## Resumo

### Arquivos de Texto (.txt)
- Sempre use `with open(...)` para garantir fechamento automático
- Sempre defina `encoding="utf-8"` para caracteres especiais
- Modos principais:
- - `"r"`: ler (read)
- - `"w"`: escrever/sobrescrever (write)
- - `"a"`: adicionar ao final (append)

``` python
# Escrever
with open("arquivo.txt", "w", encoding="utf-8") as f:
    f.write("conteúdo\n")

# Ler linha a linha (eficiente)
with open("arquivo.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())
```

### Arquivos CSV
- Use o módulo `csv` para evitar problemas com vírgulas e escapes
- `csv.DictReader`: lê CSV como dicionário (acesso por nome da coluna)
- `csv.DictWriter`: escreve CSV a partir de dicionários

> **Importante**: use `newline=""` ao escrever CSV

``` python
import csv

# Ler CSV
with open("dados.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    dados = list(reader)

# Escrever CSV
with open("saida.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["nome", "idade"])
    writer.writeheader()
    writer.writerows(dados)
```

### Boas Práticas
- Sempre use with (fecha arquivo automaticamente)
- Sempre defina encoding="utf-8"
- Trate FileNotFoundError quando o arquivo pode não existir
- Use csv.DictReader/DictWriter para CSV (mais seguro)

### Tratamento de Erros

``` python
try:
    with open("arquivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Arquivo não encontrado!")
```