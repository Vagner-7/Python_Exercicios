c = 0
soma = 0
maior = 0
menor = 0
continua = 'S'

while continua == 'S':
    numero = int(input("Digite um valor"))
    soma += numero
    c += 1
    if c == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continua = input("Deseja continuar? [S/N]: ").upper()
print(f"Voce digitou {c} numeros")
print(f"A média é {soma/c}")
print(f"A soma dos valores é {soma}")
print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")


