pessoas = {"nome": "gustavo", "sexo": "M", "Idade": 22}
pessoas["Peso"] = 90
print(f"{pessoas['nome']} tem {pessoas['Idade']} anos")
print(pessoas.items())
for k, v in pessoas.items():
    print(f"{k} = {v}")
