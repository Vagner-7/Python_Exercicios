tupla = tuple(int(input("digite um número: "))for num in range(1, 5))

print(f"Voce digitou os valores: {tupla}")
print(f"O número 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O número 3 apareceu na {tupla.index(3)+1}a posição")
else:
    print("O número 3 não está presente na tupla!")
print(f"Os valores pares digitados foram: ", end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

