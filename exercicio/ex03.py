campionato = ('','Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
         'Atlético Mineiro', 'Atlético Paranaense', 'Cruzeiro', 'Botafogo',
          'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense',
           'Ceará', 'Vasco da Gama', 'América Mineiro', 'Sport', 'Vitória',
           'Paraná')
print('\nTABELA BRASILEIRAO')
for posicao_times in range(1, 21):
        print(f'{posicao_times} - {campionato[posicao_times]}')
        
print('\nClassificados para a LIBERTADORES DA AMERICA!') 
for posicao_times in range(1,6):
    print(f'{posicao_times} - {campionato[posicao_times]}') 

print('\nOs rebaixados para segunda divisão!') 
for posicao_times in range(17,21):
      print(f'{posicao_times} - {campionato[posicao_times]}')




