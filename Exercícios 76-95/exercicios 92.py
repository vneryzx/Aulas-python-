trabalhador = {'nome': str(input('Nome: ')), 'ano_nascimento': int(input('Ano de nascimento: ')), 'ctps': int(input('Carteira de trabalho (0 não tem): '))}
if trabalhador['ctps'] != 0:
    trabalhador['ano_contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['idade'] = 2026 - trabalhador['ano_nascimento']
    trabalhador['aposentadoria'] = trabalhador['idade'] + (trabalhador['ano_contratacao'] + 35 - 2026)
    print(f'O trabalhador {trabalhador["nome"]} tem {trabalhador["idade"]} anos, foi contratado em {trabalhador["ano_contratacao"]} e receberá R${trabalhador["salario"]:.2f} de salário. Ele se aposentará aos {trabalhador["aposentadoria"]} anos.')
else:
    trabalhador['idade'] = 2026 - trabalhador['ano_nascimento']
    print(f'O trabalhador {trabalhador["nome"]} tem {trabalhador["idade"]} anos e não possui carteira de trabalho.')