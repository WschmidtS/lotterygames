import random
import numpy

print('Gerando números aleatórios para Loteria')
low = int(input('Digite o menor número do intervalo:'))
high = int(input('Digite o maior númerodo intervalo:'))
size = int(input('Digite a quantidade de números para o jogo:'))
amount = int(input('Digite a quantidade de jogos:'))

for i in range(amount):
    lotterygames = random.sample(range(low, high+1), size)
    i += 1
    print(f'Jogo{i}:{lotterygames}')
