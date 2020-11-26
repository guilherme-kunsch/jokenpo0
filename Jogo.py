from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')

sentinela = True
while (sentinela == True):

    computador = randint(0, 2)

    print('''Suas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')

    jogador = int(input('Qual sua jogada? '))

    if jogador >= 0 and jogador <= 2:
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO')
        sleep(1)
        print('-=' * 15)
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))

        if jogador == 0:  # PC jogou pedra
            if computador == 0:
                print('EMPATE')
            elif computador == 1:
                print('COMPUTADOR GANHOU')
            elif computador == 2:
                print('JOGADOR GANHOU')
        elif jogador == 1:
            if computador == 0:
                print('JOGADOR GANHOU')
            elif computador == 1:
                print('EMPATE')
            elif computador == 2:
                print('COMPUTADOR GANHOU')
        elif jogador == 2:
            if computador == 0:
                print('COMPUTADOR GANHOU')
            elif computador == 1:
                print('JOGADOR PERDEU')
            elif computador == 2:
                print('EMPATE')
    else:
        print('Jogada inválida, tente novamente!')

    rodar = int(input('''Quer continuar jogando?
     [0] NÃO
     [1] SIM\n '''))

    if rodar != 1:
        sentinela = False

