valores = []

for num in range(0, 5):
    valores.append(int(input("Digite um valor")))

for valor in valores:
    print(f"Os valores da lista são {valor}")
for pos,valor in enumerate(valores):
    print(f"Na posição {pos} tem o valor {valor}")

a = [2, 3, 4, 7]
b = a
print(a)
print(b)