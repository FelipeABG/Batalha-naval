import random,os,time 
from functions import inicio, verify,tela, vitoria
from matrizes import MatrizComputadorTela, MatrizComputador, MatrizPlayer, MatrizPlayerTela

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def rnd(x,y):
    return random.randint(x,y)

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
    tela(MatrizPlayerTela, MatrizComputadorTela)
    print('Agora escolha uma posição do tabuleiro inimigo para atacar:')
    inputs()
    clear()
    verify(MatrizComputador,MatrizComputadorTela,linha,coluna)
    tela(MatrizPlayerTela, MatrizComputadorTela)
    time.sleep(2)
    print('O computador atacará em:')
    for i in [3,2,1,0]:
        time.sleep(1)
        print(i)
    clear()
    verify(MatrizPlayer,MatrizPlayerTela,rnd(0,4),rnd(0,9))
    tela(MatrizPlayerTela, MatrizComputadorTela)
    time.sleep(3)
    if MatrizPlayerTela.count('X') == 5:
        vitoria('Computador')
        break
    elif MatrizComputadorTela.count('X') == 5:
        vitoria('Player')
        break