dados = []
matriz3x3 = []
somapar = somacoluna3 = 0
maiorlinha2 = 0
for c in range(0, 3):
    for d in range(0, 3):
        num = int(input(f'Informe um número para [{c + 1}, {d + 1}]: '))
        dados.append(num)
        if num % 2 == 0:
            somapar += num
    matriz3x3.append(dados[:])
    dados.clear()
print('Matriz 3x3:')
for linha in matriz3x3:
    print(linha)
    if linha[2] > maiorlinha2:
        maiorlinha2 = linha[2]
    somacoluna3 += linha[2]
print(f'A soma dos números pares é: {somapar}')
print(f'A soma dos números da terceira coluna é: {somacoluna3}')
print(f'O maior número da segunda linha é: {maiorlinha2}')