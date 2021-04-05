# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Informe um número que você deseja saber se é primo ou não: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
        print(f"{num} é divisivel por {i}")
print(f"Então {num} é primo." if count == 2 else f"Então {num} não é primo.")









