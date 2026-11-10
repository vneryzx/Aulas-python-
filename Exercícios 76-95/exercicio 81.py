lista = []
print('-=-'*15)
print('{:^40}'.format('Organizador de listas!'))
print('-=-'*15)
while True:
    n1 = int(input('Digite um numero:'))
    lista.append(n1)
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Se vc quer parar ou continuar digite S/N: ')).upper().strip()[0]
        print(' ')
    if parar == 'N':
        break
print(f'Voce digitou {len(lista)} numeros mano')
print(' ')
print(f'A lista original é: {lista}')
print(' ')
lista.sort()
print(f'A lista em ordem \033[33mcrescente\033[m é: {lista}')
print(' ')
lista.sort(reverse=True)
print(f'A lista em ordem \033[34mdecrescente\033[m é: {lista}')
print(' ')
if 5 in lista:
    print('O numero 5 \033[32mesta\033[m na lista parabens!')
else:
    print('O numero 5 \033[31mnão\033[m esta na lista')
print('-=-'*15)
print('\033[1;36mFIM DO PROGRAMA!\033[m')