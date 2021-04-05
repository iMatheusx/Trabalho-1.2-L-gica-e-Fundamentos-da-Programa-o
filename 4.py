# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
# fatorial a números inteiros positivos e menores que 16.

num = (input("Informe um número que deseja saber a fatorial (deve ser inteiro, positivo e menor que 16): "))
fatorial = 1
while not (num.isnumeric()):
    print(f"{num} não é um número INTEIRO, tente novamente com um número inteiro, positivo e menor que 16.")
    num = input("Informe um número que deseja saber a fatorial: ")
while (type(num) != int):
    num = int(num)
    while (num < 0 or num > 16):
        num = int(num)
        print(f"{num} não é um número válido, tente novamente com um número inteiro, positivo e menor que 16.")
        num = int(input("Informe um número que deseja saber a fatorial: "))

    while (num > 0 and num <= 16):
        print(f"{num}! = ", end="")
        for i in range(num, 0, -1):
            fatorial *= i
            resultado = fatorial
            print(f"{i}.", end="")
        print(f" = {resultado}")
        choose = input("Deseja escolher outro número para o cálculo? Sim = S, Não = N: ")
        if choose in "Ss":
            num = int(input("Informe um número que deseja saber a fatorial (deve ser inteiro, positivo e menor que 16): "))
        else:
            print("processo encerrado")
            break
