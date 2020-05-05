campionato = ('','Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
         'Atlético Mineiro', 'Atlético Paranaense', 'Cruzeiro', 'Botafogo',
          'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense',
           'Ceará', 'Vasco da Gama', 'América Mineiro', 'Sport', 'Vitória',
           'Paraná')
print('=-='*15)           
print('TABELA BRASILEIRAO')
print('=-='*15)
for t in campionato:
    print(f'{t}')  

print('=-='*15)           
print('Classificados para LIBERTADORES DA AMERICA')
print('=-='*15)
for t in range(1, 6):
    print(f'{campionato[t]}')

print('=-='*15)           
print('rebaixados para Segunda divisao')
print('=-='*15)
for t in range(-4, -0):
    print(f'{campionato[t]}')

print('=-='*15)           
print('times em ordem alfabetica')
print('=-='*15)
print(f'{sorted(campionato)}')    
print(f'Chapecoense esta na {campionato.index("Chapecoense")} posição')