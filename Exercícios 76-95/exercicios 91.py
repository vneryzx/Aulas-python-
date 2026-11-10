import random
jogadores = {'jogador1': random.randint(1, 6), 'jogador2': random.randint(1, 6), 'jogador3': random.randint(1, 6), 'jogador4': random.randint(1, 6)}
print('Valores sorteados:')
for jogador, valor in jogadores.items():
    print(f'{jogador} tirou {valor}')
    ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
print('Ranking dos jogadores:')
for i, (jogador, valor) in enumerate(ranking, start=1):
    print(f'{i}º lugar: {jogador} com {valor}')
