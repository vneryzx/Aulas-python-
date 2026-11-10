lista = []
par = []
impar = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'A lista original é: \n{lista}')
print(f'A lista que tem somente numero par é: \n{par}')
print(f'A lista que tem somente numero impar é: \n{impar}')
