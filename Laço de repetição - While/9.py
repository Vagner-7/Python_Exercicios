import random
numero_maquina = random.randint(0, 10)
numero_jogador = int(input("Tente sua sorte, digite um número de 0 a 10!"))
tentativas = 0


while numero_jogador != numero_maquina:
    numero_jogador = int(input("Errooou, tenta dnv fi"))
    tentativas += 1
if numero_jogador == numero_maquina:
    tentativas += 1
    print(f"Você acertou")
if tentativas > 0:
    print(f"Tentou {tentativas} vezes, melhora aí fi")


