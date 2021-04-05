#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input("Até qual número você deseja saber os números primos? "))
primos = 0
divisoes = 0
count = 0
num = 0
print(f"Os números primos entre 1 e {n} são:")
for i in range(2, n):
    count = 0
    for a in range(1, n + 1):
        if i % a == 0:
            count += 1
            divisoes += 1
    if count == 2:
        primos += 1
        print(f"{i}")
print(f"Foram encontrados {primos} números primos")
print(f"Foram realizadas {divisoes} divisões para encontrar estes números primos")
