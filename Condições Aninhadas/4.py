import datetime
ano_atual = datetime.datetime.now().year

ano_nascimento = int(input("Digite seu ano de nascimento"))
idade = ano_atual - ano_nascimento
falta = 18 - idade
excesso = idade - 18


if idade < 18:
    print(f"Você não possui idade mínima para o alistamento,faltam {falta} anos para seu ano de alistamento")
elif idade > 18:
    print(f"Você ultrapassou {excesso} anos do ano de alistamento")
else:
    print(f"É hora de se alistar!")

