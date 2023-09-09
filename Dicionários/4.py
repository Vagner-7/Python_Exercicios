estado = {}
brasil = []
for c in range(0, 3):
    estado["uf"] = input("Unidade Federativa: ")
    estado["sigla"] = input("Sigla do estado: ")
    brasil.append(estado.copy())
for e in brasil:
    for x, y in e.items():
        print(f"O campo {x} tem valor  {y}")

