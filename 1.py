# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Informe um número que deseja saber a fatorial: "))

fatorial = 1

print(f"{num}! = ", end="")
for i in range(num, 0, -1):
    fatorial *= i
    resultado = fatorial
    print(f"{i}.", end="")
print(f" = {resultado}")


