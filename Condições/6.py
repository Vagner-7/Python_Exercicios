numero1 = int(input("Digite o primeiro numero"))
numero2 = int(input("Digite o segundo numero"))
numero3 = int(input("Digite o terceiro numero"))

if numero1 > numero2:
    if numero1 > numero3:
        print(f"O número {numero1} o primeiro número é o maior")
if numero1 < numero2:
    if numero1 < numero3:
        print(f"O número {numero1} o primeiro número é o menor")

if numero2 > numero1:
    if numero2 > numero3:
        print(f"O número {numero2} o segundo número é o maior")
if numero2 < numero1:
    if numero2 < numero3:
        print(f"O número {numero2} o segundo número é o menor")

if numero3 > numero1:
    if numero3 > numero2:
        print(f"O número {numero3} o terceiro número é o maior")
if numero3 < numero1:
    if numero3 < numero2:
        print(f"O número {numero3} o terceiro número é o menor")

