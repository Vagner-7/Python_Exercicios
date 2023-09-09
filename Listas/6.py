lista = []
while True:
    lista.append(int(input("Digite um valor")))
    continuar = input("Deseja continuar? [S/N]").upper()
    while continuar not in ['S', 'N']:
        print("Digite apenas [S] ou [N]!")
        continuar = input("Deseja continuar? [S/N]").upper()
    if continuar == 'N':
        break
print(f"A quantidade de números que foram digitados é: {len(lista)}")
lista_desc = sorted(lista, reverse=True)
print(f"A lista de forma decrescente é: {lista_desc}")
if 5 not in lista:
    print("O número 5 não está presente na lista!")
else:
    print("O número 5 está na lista!")

