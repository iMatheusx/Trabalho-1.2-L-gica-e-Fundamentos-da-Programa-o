# Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input("Digite o número de notas a serem atribuídas para calcular a média: "))
notas = ()
a = 0
soma = 0
while a < n:
    a += 1
    nota = float(input("Informe a nota: "))
    soma += nota
print(f"a média aritmética das notas é {soma / n}")