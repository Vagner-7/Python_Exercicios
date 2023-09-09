from random import randint
computador = randint(0, 5)
numero = int(input("Digite um número"))

if numero == computador:
    print("você acertou o número")
else:
    print("ERROOOOOOOU")