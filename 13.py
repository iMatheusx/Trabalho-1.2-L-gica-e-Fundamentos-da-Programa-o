# O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
# Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém
# o número de itens que o cliente comprou e ao lado o valor da conta.
# Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços.
# Você foi contratado para desenvolver o programa que monta esta tabela de preços,
# que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
# Lojas Quase Dois - Tabela de preços 1 - R$ 1.99 2 - R$ 3.98 ... 50 - R$ 99.50
valor_item = 0
qtd = 0
while qtd < 50:
    qtd += 1
    valor_item += 1.99
    print(f"{qtd} - R${round(valor_item, 2)}")

# Sistema extra
choose = input("Deseja usar o sistema para calcular o valor em relação à quantidade de itens? S - SIM e N- NÃO: ")
if choose in "Ss":
    qtd_item = int(input("Informe a quantidade de itens da compra: "))
    laço = 0
    valor_total = 0
    while laço < qtd_item:
        laço += 1
        valor_total += 1.99
print(f"O valor da compra de {qtd_item} foi de R${round(valor_total, 2)}.")
