aluno = {}
aluno['Nome'] = input(str('Nome do aluno: ')).strip().capitalize()
n1 = float(input(f'Nota 1 do {aluno["Nome"]}: '))
n2 = float(input(f'Nota 2 do {aluno["Nome"]}: '))
aluno['Média'] = (n1 + n2) / 2
if aluno['Média'] >= 6:
    aluno['Situacao'] = '\033[32mAprovado\033[0m'
else:
    aluno['Situacao'] = '\033[31mReprovado\033[0m'
print(f'O aluno {aluno["Nome"]} tem média {aluno["Média"]} e está {aluno["Situacao"]}')