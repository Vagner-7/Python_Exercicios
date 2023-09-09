numero = int(input("Digite um número: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

contador = inicio

while contador <= fim:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1