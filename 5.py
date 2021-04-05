# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Informe um número que você deseja saber se é primo ou não: "))

count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print(f"{num} é primo." if count == 2 else f"{num} não é primo.")
