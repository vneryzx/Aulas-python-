import random
while True:
    megasena = random.sample(range(1, 61), 6)
    megasena.sort()
    print(f'Jogo da Mega-Sena: {megasena}')
    per = ' '
    while per not in 'SN':
        per = str(input('Deseja gerar outro jogo? [S/N]: ')).strip().upper()[0]
    if per == 'N':
        break
print('Fim do programa.')