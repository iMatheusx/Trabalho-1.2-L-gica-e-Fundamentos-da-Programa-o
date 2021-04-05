#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n1 = int(input("Informe o n1: "))
n2 = int(input("Informe o n2: "))
n3 = int(input("Informe o n3: "))

while ((n1 > 1000 or n1 < 0) or (n2 > 1000 or n2 < 0) or (n3 > 1000 or n3 < 0)):
    print("Um dos números não é válido, informe-os novamente!")
    n1 = int(input("Informe o n1: "))
    n2 = int(input("Informe o n2: "))
    n3 = int(input("Informe o n3: "))
if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número entre eles!')
    if n2 > n3:
       print(f'{n3} é o menor número entre eles! ')
    else:
        print(f'{n2} é o menor número entre eles! ')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número entre eles!')
    if n1 > n3:
        print(f'{n3} é o menor número entre eles! ')
    else:
        print(f'{n1} é o menor número entre eles! ')
else:
    print(f'{n3} é o maior número entre eles!')
    if n1 > n2:
        print(f'{n2} é o menor número entre eles! ')
    else:
        print(f'{n1} é o menor número entre eles! ')
print(f"a soma de {n1} + {n2} + {n3} é {n1 + n2 + n3}")