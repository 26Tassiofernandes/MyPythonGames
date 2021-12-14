# Nesse programa simulamos um restaurante contendo comidas variadas, desde pratos principais até sobremesas. Bom apetite!


print('=' * 37)
print('\033[1;7;40mBem vindo ao restaurante Boi na Brasa\033[m')
print('\033[1;7;40mFaça seu pedido abaixo\033[m')
print('=' * 37)

print('''\033[1m[1]Peixe frito
[2]Costela de porco
[3]Bife grelhado
[4]Hambúrguer com fritas  
[5]Panqueca recheada com linguiça\033[m''')

opcao = int(input('\033[1;4;33mDigite sua opção: \033[m'))

while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
    opcao = int(input('\033[1;31mOpção inválida, tente novamente: \033[m'))

if opcao == 1:
    print('\033[1;40mBoa pedida! O peixe frito é um delicioso prato.\033[m')
if opcao == 2:
    print('\033[1;40mUma costelinha deliciosa de porco saindo da brasa.\033[m')
if opcao == 3:
    print('\033[1;40mBife grelhado: uma das nossas especialidades da casa.\033[m')
if opcao == 4:
    print('\033[1;40mAqui fazemos hambúrgueres com fritas melhores que os do Burger King, confia!\033[m')
if opcao == 5:
    print('\033[1;40mMelhores panquecas do mundo, ainda por cima recheadas com linguiça, duvido você encontrar melhores.\033[m')

x = str(input('\033[1;4;35mDeseja uma bebida como acompanhante?[S/N]: \033[m')).upper().strip()
while x != 'S' and x != 'N':
    x = str(input('\033[1;4;35mDeseja uma bebida como acompanhante?[S/N]: \033[m')).upper().strip()

if x == 'S':
    print('''\033[1m[1]Suco de laranja
[2]Suco de limão
[3]Suco de uva
[4]Refrigerante em lata
[5]Achocolatado\033[m''')

opcao2 = int(input('\033[1;4;36mDigite sua opção: \033[m'))
while opcao2 != 1 and opcao2 != 2 and opcao2 != 3 and opcao2 != 4 and opcao2 != 5:
    opcao2 = int(input('\033[1;4;36mDigite sua opção: \033[m'))
if opcao2 == 1:
    print('\033[1;40mQue maravilha, traremos o mais rápido possível!\033[m')
if opcao2 == 2:
    print('\033[1;40mSaindo um suco de limão para refrescar sua mente.\033[m')
if opcao2 == 3:
    print('\033[1;40mSucos de uva geralmente são bem generosos, por aqui não é diferente.\033[m')
if opcao2 == 4:
    print('\033[1;40mUma latinha gelada pra já.\033[m')
if opcao2 == 5:
    print('\033[1;40mA nossa caneca de acholatado promete ser uma beleza.\033[m')

y = str(input('\033[1;4;32mDeseja uma deliciosa sobremesa? [S/N]: \033[m')).upper().strip()
while y != 'S' and y != 'N':
    y = str(input('\033[1;4;32mDeseja uma deliciosa sobremesa? [S/N]: \033[m')).upper().strip()

if y == 'S':
    print('''\033[1m[1]Pudim de leite
[2]Açaí natural
[3]Mousse de chocolate
[4]Sorvete de baunilha
[5]Goiabada''')

    opcao3 = int(input('\033[1;4;35mDigite sua opção: \033[m'))
    while opcao3 != 1 and opcao3 != 2 and opcao3 != 3 and opcao3 != 4 and opcao3 != 5:
        opcao3 = int(input('\033[1;4;35mDigite sua opção: \033[m'))

    if opcao3 == 1:
        print('\033[1;40mAs vezes, tudo que precisamos é de um pudim gigante gelado.\033[m')
    if opcao3 == 2:
        print('\033[1;40mDizemos não ao açaí fake, aqui servimos açaí raiz.\033[m')
    if opcao3 == 3:
        print('\033[1;40mO nosso mousse de chocolate é delicioso demais, prometemos não decepcionar.\033[m')
    if opcao3 == 4:
        print('\033[1;40mNossos cozinheiros preparam um sorvete de baunilha especial, aproveite.\033[m')
    if opcao3 == 5:
        print('\033[1;40mGoiabada regional suculenta e de bom agrado.\033[m')

print('\033[1;7;40mBom apetite, agradecemos a preferência!\033[m')
