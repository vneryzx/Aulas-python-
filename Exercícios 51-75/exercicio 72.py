cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('\033[31mTente novamente.\033[m ' , end='')
print(f'Vc digitou o numero \033[33m{cont[num]}\033[m!')