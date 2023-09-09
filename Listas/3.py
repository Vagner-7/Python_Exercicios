lista = []
pos_maior = []
pos_menor = []
for num in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {num}: ")))
print(f"Voce digitou os valores{lista}: ")
for pos, valor in enumerate(lista):
    if valor == max(lista):
        pos_maior.append(pos)
for pos, valor in enumerate(lista):
    if valor == min(lista):
        pos_menor.append(pos)
print(f"O maior valor encontrado foi:  {max(lista)} nas posições: {pos_maior}....")
print(f"O menor valor encontrado foi: {min(lista)} na posições: {pos_menor}....")