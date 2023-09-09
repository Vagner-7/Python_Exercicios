from random import randint
c = 0

while True:
    jogada = int(input("Digite sua jogada"))
    computador = randint(0, 10)
    total = jogada + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar [P/I]')).upper()
    print(f"Voce jogou {jogada} e o computador jogou {computador}. Resultando em {total}")
    if tipo == 'P':
        if total % 2 == 0:
            print("Você venceu!")
            c += 1
        else:
            print("Você perdeu!")
            break
    if tipo == 'I':
        if total % 2 == 1:
            print("Você venceu!")
            c += 1
        else:
            print("Você perdeu!")
            break
    print("Play again")

print(f"O número de vezes que voce ganhou foi {c}")
