# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.

turmas = int(input("Informe o número de turmas: "))
a = 0
soma = 0
while a < turmas:
    pessoas = int(input("Informe a quantidade da pessoas para esta turma: "))
    if pessoas <= 40:
        print("Quantidade de pessoas cadastrada com sucesso.")
        a += 1
        soma += pessoas
    else:
        print("A turma não pode ter mais de 40 pessoas vinculadas")
media = soma // turmas
print(f"a média de pessoas por turma é {media}")