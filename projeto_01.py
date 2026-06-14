"""SISTEMA DE CADASTRO DE ALUNOS"""

# Variáveis para armazenar as informações do aluno
NOME = "John Doe "
IDADE = 20
EMAIL = "JOHN.Doe@email.com"
MATRICULA = 2026060920

CADASTRO_ALUNO = f"""
{'=' * 60}
{'CADASTRO DO ALUNO':^60}
{'=' * 60}
Nome: {NOME}
Idade: {IDADE}
Email: {EMAIL}
Matrícula: {MATRICULA}
{'=' * 60}
"""

print(CADASTRO_ALUNO)

##########################################################################

# Validação do Email
# Verifique se o email:
# - contém "@"
# - não tem espaços
# - tem pelo menos 5 caracteres

EMAIL_VALIDO = ("@" in EMAIL) and (len(EMAIL) > 5) and (' ' not in EMAIL)

# Validação da Idade
# Verifique se a idade é maior que 0 e menor que 120

IDADE_VALIDA = (IDADE > 0) and (IDADE < 120)

# Validação do Nome
# Verifique se o nome não está vazio (após remover espaços)

NOME_VALIDO = len(NOME.strip()) > 0

# Validação geral
# Combine todas as validações usando operadores lógicos

DADOS_VALIDOS = EMAIL_VALIDO and IDADE_VALIDA and NOME_VALIDO

# Imprima os resultados das validações
# Escreva seu código aqui

VALIDACAO_DE_DADOS = f"""
{'=' * 60}
{'RESULTADO DAS VALIDAÇÕES':^60}
{'=' * 60}
Nome é valido? {NOME_VALIDO}
Idade é valida? {IDADE_VALIDA}
Email é valido? {EMAIL_VALIDO}

Dados são validos? {DADOS_VALIDOS}
{'=' * 60}
"""

print(VALIDACAO_DE_DADOS)

##########################################################################

# Conversão e Cálculo de notas
# Converter notas de texto para float
# Use float() para converter cada nota
nota01 = float("2")
nota02 = float("5")
nota03 = float("8")

# Calcular a média
# Some as três notas e divida por 3
soma = nota01 + nota02 + nota03
media = soma / 3

# Imprima um cabeçalho "CÁLCULO DE NOTAS" e exiba as notas e a média
# Escreva seu código aqui
CALCULO_DE_NOTAS = f"""
{'=' * 60}
{'CÁLCULO DE NOTAS':^60}
{'=' * 60}
As notas do aluno são:
Nota 01: {nota01}
Nota 02: {nota02}
Nota 03: {nota03}

Média: {media}
{'=' * 60}
"""

print(CALCULO_DE_NOTAS)

##########################################################################

# Verificar aprovação
# Defina a nota mínima como 7.0
# Verifique se foi aprovado (média >= nota_minima)

NOTA_MINIMA = 7
aluno_aprovado = media >= NOTA_MINIMA

# Verificar se está em recuperação (média entre 5.0 e 6.9)
# Use operadores relacionais e lógicos
em_recuperacao = media >= 5 and media <= 6.9

# Verificar se foi reprovado (média < 5.0)
reprovado = media < 5

# Imprima um cabeçalho "VERIFICAÇÃO DE APROVAÇÃO" e exiba os resultados
# Escreva seu código aqui
VERIFICACAO_DE_APROVACAO = f"""
{'=' * 60}
{'VERIFICAÇÃO DE APROVAÇÃO':^60}
{'=' * 60}
Aluno aprovado? {aluno_aprovado}
Aluno em recuperação? {em_recuperacao}
Aluno reprovado? {reprovado}
{'=' * 60}
"""

print(VERIFICACAO_DE_APROVACAO)

##########################################################################

# Limpar e formatar o nome
# Use strip() para remover espaços extras e title() para capitalizar
NOME_FORMATADO = NOME.strip().title()

# Formatar email
# Use strip() para remover espaços e lower() para minúsculas
EMAIL_FORMATADO = EMAIL.strip().lower()

# Imprima um cabeçalho "FORMATAÇÃO DE DADOS"
# exiba os dados originais e formatados
FORMATACAO_DE_DADOS = f"""
{'=' * 60}
{'FORMATAÇÃO DE DADOS':^60}
{'=' * 60}

Dados originais:
Nome: {NOME}
Idade: {IDADE}
Email: {EMAIL}

Dados formatados:
Nome: {NOME_FORMATADO}
Idade: {IDADE}
Email: {EMAIL_FORMATADO}
{'=' * 60}
"""
print(FORMATACAO_DE_DADOS)

##########################################################################

# Gerar relatório formatado
# Calcule os pontos necessários para aprovação (se não aprovado)
# Crie um relatório usando f-strings com:
#   - Cabeçalho formatado
#   - Dados do aluno
#   - Notas e média
#   - Resultado (aprovado, recuperação, reprovado)
#   - Pontos necessários
# Escreva seu código aqui

pontos_necessarios = NOTA_MINIMA - media

RELATORIO_FINAL = f"""
{'=' * 60}
{'RELATÓRIO DO ALUNO':^60}
{'=' * 60}
Nome: {NOME_FORMATADO}
Idade: {IDADE}
Email: {EMAIL_FORMATADO}


NOTAS:
  Nota 1: {nota01}
  Nota 2: {nota02}
  Nota 3: {nota03}
  Média: {media}


RESULTADO:
  Aprovado: {aluno_aprovado}
  Em recuperação: {em_recuperacao}
  Reprovado: {reprovado}


PONTOS NECESSÁRIOS:
  {pontos_necessarios if pontos_necessarios > 0 else '–'}
"""

print(RELATORIO_FINAL)
