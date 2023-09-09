geral = []

while True:
    nome = input("Nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2)/2
    geral.append([nome, [nota1, nota2], media])
    continuar = input("Deseja continuar? [S/N]").upper()
    while continuar not in ["S", "N"]:
        print("Digite apenas [S/N]!")
        continuar = input("Deseja continuar? [S/N]").upper()
    if continuar == "N":
        break
for i, n in enumerate(geral):
    print(f"{i} - A média de {n[0]} é {n[2]}")
while True:
    opc = int(input("Mostrar a nota de qual aluno? (999 interrompe)"))
    if opc == 999:
        print("FIM")
        break
    if opc <= len(geral)-1:
        print(f"As notas de {geral[opc][0]} são {geral[opc][1]}")



