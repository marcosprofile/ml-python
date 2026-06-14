# Parte 1: Cadastro de Usuário
# Crie as seguintes variáveis para o usuário:
# - nome = "João Silva"
# - idade = 25
# - e_estudante = True
# - tem_carteira_biblioteca = True
# - tem_multa_pendente = False
# Imprima os dados formatados

NOME = "João Silva"
IDADE = 25
E_ESTUDANTE = True
TEM_CARTEIRA_BIBLIOTECA = True
TEM_MULTA_PENDENTE = False

CADASTRO_USUARIO = f"""
{"=" * 60}
{"DADOS DO USUÁRIO":^60}
{"=" * 60}

Nome: {NOME}
Idade: {IDADE}
Estudante: {E_ESTUDANTE}
Carteira Biblioteca: {TEM_CARTEIRA_BIBLIOTECA}
Multa Pendente: {TEM_MULTA_PENDENTE}

{"=" * 60}
"""

print(CADASTRO_USUARIO)

##########################################################################

# Parte 2: Validação de Elegibilidade
# Verifique se o usuário pode usar a biblioteca:
# - Idade mínima: 12 anos
# - Deve ter carteira da biblioteca
# - Não pode ter multas pendentes
# Se elegível, verifique o tipo (estudante tem 15 dias, regular tem 10 dias)
# Escreva seu código aqui

elegibilidade = False
tempo_com_livro = 0

if IDADE >= 12 and TEM_CARTEIRA_BIBLIOTECA and not TEM_MULTA_PENDENTE:
    elegibilidade = True
    if E_ESTUDANTE:
        tempo_com_livro = 15
    else:
        tempo_com_livro = 10
else:
    print("A pessoa não pode acessar a biblioteca.")


VALIDACAO_DE_ELEGIBILIDADE = f"""
{"=" * 60}
{"VERIFICAÇÃO DE ELEGIBILIDADE":^60}
{"=" * 60}

Nome: {NOME}
É elegível a acessar a biblioteca? {elegibilidade}
É estudante: {E_ESTUDANTE}

É possível alugar um livro por {tempo_com_livro} dias.

{"=" * 60}
"""

print(VALIDACAO_DE_ELEGIBILIDADE)

##########################################################################

# Parte 3: Sistema de Empréstimo
# Crie variáveis para o empréstimo:
# - nome_livro = "Python para Iniciantes"
# - dias_emprestimo = 12
# - prazo_maximo = 10 (regular)
# - prazo_estudante = 15
# Determine o prazo baseado no tipo de usuário
# Calcule se está em atraso ou quantos dias restam
# Escreva seu código aqui

NOME_LIVRO = "Python para Iniciantes"
DIAS_EMPRESTIMO = 12
PRAZO_MAXIMO = 10
PRAZO_ESTUDANTE = 15

if E_ESTUDANTE:
    PRAZO_PERMITIDO = PRAZO_ESTUDANTE
    TIPO_USUARIO = "Estudante"
else:
    PRAZO_PERMITIDO = PRAZO_MAXIMO
    TIPO_USUARIO = "Regular"

# verificar se há dias em atraso
DIAS_ATRASO = DIAS_EMPRESTIMO - PRAZO_PERMITIDO
DIAS_RESTANTES = max(0, PRAZO_PERMITIDO - DIAS_EMPRESTIMO)

if DIAS_ATRASO > 0:
    print(f"O livro \"{NOME_LIVRO}\" está em atraso em {DIAS_ATRASO} dias.")
else:
    DIAS_RESTANTES = PRAZO_PERMITIDO - DIAS_EMPRESTIMO

RELATORIO_DE_EMPRESTIMO = f"""
{"=" * 60}
{"RELATÓRIO DE EMPRÉSTIMO":^60}
{"=" * 60}

USUÁRIO:
Nome: {NOME}
Tipo de usuário: {TIPO_USUARIO}

DADOS DO EMPRÉSTIMO:
Livro emprestado: {NOME_LIVRO}
Dias de empréstimo: {DIAS_EMPRESTIMO}
Prazo permitido: {PRAZO_PERMITIDO}
Dias em atraso: {DIAS_ATRASO}
Dias restantes: {DIAS_RESTANTES}

Você pode usar o livro \"{NOME_LIVRO}\" por {DIAS_RESTANTES} dias.
{"=" * 60}
"""

