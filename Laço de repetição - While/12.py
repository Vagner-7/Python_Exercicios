# PA com While
primeiro = int(input())
razao = int(input())
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} > ", end='')
        termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos voce quer mostrar a mais?"))
print(f"Fim com um total de {total} de termos")
