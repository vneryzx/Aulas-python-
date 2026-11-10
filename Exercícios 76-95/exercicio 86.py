dados = []
matriz3x3 = []
for c in range(0, 3):
    for d in range(0, 3):
        num = int(input(f'Informe um número para [{c + 1}, {d + 1}]: '))
        dados.append(num)
    matriz3x3.append(dados[:])
    dados.clear()
print('Matriz 3x3:')
for linha in matriz3x3:
    print(linha)
