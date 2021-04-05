# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
# e o valor médio gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qtd_cd = int(input("Informe a quantidade de CDs adquirida pelo colecionador: "))

laço = 0
soma = 0
while laço < qtd_cd:
    laço += 1
    valor = float(input('Informe o valor gasto neste CD: '))
    soma += valor
media = soma // qtd_cd
print(f"A média de dinheiro gasto em CDs é de R${media}")