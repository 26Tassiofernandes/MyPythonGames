import random
from time import sleep

lista = [1, 2, 3]
escolhido = random.choice(lista)

print('''Pedra, papel ou tesoura? 
[1]Pedra
[2]Papel
[3]Tesoura''')

opçao = int(input('\033[1;34m>>>Digite sua opção e boa sorte: '))
print('\033[35mPROCESSANDO...')
sleep(1.5)

while opçao < 1 or opçao > 3:
    opçao = int(input('\033[1;31mValor incorreto. Tente novamente: '))
    print('\033[1;33mKapakapa...')
    sleep(1.5)
if escolhido == opçao:
    print('\033[33mEMPATE!\033[m Por coincidência, o computador fez a mesa jogada que você!')

elif opçao != escolhido and opçao == 1 and escolhido == 2:
    print('\033[31mVOCÊ FOI DERROTADO!\033[m Com o papel o computador embrulha sua pedra e ganha a partida kapakapakapa!')

elif opçao != escolhido and opçao == 2 and escolhido == 3:
    print('\033[31mVOCÊ FOI DERROTADO!\033[m Com a tesoura o computador corta seu papel e ganha a partida kapakapakapa!')

elif opçao != escolhido and opçao == 3 and escolhido == 1:
    print('\033[31mVOCÊ FOI DERROTADO!\033[m Com a Pedra o computador esmaga sua tesoura e ganha a partida kapakapakapa!')

elif opçao != escolhido and opçao == 3 and escolhido == 2:
    print('\033[32mVOCÊ VENCEU!\033[m Com a sua tesoura você corta o papel lançado pelo computador e leva a partida!')

elif opçao != escolhido and opçao == 2 and escolhido == 1:
    print('\033[32mVOCÊ VENCEU!\033[m Com o seu papel você embrulha a pedra lançada pelo computador e leva a partida!')

elif opçao != escolhido and opçao == 1 and escolhido == 3:
    print('\033[32mVOCÊ VENCEU!\033[m Com a sua pedra você esmaga a tesoura lançada pelo computador e leva a partida!')
