valor_da_casa = int(input("Digite o valor da casa"))
salario = int(input("Digite o seu salário"))
anos = int(input("Digite em quantos anos será parcelado"))

prest_mensal = (valor_da_casa/(anos*12))


if prest_mensal <= (salario * 0.3):
    print(f"O valor das prestações mensais é: {prest_mensal:.2f} R$")
else:
    print(f"O valor excede 30% do seu salário")