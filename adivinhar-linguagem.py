import requests
import random

# Importando uma API
url = "https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json"
resposta = requests.get(url)
data = resposta.json()

# Biblioteca Random escolhe um indice aleatório
valor_secreto = random.choice(data)
linguagem_secreta = valor_secreto['palavra']
dica = valor_secreto['dica']

print('-----------  Jogo de adivinhação  ----------- \n' )
menu = '''
escolha um tipo de dica:
[a] quantidade de letras
[b] função da linguagem
[c] todas
'''
escolha = input(f'{menu}Digite sua opção: ')
print('\n--------------------------------------------')

if escolha == 'a':
    print(f'A linguagem tem: {len(linguagem_secreta)} letras.')
elif escolha == 'b':
    print(f'A função da linguagem é: {dica}.')
else:
    print(f'A linguagem tem: {len(linguagem_secreta)} letras. \nFunção: {dica}')


while True :
    print('\n--------------------------------------------')
    chute = str(input('Digite a linguagem: ').lower())
    if linguagem_secreta == chute:
        print(f'Acertou!! A linguagem era {linguagem_secreta}')
        break
    else:
        print('Hmm... você errou.')