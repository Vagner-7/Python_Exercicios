dados = {"Nome": "Pedro", "Idade": 25}
dados["sexo"] = "M" #Novo elemento
# remove um elemento  del dados["Idade"]
print(dados["Nome"])
print(dados)
#print(dados.values()) > Retorna os valores ex: 'Pedro', 25, 'M'
#print(dados.keys()) > Retorna as chaves ex: 'Nome', 'Idade', 'Sexo''
#print(dados.items()) > Retorna os valores e as chaves
for x, y in dados.items():
    print(f"O {x} é {y}")