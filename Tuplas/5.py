from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("Os números sorteados em ordem foram: ", end='')
for n in numeros:
    print(f"{n} ", end='')

print(f"\nO maior valor foi: {max(numeros)}")
print(f"O menor falor foi: {min(numeros)}")
