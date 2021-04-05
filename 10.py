# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.0

eleitores = int(input("Informe o número de eleitores: "))
a = 0
pedrin = 0
tonho = 0
cleber = 0

while a < eleitores:
    a += 1
    voto = input("Informe o número do candidato que deseja votar \npedrin borrachero - 1 \ntonho matador de porco - 2  \ncleber vendedor de paçoca - 3: ")
    if voto == "1":
        pedrin =+ 1
    if voto == "2":
        tonho += 1
    if voto == "3":
        cleber += 1
print(f"-------------- TOTAL DE VOTOS -------------- \nvotos no pedrin: {pedrin}; \n votos no tonho: {tonho};  \nvotos no cleber: {cleber}.")

if pedrin > tonho and pedrin > cleber:
    print("Pedrin borrachero foi o vencedor da eleição, dizq vai ter vale-pneu pra funcionário público")
elif tonho > pedrin and tonho > cleber:
    print("Tonho foi o ganhador da eleição, agora é só se bolear no torresmo e salame piazada!!")
elif cleber > tonho and cleber > pedrin:
    print("Cleber vendedor de paçoca foi o vencedor da eleição, paçoca pra geral!!")
elif cleber == tonho and cleber == pedrin:
    print("Deu empate, vamo fazer o desempate no truco, as duplas serão o prefeito e seu vice")