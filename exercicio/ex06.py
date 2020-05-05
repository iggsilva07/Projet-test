listagem = ('lapis', 1.75,
            'borracha', 2, 
            'caderno', 15, 
            'estojo', 25.00,
            'transferidor', 4.20,
            'compasso', 9.90,
            'mochila', 129.32, 
            'canetas', 22.30,
            'livro', 24.90)
print('=-'*20)
print(f'{"Listagem de preços":^38}')
print('=-'*20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'{listagem[pos]:.>7.2f}')    
print('=-'*20)