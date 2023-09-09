from datetime import datetime
ano_atual = datetime.now().year
maior = 0
menor = 0

for c in range(7):
    ano_nasc = int(input())
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1

print(maior)
print(menor)
