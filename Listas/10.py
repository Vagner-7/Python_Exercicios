lista = [[], []]
for n in range(1, 8):
    numero = int(input(f"Digite o {n} valor: "))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print(f"par{sorted(lista[0])}")
print(f"ímpar{sorted(lista[1])}")