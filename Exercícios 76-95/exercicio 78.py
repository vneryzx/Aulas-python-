lista = []
for indice in range(1, 6):
    n = int(input(f'Digite um valor na {indice}ª posição: '))
    lista.append(n)
print(f'Você digitou os valores \033[31m{lista}\033[m')
print(f'O maior valor digitado foi \033[31m{max(lista)}\033[m na posição ', end='')
for indice, valor in enumerate(lista):
    if valor == max(lista):
        print(f'\033[31m{indice + 1}', end='ª\033[m, ')
print(f'\nO menor valor digitado foi \033[31m{min(lista)}\033[m na posição ', end='')
for indice, valor in enumerate(lista):
    if valor == min(lista):
        print(f'\033[31m{indice + 1}', end='ª\033[m, ')