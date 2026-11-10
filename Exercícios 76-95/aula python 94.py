grupopessoas = {}
grupopessoas['pessoas'] = []
grupopessoas['media'] = 0
while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ').strip().capitalize()
    pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    grupopessoas['pessoas'].append(pessoa)
    grupopessoas['media'] += pessoa['idade']
    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
grupopessoas['media'] /= len(grupopessoas['pessoas'])
print('-=' * 30)
print(f'A) Ao todo temos {len(grupopessoas["pessoas"])} pessoas cadastradas.')
print(f'B) A média de idade é de {grupopessoas["media"]:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for pessoa in grupopessoas['pessoas']:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for pessoa in grupopessoas['pessoas']:
    if pessoa['idade'] > grupopessoas['media']:
        print(f'    nome = {pessoa["nome"]}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]};')