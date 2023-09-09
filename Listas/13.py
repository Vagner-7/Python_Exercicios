import random
import time
geral = []
num_jogos = int(input("Quantos jogos voce quer que a máquina sorteie?"))
for n in range(num_jogos):
    valor = random.sample(range(1, 60), 6)
    if valor not in geral:
        geral.append(valor)
    else:
        print("Combinação já cadastrada!")
for n, j in enumerate(geral, start=1):
    print(f"Jogo {n}: {sorted(j)}")
    time.sleep(0.3)
    if n < num_jogos:
        print("Sorteando...")
        time.sleep(2)
print("FIM")
