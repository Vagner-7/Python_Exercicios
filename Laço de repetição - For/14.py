quantidade = int(input())
c = 0
soma = 0
q = 0
media = 0
btw = []

for i in range(1, quantidade+1):
    entrada = input().split(" ")
    nome = ''
    preco = 0
    if len(entrada) == 2:
        nome = entrada[0]
        preco = entrada[1]
    elif len(entrada) > 2:
        preco = entrada[-1]
        nome = " ".join(entrada[:len(entrada) -1])
    preco = float(preco)
    if preco < 5:
        c += 1
    elif preco > 10:
        soma += preco
        q += 1
    elif 5 < preco < 10:
        btw.append(nome)
if q != 0:
    media = soma/q


print(f"Produtos com preço <R$ 5.00 = {c}")
print(f"Produtos com preço entre R% 5.00 e R$ 10.00 = {', '.join(btw)}")
print(f"Média dos produtos com preço > R$ 10.00 = R${media}")



