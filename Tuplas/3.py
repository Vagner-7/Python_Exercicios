extenso = ('Zero', 'Um', 'Dois', 'Três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'Catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = 'S'
while continuar == 'S':
    a = int(input("Digite o número que voce quer ver por extenso entre 0 a 20"))
    if 0 <= a <= 20:
        print(f"Voce digitou o número {extenso[a]}")
        continuar = input("Deseja continuar?[S/N]").upper()
    else:
        print("Número fora do intervalo, tente novamente")
print("Fim do programa!")



