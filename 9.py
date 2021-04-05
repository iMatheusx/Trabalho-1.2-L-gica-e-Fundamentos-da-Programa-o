# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
# se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é
# jovem, adulta ou idosa, conforme a média calculada.
pessoas = int(input("Informe o número de pessoas na turma: "))
a = 0
soma = 0
while a < pessoas:
    a += 1
    nota = int(input("Informe a idade da pessoa: "))
    soma += nota
media = soma // pessoas
print(f"a média aritmética das notas é {media}")

if media > 0 and media <= 25:
    print("A turma pode ser considerada jovem")
if media >= 26 and media <= 60:
    print("A turma pode ser considerada adulta")
if media > 60:
    print("A turma pode ser considerada idosa")
