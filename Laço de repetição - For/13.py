um = 0
dois = 0
tres = 0
quatro = 0
cinco = 0
seis = 0

for num in range(20):
    numero = int(input())
    if numero == 1:
        um += 1
    elif numero == 2:
        dois += 1
    elif numero == 3:
        tres += 1
    elif numero == 4:
        quatro += 1
    elif numero == 5:
        cinco += 1
    elif numero == 6:
        seis += 1

print(f"O número 1 saiu {um} vezes.")
print(f"O número 2 saiu {dois} vezes.")
print(f"O número 3 saiu {tres} vezes.")
print(f"O número 4 saiu {quatro} vezes.")
print(f"O número 5 saiu {cinco} vezes.")
print(f"O número 6 saiu {seis} vezes.")
