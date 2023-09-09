reta1 = float(input("Digite a primeira reta"))
reta2 = float(input("Digite a segunda reta"))
reta3 = float(input("Digite a terceira reta"))

if ((reta1 - reta2) < reta3 < reta1+reta2):
    if((reta1-reta3)<reta2<reta1+reta3):
        if((reta2-reta3) < reta1 < reta2 +reta3):
            print("Os valores de segmento de reta formam um triângulo")
if reta1 == reta2 == reta3:
    print("É um triângulo equilátero")
elif reta1 == reta2 or reta1 == reta3 or reta3 == reta1:
    print("É um triângulo isósceles")
elif reta1 != reta2 != reta3:
    print("É um triângulo escaleno")


else:
    print("Os valores de segmento de reta não formam um triângulo")

