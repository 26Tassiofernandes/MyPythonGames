from time import sleep
import random
from pygame import mixer

# Número máximo de tentativas por jogada
tent = 7 


# Lista de esportes escolhidos
sports = ['ATLETISMO', 'BASQUETE', 'BOXE', 'CANOAGEM', 'CICLISMO', 'ESGRIMA', 'FUTEBOL', 'GINASTICA', 'GOLFE',
          'HANDEBOL', 'JUDO', 'NATAÇAO', 'REMO', 'SKATE', 'SURFE', 'TAEKWONDO', 'TENISDEMESA', 'VOLEI']

# Sorteio de um esporte aleatório da lista
sort_sports = random.choice(sports)

# Lista de planetas escolhidos
planets = ['MERCURIO', 'VENUS', 'TERRA', 'MARTE', 'JUPITER', 'SATURNO', 'URANO', 'NETUNO']

# Sorteio de um planeta aleatório da lista
sort_planets = random.choice(planets)

# Lista de cores escolhidas
cores = ['AZUL', 'VERMELHO', 'ROSA', 'AMARELO', 'PRETO', 'VERDE', 'CINZA', 'MARROM', 'ROXO', 'LARANJA', 'VIOLETA',
         'BRANCO']

# Sorteio de uma cor aleatória da lista
sort_cores = random.choice(cores)


# Lista de super heróis escolhidos
heroes = ['CAPITAOAMERICA', 'MULHERMARAVILHA', 'HOMEMARANHA', 'HOMEMDEFERRO', 'HULK', 'BATMAN',
          'SUPERMAN', 'LANTERNAVERDE', 'DEADPOOL', 'SHAZAN', 'AQUAMAN', 'THOR', 'VIUVANEGRA', 'WOLVERINE',
          'GAVIAOARQUEIRO', 'FLASH', 'PANTERANEGRA', 'SUPERGIRL']

# Sorteio de um héroi aleatório da lista
sort_heroes = random.choice(heroes)

print('=-' * 15)
print('\033[1;7;40mBEM VINDO AO JOGO DA ADIVINHAÇÃO \033[m')
print('=-' * 15)
start = str(input('\033[1;7;40mDigite start para jogar ou f para sair:\033[m ')).upper().strip()

while start != 'START' and start != 'F':
    start = str(input('\033[1;7;40mDigite start para jogar ou f para sair:\033[m ')).upper().strip()

