itens = ('lápis','borracha','caderno','estojo','transferidor','compasso','mochila','caneta','livro')
valores = (1.75,2,15.90,25,4.20,9.99,120.32,22.30,34.90)
print('-'*46)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*46)
# a variavel a esquerda, representa os indices, a direita a posição do contador
for pos,c in enumerate(itens and valores):
    print(f'{itens[pos]:.<35}R$ {valores[pos]:>7.2f}|'.title())
print('-'*46)
n = str(input('Voce quer comprar algo S ou N:')).strip().upper()[0]
if n == 'S':
    print('fodasekkkk')
else:
    print('tchau')