numero = 0
cont = 0
soma = 0


while numero != 999:
    cont += 1
    soma += numero
    numero = int(input())
print(f"Você digitou {cont} valores e a soma de todos eles é {soma}")
