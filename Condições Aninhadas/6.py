import datetime
ano_atual = datetime.datetime.now().year

ano_nascimento = int(input("Digite o ano de nascimento"))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print("Categoria Mirim")
elif idade <= 14:
    print("Categoria Infantil")
elif idade <= 19:
    print("Categoria Junior")
elif idade <= 20:
    print("Categoria Sênior")
elif idade > 20:
    print("Categoria Master")