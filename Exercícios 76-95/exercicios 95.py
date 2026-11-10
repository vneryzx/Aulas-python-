aprovjogador = {}
grupojogador = []
while True:
    jogador = {}
    jogador['nome'] = input('Nome do jogador: ').strip().capitalize()
    jogador['gols'] = []
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(partidas):
        gols = int(input(f'Quantos gols na partida {i + 1}? '))
        jogador['gols'].append(gols)
    jogador['total'] = sum(jogador['gols'])
    grupojogador.append(jogador)
    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":<5}')
print('-' * 40)
for i, jogador in enumerate(grupojogador):
    print(f'{i:<4}{jogador["nome"]:<15}{str(jogador["gols"]):<15}{jogador["total"]:<5}')   