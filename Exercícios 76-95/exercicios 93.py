aprovfut = {}
aprovfut['Nome'] = input(str('Nome do jogador: ')).strip().capitalize()
aprovfut['partidas'] = int(input(f'Quantas partidas {aprovfut["Nome"]} jogou? '))
aprovfut['gols'] = []
for i in range(aprovfut['partidas']):
    gols = int(input(f'Quantos gols na partida {i + 1}? '))
    aprovfut['gols'].append(gols)
aprovfut['total'] = sum(aprovfut['gols'])
print('-=' * 30)
print(aprovfut)
print('-=' * 30)
for k, v in aprovfut.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {aprovfut["Nome"]} jogou {aprovfut["partidas"]} partidas.')
for i in range(aprovfut['partidas']):
    print(f'    => Na partida {i + 1}, fez {aprovfut["gols"][i]} gols.')
print(f'Foi um total de {aprovfut["total"]} gols.')