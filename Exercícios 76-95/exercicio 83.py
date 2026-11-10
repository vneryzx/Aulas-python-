entrada = input('Digite a expressão a ser analisada: ')
parentese_abrir = parentese_fechar = 0

for i, v in enumerate(entrada):
    if v == '(':
        parentese_abrir += 1
        parentese_fechar -= 1
    if v == ')':
        parentese_fechar += 1
        parentese_abrir -= 1
    if parentese_fechar > parentese_abrir:
        print(f'Há algum erro na ordem dos parênteses na posição {i + 1}')
        break
if parentese_abrir == parentese_fechar:
    print('Expressão correta!')
else:
    print('Há algum erro na quantidade de parênteses.')