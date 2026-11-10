dados = []
parimpar = []
while True:
    num = int(input('Informe um número inteiro: '))
    dados.append(num)
    if num % 2 == 0:
        parimpar.append('Par')
    else:
        parimpar.append('Ímpar')
    per = ' '
    while per not in 'SN':
        per = str(input('Deseja continuar a cadastrar números? [S/N]: ')).strip().upper()[0]
    if per == 'N':
        break
dados.sort()
print(f'Foram cadastrados {len(dados)} números.')
print(f'Os números cadastrados foram: {dados}')
print(f'Os números pares e ímpares foram: {parimpar}')
print('\033[32mFim do programa.\033[m')