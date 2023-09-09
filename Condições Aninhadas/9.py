print('''Tabela
Digite 1 para pagamento à vista em dinheiro/cheque
Digite 2 para pagamento à vista no cartão
Digite 3 para pagamento em até 2x no cartão
Digite 4 para pagamento em até 3x no cartão''')


preco_produto = float(input("Digite o valor do produto"))
forma_pag = int(input("Digite o código referente à forma de pagamento"))

if forma_pag == 1:
    print(f"O valor a ser pago será de {preco_produto*0.9} R$")
elif forma_pag == 2:
    print(f"O valor a ser pago será de {preco_produto*0.95} R$")
elif forma_pag == 3:
    print(f"O valor a ser pago será de {preco_produto} R$")
elif forma_pag == 4:
    print(f"O valor a ser pago será de {preco_produto*1.2} R$")

