campeonato = ('Sport', 'Vasco', 'Botafogo', 'Flamengo', 'Fluminense',
              'Cuiabá', 'Chapecoense', 'Santos', 'Cruzeiro', 'Internacional',
              'Grêmio', 'Goiás', 'América-Mg', 'RB-Bragantino',
              'Coritiba', 'São-Paulo', 'Corinthians', 'Bahia', 'Fortaleza', 'Tufões-VDC')

print(f"Os cinco primeiros colocados são {campeonato[0:5]}")
print(f"Os times rebaixados foram {campeonato[16:20]}")
print(f"Os times em ordem alfabética: {sorted(campeonato)}")
print(f"A Chapecoense se encontra na {campeonato.index('Chapecoense')+1}ª posição do campeonato ")
