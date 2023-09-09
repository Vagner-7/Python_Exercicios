num = [2, 5, 9, 1, 3]
num.insert(2, 12)
num.append(8)
num.pop() #remove o ultimo elemento da lista por padrao, porem pode escolher o indice a ser removido
num.pop(1) #remove o elemento de indice 1
num.remove(1) #remove o primeiro valor 1 da lista, caso nao possua o valor na lista ocorrerá um erro
print(sorted(num))
