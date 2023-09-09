numero = int(input("Digite o numero a ser convertido"))
opcão = int(input("Digite 1 para binário, 2 para octal e 3 para hexadecimal"))

if opcão == 1:
    print(f"O número convertido em questão é {numero, bin(numero)}")
elif opcão == 2:
    print(f"O número convertido em questão é {numero, oct(numero)}")
elif opcão == 3:
    print(f"O número convertido em questão é {numero, hex(numero)}")
else:
    print(f"O número digitado não está na base de dados para conversão")