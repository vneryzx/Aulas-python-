n = []
for c in range(5):
    valor = int(input('Informe um número: '))
    if c == 0:
        n.append(valor)
        print(f'Adicionado na posição {c + 1} da lista')
    else:
        foi_inserido = False
        for pos, numeros in enumerate(n):
            if valor < numeros:
                n.insert(pos, valor)
                print(f'Adicionado na posição {pos + 1 } da lista')
                foi_inserido = True
                break
        if not foi_inserido:
            n.append(valor)
            print(f'Adicionado no final da lista')
print('-=-' * 20)
print(f'Os números informados foram: {n}')