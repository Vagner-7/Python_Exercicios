lista = []
continuar = 'S'
while continuar == 'S':
    num = int(input("Digite um valor:"))
    if num not in lista:
        lista.append(num)
        print("Novo valor adicionado!")
        continuar = input("Deseja continuar [S/N]").upper()
    else:
        print("valor já foi adicionado anteriormente, logo não será adicionado!")
        continuar = input("Deseja continuar [S/N]").upper()
print(sorted(lista))
print("FIM")
