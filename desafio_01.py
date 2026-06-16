"""DESAFIO: Sistema de Gestão de Loja"""


# 1. Crie dados do cliente:
#    - nome, idade, e_cliente_vip, tem_cadastro
# 2. Crie dados da compra:
#    - valor_compra, distancia
# 3. Valide o cliente (idade >= 18, tem cadastro)
# 4. Calcule desconto baseado nas regras especificadas
# 5. Calcule frete baseado na distância
# 6. Calcule o valor final (valor - desconto + frete)
# 7. Gere um relatório completo e organizado


# Parte 1. Dados do cliente
NOME = "John Doe"
IDADE = 25
E_CLIENTE_VIP = True
TEM_CADASTRO = True

# Parte 2. Dados da compra
VALOR_COMPRA = 300
DISTANCIA = 200

# Parte 3. Validação do cliente
if IDADE >= 18 and TEM_CADASTRO:
    CLIENTE_VALIDO = True
else:
    CLIENTE_VALIDO = False

desconto = float(0)

# Parte 4. Desconto
if VALOR_COMPRA >= 500:
    desconto = float(0.15)
elif VALOR_COMPRA >= 200:
    desconto = float(0.1)
elif VALOR_COMPRA >= 100:
    desconto = float(0.05)

if E_CLIENTE_VIP and desconto <= 0.25:
    desconto += 0.05

frete = 30

# Parte 5. Frete
if DISTANCIA < 50:
    if VALOR_COMPRA >= 200:
        frete = 0
    else:
        frete = 20
elif DISTANCIA > 200:
    if VALOR_COMPRA >= 200:
        frete = 0
    else:
        frete = 30

# Parte 6. Valor final
valor_final = VALOR_COMPRA * (1 - desconto) + frete

# Parte 7. Relatório completo

print("=" * 60)
print("RELATÓRIO COMPLETO DA COMPRA".center(60))
print("=" * 60)

print("\n – DADOS DO CLIENTE:")
print(f" Nome: {NOME} \n Idade: {IDADE}")
if E_CLIENTE_VIP:
    print(" Tipo: Cliente VIP")
else:
    print(" Tipo: Cliente Regular")

print("\n – DADOS DA COMPRA:")
print(f" Valor da compra: R$ {VALOR_COMPRA:.2f}")
print(f" Distância: {DISTANCIA} km")

print("\n – STATUS:")
if CLIENTE_VALIDO:
    print(f" Cliente válido? {CLIENTE_VALIDO}")
else:
    print(f" Cliente válido? {CLIENTE_VALIDO}")
    print(" Motivo: Idade insuficiente ou não possui cadastro")

print("\n – DESCONTO:")
print(f" Valor: R$ {desconto * VALOR_COMPRA:.2f}")

print("\n – FRETE:")
print(f" Valor: R$ {frete:.2f}")

print("\n – VALOR FINAL:")
print(f" Valor: R$ {valor_final:.2f}")

print("\n" + "=" * 60)
