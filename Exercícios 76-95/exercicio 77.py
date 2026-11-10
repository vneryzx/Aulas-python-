nomes = tuple((input('Digite palavras para verificar as vogais: '))for c in range(1, 5))
for c in range (0,4): 
    print (f"A Palavra {nomes[c]} Possui {nomes[c].lower().count('a')} [A] escritos, {nomes[c].lower().count('e')} [E] escritos, {nomes[c].lower().count('i')} [I] escritos, {nomes[c].lower().count('o')} [O] escritos e {nomes[c].lower().count('u')} [U] escritos")