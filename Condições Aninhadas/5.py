nota1 = int(input("Digite a primeira nota"))
nota2 = int(input("Digite a segunda nota"))

media = (nota1 + nota2)/2

if media < 5:
    print(f"Reprovado")
elif 5.0 >= media <= 6.9:
    print(f"Recuperação")
elif media >= 7:
    print(f"Aprovado")