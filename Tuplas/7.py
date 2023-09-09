produtos = (("Ovo", 10.50),
            ("Maça", 25.00),
            ("Banana", 5.75),
            ("Pera", 15.99),
            ("Torta", 8.49),
            ("Lápis", 12.75),
            ("Copo", 30.00),
            ("Carteira", 7.25),
            ("Caderno", 18.50),
            ("Camisa", 22.99))
print('-'*28)
print('-'*4, 'LISTAGEM DE PREÇOS', '-'*4)
print('-'*28)
for nome, preco in produtos:
    espacos = 30 - len(nome) - len(f"RS {preco:.2f}")
    print(f"{nome}{'.'*espacos}{preco:.2f}")
