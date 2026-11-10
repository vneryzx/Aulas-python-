lista = []
while True:
    num = int(input('Digite um numero ai:'))
    if num not in lista:
        lista.append(num)
    else:
        print('Numero repitido')
    acabar = ' '
    while acabar not in 'SN':
        acabar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if acabar == 'N':
        break
lista.sort()
print(f'OS numeros digitados em ordem crescente foram: {lista}')
print('FIM DO JOGO')