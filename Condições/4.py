distancia = int(input("Digite a distância percorrida em Km"))
taxa_a = distancia * 0.5
taxa_b = distancia * 0.45

if distancia <= 200:
    print(f"O valor da passagem é {taxa_a} R$")
else:
    print(f"o valor da passagem é {taxa_b} R$")