if start == 'START':
    mixer.init()
    mixer.music.load('Sparkman(MP3_320K).mp3')
    mixer.music.play()
    print('\033[1mVamos começar...')
    sleep(2)

    print('=-' * 15)
    print('''Escolha um tema abaixo:
[1]Esportes olímpicos
[2]Planetas
[3]Cores comuns
[4]Super-heróis''')
    print('=-' * 15)

    tema = int(input('\033[1;34m>>>Digite seu tema e boa sorte: \033[m'))
    print('PROCESSANDO...')
    sleep(1.5)
    while tema < 1 or tema > 4:
        tema = int(input('\033[1;34m>>>Digite seu tema e boa sorte: \033[m'))
        print('PROCESSANDO...')
        sleep(1.5)

    if tema == 1:
        print(f'Você escolheu a temática \033[4mESPORTES\033[m, ao todo temos {len(sports)} esportes em nossa lista...')
        sleep(1.5)
        esporte = str(input(
            f'\033[1mDigite um esporte olímpico com {len(sort_sports.strip())} letras (sem espaços e acentos): ')).upper().strip()

        while esporte != sort_sports:
            esporte = str(input('\033[1;4;31mResposta incorreta. Tente novamente: \033[m')).upper().strip()
            tent = tent - 1
            
            if tent == 0:
                print('\033[1;31mGame Over!\033[m')
                print(f'\033[1;32mA resposta correta era \033[1;4;35m{sort_sports}!\033[m')
                break

            if tent == 3:
                perg = str(input('\033[1mDeseja uma dica?[S/N]: ')).upper().strip()
                while perg != 'S' and perg != 'N':
                    perg = str(input('Deseja uma dica?[S/N]: \033[m')).upper().strip()
                if perg == 'S':
                    esporte = str(input(f'\033[1;4;32mO esporte olímpico começa com a letra {sort_sports.strip()[0]}: \033[m')).upper().strip()
                if perg == 'N':
                    esporte = str(input('\033[1;36mQual é o esporte olímpico? \033[m'))

        if esporte == sort_sports:
            print(f'\033[1;35mParabéns. O esporte olímpico é \033[1;4;32m{esporte}.\033[m')

    if tema == 2:
        print(f'Você escolheu a temática \033[4mPLANETAS\033[m, ao todo temos {len(planets)} planetas na lista...')
        sleep(1.5)
        planeta = str(input(f'\033[1mDigite um planeta com {len(sort_planets.strip())} letras (sem espaços e acentos): \033[m')).upper()

        while planeta != sort_planets:
            planeta = str(input('\033[1;4;31mResposta incorreta. Tente novamente: \033[m')).upper().strip()
            tent = tent - 1
            print(f'\033[1;4mVocê tem {tent} tentativas\033[m')
            if tent == 0:
                print('\033[1;31mGame Over!\033[m')
                print(f'\033[1;32mA resposta correta era \033[1;4;35m{sort_planets}!\033[m')
                break

            if tent == 3:
                perg = str(input('\033[1mDeseja uma dica?[S/N]: ')).upper().strip()
                while perg != 'S' and perg != 'N':
                    perg = str(input('Deseja uma dica?[S/N]: \033[m')).upper().strip()
                if perg == 'S':
                    planeta = str(input(f'\033[1;4;32mO planeta começa com a letra {sort_planets.strip()[0]}: \033[m')).upper().strip()
                if perg == 'N':
                    planeta = str(input('\033[1;36mQual é o planeta? \033[m'))

        if planeta == sort_planets:
            print(f'\033[1;35mParabéns. O Planeta escolhido é \033[1;4;32m{planeta}.\033[m')

    if tema == 3:
        print(f'Você escolheu a temática \033[4mCORES COMUNS\033[m, ao todo temos {len(cores)} cores em nossa lista...')
        sleep(1.5)
        cor = str(input(f'\033[1mDigite uma cor comum com {len(sort_cores.strip())} letras (sem espaços e acentos): \033[m')).upper().strip()

        while cor != sort_cores:
            cor = str(input('\033[1;4;31mResposta incorreta. Tente novamente: \033[m')).upper().strip()
            tent -= 1
            print(f'\033[1;4mVocê tem {tent} tentativas\033[m')

            if tent == 3:
                perg = str(input('\033[1mDeseja uma dica?[S/N]: ')).upper().strip()
                while perg != 'S' and perg != 'N':
                    perg = str(input('Deseja uma dica?[S/N]: \033[m')).upper().strip()
                if perg == 'S':
                    cor = str(input(f'\033[1;4;32mA cor comum começa começa com a letra {sort_cores.strip()[0]}: \033[m')).upper().strip()
                if perg == 'N':
                    cor = str(input('\033[1;36mDigite a cor: \033[m')).strip().upper()

            if tent == 0:
                print('\033[1;31mGame Over!\033[m')
                print(f'\033[1;32mA resposta correta era \033[1;4;35m{sort_cores}!\033[m')
                break

        if cor == sort_cores:
            print(f'\033[1;35mParabéns pela adivinhação. A cor escolhida é \033[1;4;32m{cor}!\033[m')

    if tema == 4:
        print(f'Você escolheu a temática \033[4mSUPER HERÓIS\033[m, ao todo temos {len(heroes)} super heróis na lista...')
        sleep(1.5)
        heroi = str(input(f'\033[1mDigite um super herói com {len(sort_heroes.strip())} letras (sem espaços e acentos): \033[m')).upper().strip()

        while heroi != sort_heroes:
            heroi = str(input('\033[1;4;31mResposta incorreta. Tente novamente: \033[m')).upper().strip()
            tent = tent - 1
            print(f'\033[1;4mVocê tem {tent} tentativas\033[m')

            if tent == 3:
                perg = str(input('\033[1mDeseja uma dica?[S/N]: ')).upper().strip()
                while perg != 'S' and perg != 'N':
                    perg = str(input('Deseja uma dica?[S/N]: \033[m')).upper().strip()
                if perg == 'S':
                    heroi = str(input(f'\033[1;4;32mO super herói começa com a letra {sort_heroes.strip()[0]}: \033[m')).upper().strip()
                if perg == 'N':
                    heroi = str(input('\033[1;36mDigite o nome do héroi: \033[m')).upper().strip()

            if tent == 0:
                print('\033[1;31mGame Over!\033[m')
                print(f'\033[1;32mA resposta correta era \033[1;4;35m{sort_heroes}!\033[m')
                break

        if heroi == sort_heroes:
            print(f'\033[1;35mParabéns pela adivinhação. O super herói escolhido é \033[1;4;32m{heroi}!\033[m')

if start == 'F':
    print('\033[1;33mVocê saiu do jogo da adivinhação, volte sempre.')
