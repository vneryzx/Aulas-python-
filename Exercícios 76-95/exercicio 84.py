dados = []
pessoa = []
maior = menor = c = 0
p_pe = []
p_le = []
while True:
    print('-' * 30)
    nome = str(input('Informe seu Nome: '))
    peso = int(input('Informe seu Peso em [Kg]: '))
    c += 1
    dados = [nome, peso]
    pessoa.append(dados[:])
    if c == 1:
        maior = menor = peso
        print('\033[32mPrimeiro cadastro! Peso definido como maior e menor.\033[m')
        print('-' * 30)
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    per = ' '
    while per not in 'SN':
        per = str(input('Deseja continuar a cadastrar pessoas? [S/N]: ')).strip().upper()[0]
    if per == 'N':
        break
print('-' * 30)
print(f'Foram feito {len(pessoa)} cadastros.')
for gente in pessoa:
    if maior == gente[1]:
        p_pe.append(gente[0])
    if menor == gente[1]:
        p_le.append(gente[0])
print(f'O maior peso foi de {maior} kg. Peso de {p_pe}')
print(f'O menor peso foi de {menor} kg. Peso de {p_le}')
print('-' * 30)
print('Fim do programa.')