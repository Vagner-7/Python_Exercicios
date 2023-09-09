nome_cidade = str(input('Digite o nome da sua cidade'))
primeiro_nome = nome_cidade.strip().split()[0]

if primeiro_nome == 'SANTO':
    print('Começa com SANTO')
else:
    print('Não começa com Santo')
