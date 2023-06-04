import random,os,time 

MatrizPlayer = [
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10
]

MatrizComputador = [
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10
]

MatrizPlayerTela = [
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10
]

MatrizComputadorTela = [
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10
]
 
def tela():
    print(f''' Tabuleiro do Jogador:                         Tabuleiro computador:  
  {MatrizPlayerTela[0][0]} | {MatrizPlayerTela[0][1]} | {MatrizPlayerTela[0][2]} | {MatrizPlayerTela[0][3]} | {MatrizPlayerTela[0][4]} | {MatrizPlayerTela[0][5]} | {MatrizPlayerTela[0][6]} | {MatrizPlayerTela[0][7]} | {MatrizPlayerTela[0][8]} | {MatrizPlayerTela[0][9]}         {MatrizComputadorTela[0][0]} | {MatrizComputadorTela[0][1]} | {MatrizComputadorTela[0][2]} | {MatrizComputadorTela[0][3]} | {MatrizComputadorTela[0][4]} | {MatrizComputadorTela[0][5]} | {MatrizComputadorTela[0][6]} | {MatrizComputadorTela[0][7]} | {MatrizComputadorTela[0][8]} | {MatrizComputadorTela[0][9]}       
-----------------------------------------     -----------------------------------------  
  {MatrizPlayerTela[1][0]} | {MatrizPlayerTela[1][1]} | {MatrizPlayerTela[1][2]} | {MatrizPlayerTela[1][3]} | {MatrizPlayerTela[1][4]} | {MatrizPlayerTela[1][5]} | {MatrizPlayerTela[1][6]} | {MatrizPlayerTela[1][7]} | {MatrizPlayerTela[1][8]} | {MatrizPlayerTela[1][9]}         {MatrizComputadorTela[1][0]} | {MatrizComputadorTela[1][1]} | {MatrizComputadorTela[1][2]} | {MatrizComputadorTela[1][3]} | {MatrizComputadorTela[1][4]} | {MatrizComputadorTela[1][5]} | {MatrizComputadorTela[1][6]} | {MatrizComputadorTela[1][7]} | {MatrizComputadorTela[1][8]} | {MatrizComputadorTela[1][9]}   
-----------------------------------------     -----------------------------------------      
  {MatrizPlayerTela[2][0]} | {MatrizPlayerTela[2][1]} | {MatrizPlayerTela[2][2]} | {MatrizPlayerTela[2][3]} | {MatrizPlayerTela[2][4]} | {MatrizPlayerTela[2][5]} | {MatrizPlayerTela[2][6]} | {MatrizPlayerTela[2][7]} | {MatrizPlayerTela[2][8]} | {MatrizPlayerTela[2][9]}         {MatrizComputadorTela[2][0]} | {MatrizComputadorTela[2][1]} | {MatrizComputadorTela[2][2]} | {MatrizComputadorTela[2][3]} | {MatrizComputadorTela[2][4]} | {MatrizComputadorTela[2][5]} | {MatrizComputadorTela[2][6]} | {MatrizComputadorTela[2][7]} | {MatrizComputadorTela[2][8]} | {MatrizComputadorTela[2][9]}       
-----------------------------------------     -----------------------------------------                                              
  {MatrizPlayerTela[3][0]} | {MatrizPlayerTela[3][1]} | {MatrizPlayerTela[3][2]} | {MatrizPlayerTela[3][3]} | {MatrizPlayerTela[3][4]} | {MatrizPlayerTela[3][5]} | {MatrizPlayerTela[3][6]} | {MatrizPlayerTela[3][7]} | {MatrizPlayerTela[3][8]} | {MatrizPlayerTela[3][9]}         {MatrizComputadorTela[3][0]} | {MatrizComputadorTela[3][1]} | {MatrizComputadorTela[3][2]} | {MatrizComputadorTela[3][3]} | {MatrizComputadorTela[3][4]} | {MatrizComputadorTela[3][5]} | {MatrizComputadorTela[3][6]} | {MatrizComputadorTela[3][7]} | {MatrizComputadorTela[3][8]} | {MatrizComputadorTela[3][9]}       
-----------------------------------------     -----------------------------------------                                                   
  {MatrizPlayerTela[4][0]} | {MatrizPlayerTela[4][1]} | {MatrizPlayerTela[4][2]} | {MatrizPlayerTela[4][3]} | {MatrizPlayerTela[4][4]} | {MatrizPlayerTela[4][5]} | {MatrizPlayerTela[4][6]} | {MatrizPlayerTela[4][7]} | {MatrizPlayerTela[4][8]} | {MatrizPlayerTela[4][9]}         {MatrizComputadorTela[4][0]} | {MatrizComputadorTela[4][1]} | {MatrizComputadorTela[4][2]} | {MatrizComputadorTela[4][3]} | {MatrizComputadorTela[4][4]} | {MatrizComputadorTela[4][5]} | {MatrizComputadorTela[4][6]} | {MatrizComputadorTela[4][7]} | {MatrizComputadorTela[4][8]} | {MatrizComputadorTela[4][9]} 
''')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def rnd(x,y):
    return random.randint(x,y)

def inicio(MatrizJogo,y,z):
    while True:
        if MatrizJogo[y-1][z-1] != 0:
            print('Posição já ocupada')
            y = int(input('Digite a linha: '))
            z = int(input('Digite a coluna: '))
        else:
            MatrizJogo[y-1][z-1] = 1
            break

def verify(MatrizJogo,MatrizTela,y,z):
    MatrizTela[y-1][z-1] = 1
    if MatrizJogo[y-1][z-1] == MatrizTela[y-1][z-1]:
        MatrizTela[y-1][z-1] = '\033[92mX\033[0m'
        print('\033[92mNavio inimigo atingido!\033[0m')
    else:
        MatrizTela[y-1][z-1] = '\033[91mO\033[0m'
        print('\033[91mNenhum navio atingido!\033[0m')
    
def inputs():
    global linha,coluna
    linha = int(input('linha: '))
    coluna = int(input('Coluna: '))
    return linha,coluna  

isInicio = True
while True:
    clear()
    if isInicio:
        for i in range(5):
            print(f''' Bem vindo ao jogo Batalha Naval!
 Digite a posição inicial de seu {i+1}º navio: ''')
            inputs()
            inicio(MatrizPlayer,linha,coluna)
            inicio(MatrizComputador,rnd(0,4),rnd(0,9))
            clear()
    isInicio = False
    tela()
    print('Agora escolha uma posição do tabuleiro inimigo para atacar:')
    inputs()
    clear()
    verify(MatrizComputador,MatrizComputadorTela,linha,coluna)
    tela()
    time.sleep(2)
    print('O computador atacará em:')
    for i in [3,2,1,0]:
        time.sleep(1)
        print(i)
    clear()
    verify(MatrizPlayer,MatrizPlayerTela,rnd(0,4),rnd(0,9))
    tela()
    time.sleep(3)
    if MatrizPlayerTela.count('X') == 5:
        print('''Vitoria do computador!
        Feito por:
        Felipe Augusto
        Johan Stromberg
        Evandro Diniz
        Giuseppe Bruno
        André Eller''')
        break
    elif MatrizComputadorTela.count('X') == 5:
        print('''Vitoria do Player!
        Feito por:
        Felipe Augusto
        Johan Stromberg
        Evandro Diniz
        Giuseppe Bruno
        André Eller''')
        break