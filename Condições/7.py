salario = int(input("Digite o valor do salário"))

aumento_a = salario * 1.1
aumento_b = salario * 1.15

if salario > 1250:
    print(f"O aumento será de 10%, resultando em {aumento_a:.2f} R$ como novo salário")
else:
    print(f"O aumento será de 15%, resultando em {aumento_b:.2f} R$ como novo salário")
