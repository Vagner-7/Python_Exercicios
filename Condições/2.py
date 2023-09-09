velocidade = int(input("Digite a velocidade"))
km_max = 80
multa = (velocidade - km_max) * 7

if velocidade > km_max:
    print(f"voce deverá pagar uma multa de {multa}")
else:
    print("OK, você respeita as leis de trãnsito")