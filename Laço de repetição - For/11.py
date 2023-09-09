soma_idade = 0
maior_idade = 0
c = 0
nomevelho = ''

for i in range(1, 6):
    print(f"------- {i}a PESSOA -------")
    nome = str(input("Digite o nome:")).strip()
    idade = int(input("Digite a idade:"))
    sexo = str(input("Digite o sexo [M/F]")).upper().strip()
    soma_idade += idade
    if sexo == "M" and idade > maior_idade:
        maior_idade = idade
        nomevelho = nome
    if i == 1 and sexo == 'M':
        maior_idade = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        c += 1

print(f"A média de idade desse grupo é {soma_idade/5}")
print(f"O homem mais velho se chama {nomevelho} e possui {maior_idade} anos")
print(f"O número de mulheres com menos de 20 anos é {c}")