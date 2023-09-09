frase = str(input()).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print(f" As palavras {junto} e {inverso} formam um palíndromo")
else:
    print(f"Não é palíndromo")