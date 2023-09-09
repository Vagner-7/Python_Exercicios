lista = []
par = []
impar = []
while True:
    lista.append(int(input("Digite um valor")))
    continuar = input("Deseja continuar? [S/N]").upper()
    while continuar not in ['S', 'N']:
        print("Digite apenas [S] ou [N]!")
        continuar = input("Deseja continuar? [S/N]").upper()
    if continuar == "N":
        break

for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f"Os valores pares são: {sorted(par)}")
print(f"Os valores ímpares são: {sorted(impar)}")
print(f"A lista completa tem os valores: {sorted(lista)}")