print(RELATORIO_DE_EMPRESTIMO)

##########################################################################

# Parte 5: Sistema de Renovação
# Crie variáveis: numero_renovacoes = 1, tem_reserva = False
# Verifique se pode renovar considerando:
# - Não pode estar em atraso
# - Máximo de 2 renovações
# - Não pode ter reserva
# - Não pode ter multa pendente
# Se pode renovar, calcule o novo prazo
# Escreva seu código aqui


# Sistema de Renovação
NUMERO_RENOVACOES = 1
TEM_RESERVA = False

print("\n" + "=" * 60)
print("SISTEMA DE RENOVAÇÃO".center(60))
print("=" * 60)

# Verificar Condições para renovação
pode_renovar = True
motivo_impedimento = ""

# Verificar se está em atraso
if DIAS_ATRASO > 0:
    pode_renovar = False
    motivo_impedimento = "Livro em atraso – Devolva primeiro"
elif NUMERO_RENOVACOES >= 2:
    pode_renovar = False
    motivo_impedimento = "Limite de renovações atingido (máximo: 2)"
elif TEM_RESERVA:
    pode_renovar = False
    motivo_impedimento = "Livro reservado por outro usuário"
elif TEM_MULTA_PENDENTE:
    pode_renovar = False
    motivo_impedimento = "Multa pendente deve ser quitada"

# Exibir resultado
if pode_renovar:
    print("– Renovação PERMITIDA")
    print(f"Renovações realizadas: {NUMERO_RENOVACOES}/2")

    # Calcular novo prazo
    if E_ESTUDANTE:
        novo_prazo = PRAZO_ESTUDANTE
    else:
        novo_prazo = PRAZO_MAXIMO

    print(f"Novo prazo: {novo_prazo} dias a partir de hoje")
else:
    print("– Renovação NEGADA")
    print(f"Motivo: {motivo_impedimento}")

print("=" * 60)

##########################################################################

# Parte 6: Relatório Final
# Crie um relatório completo exibindo:
# - Dados do usuário
# - Status de elegibilidade
# - Informações do empréstimo
# - Valor da multa (se houver)
# - Status de renovação
# Use formatação para deixar o relatório organizado
# Escreva seu código aqui


# Gerar Relatório Final
print("\n" + "=" * 60)
print("RELATÓRIO COMPLETO DA BIBLIOTECA".center(60))
print("=" * 60)

# Dados do Usuário
print("\n – DADOS DO USUÁRIO:")
print(f" Nome: {NOME} | Idade: {IDADE} anos")
if E_ESTUDANTE:
    print(" Tipo: Estudante")
else:
    print(" Tipo: Usuário Regular")

# Status
print("\n – STATUS:")
if elegibilidade:
    print(" Elegibilidade: APROVADO")
else:
    print(f" Elegibilidade: NEGADO – {motivo_impedimento}")

# Empréstimo
print("\n – EMPRÉSTIMO:")
print(f" Livro: {NOME_LIVRO}")
print(f" Dias desde empréstimo: {DIAS_EMPRESTIMO} dias")
print(f"Prazo permitido: {PRAZO_PERMITIDO} dias")

if DIAS_ATRASO > 0:
    print(f" Status: ATRASADO ({DIAS_ATRASO} dias)")
else:
    DIAS_RESTANTES = PRAZO_PERMITIDO - DIAS_EMPRESTIMO
    print(f" Status: NO PRAZO ({DIAS_RESTANTES} dias restantes)")

# Multa
MULTA_FINAL = 0

print("\n – MULTA:")
if MULTA_FINAL > 0:
    print(f" Valor: R$ {MULTA_FINAL:.2f}")
else:
    print(" Valor: R$ 0,00 – Sem multa")

# Renovação
print("\n RENOVAÇÃO:")
if pode_renovar:
    print(f" Status: DISPONÍVEL ({NUMERO_RENOVACOES}/2 renovações)")
else:
    print(f" Status: NÃO DISPONÍVEL – {motivo_impedimento}")

print("\n" + "=" * 60)
