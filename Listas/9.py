geral = []
dado = []
maior = menor = 0
while True:
    dado.append(input("Nome: "))
    dado.append(float(input("Peso: ")))
    if len(geral) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    continuar = input("Deseja continuar? [S/N]").upper()
    geral.append(dado[:])
    dado.clear()
    while continuar not in ['S', 'N']:
        print("Digite apenas [S] ou [N]")
        continuar = input("Deseja continuar? [S/N]").upper()
    if continuar == 'N':
        break
print(f"{len(geral)} pesosas foram cadastradas")
print(f"O maior peso cadastrado foi: {maior} Kg peso de ", end='')
for p in geral:
    if p[1] == maior:
        print(f"{p[0]} ", end='')
print()
print(f"O menor peso cadastrado foi: {menor} de ", end='')
for p in geral:
    if p[1] == menor:
        print(f"{p[0]} ", end='')


