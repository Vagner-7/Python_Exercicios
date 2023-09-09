# = list()
#lista.append('Gustavo')
#lista.append(40)
#galera = list()
#galera.append(lista[:])
#lista[0] = 'Maria'
#lista[1] = 22
#galera.append(lista[:])
#print(galera)

#x = [['Joao',20], ['Ana', 24], ['Pedro', 22], ['Carlos', 24]]
#for p in x:
#    print(f"{p[0]} tem {p[1]} anos de idade")

maior = 0
menor = 0
geral = []
dado = []
for c in range(0, 3):
    dado.append(input("Nome: "))
    dado.append(int(input("Idade: ")))
    geral.append(dado[:])
    dado.clear()
for p in geral:
    if p[1] >= 18:
        maior += 1
        print('maior de idade')
    else:
        menor +=1
        print('menor de idade')
print(f"Temos {maior} maiores de idade e {menor} menores de idade")
