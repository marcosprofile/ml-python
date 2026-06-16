""" SEQUÊNCIA DE FIBONACCI """

# Parte 1: Configuração inicial
# Crie variáveis: limite_termos = 10 e limite_valor = 100
# Imprima um cabeçalho "SEQUÊNCIA DE FIBONACCI"
# Imprima as informações sobre os limites e a definição da sequência


LIMITE_TERMOS = 10
LIMITE_VALOR = 100

TEXTO = f"""
{"=" * 60}
{"SEQUÊNCIA DE FIBONACCI":^60}
{"=" * 60}
Limite de termos: {LIMITE_TERMOS}
Limite de valor: {LIMITE_VALOR}
{"=" * 60}
"""

print(TEXTO)

###############################################################################

# Parte 2: Gerar sequência de Fibonacci usando for
# Crie uma lista fibonacci = [0, 1] (inicializa com os dois primeiros termos)
# Use um laço for com range(2, limite_termos) para gerar os próximos termos
# Para cada índice:
# # calcule o próximo termo como fibonacci[i-1] + fibonacci[i-2]
# Use append() para adicionar cada termo à lista
# Após o laço, use outro laço for para exibir a sequência completa


fibonacci = [0, 1]

for valor in range(2, LIMITE_TERMOS):
    proximo = fibonacci[valor-1] + fibonacci[valor-2]
    fibonacci.append(proximo)

print(f"Sequência de Fibonacci com laço For:   {fibonacci}")


###############################################################################


# Parte 3: Gerar sequência usando while até atingir um valor limite
# Crie uma lista fibonacci_while = [0, 1] e indice = 2
# Use um laço while True para gerar termos indefinidamente
# Dentro do laço, calcule o próximo termo
# Se o próximo termo ultrapassar LIMITE_VALOR, use break para parar
# Caso contrário, adicione o termo à lista e incremente o índice
# Após o laço, use um laço for para exibir a sequência completa


fibonacci_while = [0, 1]
indice = 2

while True:
    proximo = fibonacci_while[indice - 1] + fibonacci_while[indice - 2]

    if len(fibonacci_while) >= LIMITE_TERMOS:
        break

    fibonacci_while.append(proximo)
    indice += 1

print(f"Sequência de Fibonacci com laço While: {fibonacci_while}")
