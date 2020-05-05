#testando repositorio no git -- alteração
num = (int(input('Digite um numero inteiro: ')),
       int(input('Digite outro numero inteiro: ')),
        int(input('Digite mais um numero inteiro: ')),
        int(input('Digite o ultimo numero inteiro: ')))
print(f'voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes ')
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3)+1} posição')
else:
    print('O valor 3 nao foi digitado')
for n in num:
    if n % 2 == 0:
        print('Os numeros pares sao: {} '.format(n) , end=' ')
