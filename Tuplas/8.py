palavras = ("carro", "bicicleta", "computador", "janela", "telefone",
            "gato", "cachorro", "livro", "mesa", "caneta",
            "chave", "porta", "sapato", "chocolate", "banana",
            "piano", "quadro", "flor", "mochila", "relógio")
for nome in palavras:
    print(f"\nNa palavra {nome.upper()} temos: ", end='')
    for vogais in nome:
        if vogais in nome:
            if vogais.lower() in 'aeiou':
                print(vogais, end=" ")