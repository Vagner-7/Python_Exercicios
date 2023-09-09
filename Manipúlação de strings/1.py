nome = str(input('Digite seu nome')).strip()
nome_dividido = nome.split()

print(f"Seu nome em letras maíusculas é {nome.strip().upper()}")
print(f"Seu nome em letras minúsculas é {nome.strip().lower()}")
print(f"O número de letras que seu nome possui é {len(nome)- nome.count(' ')}")
print(f"O número de letras do seu primeiro nome é {len(nome_dividido[0])}")
