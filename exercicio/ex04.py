from random import randint
from time import sleep
numeros = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)
print('sorteando...')
sleep(1)
for num in numeros:
    print(f'{num}', end=' ')
print()
print(f'maior valor foi {max(numeros)}')
print(f'menor valor foi {min(numeros)}')
