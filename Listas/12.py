matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_t = seg_col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o valor para [{l}][{c}]"))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print(f"A soma dos valores é {soma_par}")
for l in range(0, 3):
    soma_t += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {soma_t}")
for c in range(0, 3):
    if c == 0:
        seg_col = matriz[1][c]
    elif matriz[1][c] > seg_col:
        seg_col = matriz[1][c]
print(f"O maior da segunda linha é {seg_col}")

#complicado