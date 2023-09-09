primeiro_numero = int(input("Digite o primeiro número"))
segundo_numero = int(input("Digite o segundo número"))

if primeiro_numero > segundo_numero:
    print(f"O primeiro valor é o maior!")
elif primeiro_numero == segundo_numero:
    print(f"Não existe valor maior, os dois são iguais!")
else:
    print(f"O segundo valor é o maior!")