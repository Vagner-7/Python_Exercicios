# Super matemático 
numero_um = int(input("Digita o primeiro valor aí"))
numero_dois = int(input("Digita o segundo valor aí"))
numero = 0

while numero != 5:
    numero = int(input(
        "Escolha sua opção:\n"
        "[1] Somar\n"
        "[2] Multiplicar\n"
        "[3] Maior\n"
        "[4] Novos números\n"
        "[5] Sair do programa"))

    if numero == 1:
        print(f"A soma entre os valores é: {numero_um + numero_dois}")
    elif numero == 2:
        print(f"O produto dos valores é: {numero_um * numero_dois}")
    elif numero == 3:
        if numero_um > numero_dois:
            print(f"O {numero_um} (primeiro número) é o maior!")
        elif numero_um == numero_dois:
            print(f"Os números em análise são iguais!")
        else:
            print(f"O {numero_dois} (segundo número) é o maior!")
    elif numero == 4:
        numero_um = int(input("Digita o primeiro valor aí"))
        numero_dois = int(input("Digita o segundo valor aí"))
    elif numero == 5:
        print("Chega fi, cabou a graça")
    else:
        print("Opção inválida. Tenta dnv aí.")
print("Chega fi, cabou a graça")
