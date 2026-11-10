dados = []
alunos = []
n = 0

print('='*30)

while True:
    dados = [input('Nome: '),
             float(input('Nota 1: ')),
             float(input('nota 2: '))]
    alunos.append(dados[:])
    dados.clear()

   #continuar ou nao
    continuar = ''
    while True:
        continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break

print('='*30)
print(f'{"No.":<8}{"Nome.":<12} Media')
for c, f in enumerate(alunos):
    media = (alunos[c][1] + alunos[c][2]) / 2
    print(f'{c:<7} {alunos[c][0]:<11} {media}', end= '  ')
    print('')

while n != 999:
    n = int(input('Deseja ver a nota de qual aluno[999 pra sair]?'))
    if n == 999:
        break
    elif n in range(0, len(alunos)):
        print(f'As notas de {alunos[n][0]} foram: [{alunos[n][1]}, {alunos[n][2]}]')
    else:
        print(f'ERRO: Aluno No. {n} nao EXISTE.')