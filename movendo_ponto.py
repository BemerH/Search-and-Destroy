import random

def arenaJogo(aux,campo):
    for i in range(aux):
        for j in range(aux):
            print(campo[i][j], end='')
            if j != aux-1:
                print(' - ',end='')
        print()

def funControle(move,campo):
    linha = 0
    coluna = 0
    
    aux = 5
    
    for i in range(aux):
        for j in range(aux):
            if campo[i][j] == 'X':
                linha = i
                coluna = j
                
    campo[linha][coluna] = ''

    if move == 'W':
        funUp(move,linha,coluna,campo)
    elif move == 'S':
        funDown(move,linha,coluna,campo)
    elif move == 'A':
        funLeft(move,linha,coluna,campo)
    elif move == 'D':
        funRight(move,linha,coluna,campo)
        
def funUp(move,linha,coluna,campo):
    campo[linha-1][coluna] = 'X'
def funDown(move,linha,coluna,campo):
    if linha == 4:
        campo[0][coluna] = 'X'
    else:
        campo[linha+1][coluna] = 'X'
def funLeft(move,linha,coluna,campo):
    campo[linha][coluna-1] = 'X'
def funRight(move,linha,coluna,campo):
    if coluna == 4: 
        campo[linha][0] = 'X'
    else:
        campo[linha][coluna+1] = 'X'

linha = random.randint(0,4)
coluna = random.randint(0,4)

linhaDaBola = random.randint(0,4)
colunaDaBola = random.randint(0,4) 

campo = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']] 
campo[linha][coluna] = 'X'
campo[linhaDaBola][colunaDaBola] = 'O'

aux = 5

laco = None
while True:
    #arenaJogo(aux,campo)
    temBolinha = False
    for i in range(aux):
        for j in range(aux):
            if campo[i][j] == 'O':
                temBolinha = True
    if temBolinha == False:
        linhaDaBola = random.randint(0,4)
        colunaDaBola = random.randint(0,4)   
        campo[linhaDaBola][colunaDaBola] = 'O'
    """
    for i in range(aux):
        for i in range(aux):
            if(campo[linha][coluna] != 'O'):
                while True:
                    linhaDaBola = random.randint(0,4)
                    colunaDaBola = random.randint(0,4)
                    
                    if linha != linhaDaBola or coluna != colunaDaBola:
                        campo[linhaDaBola][colunaDaBola] = 'O'   
                        break
      """  
    for i in range(aux):
        for j in range(aux):
                
            print(campo[i][j], end='')
            if j != aux-1:
                print(' - ',end='')
        print()
    
    move = input('Type W,A,S,D:')
    
    if move == '0':
        break
    elif move == 'W' or move == 'A' or move == 'S' or move == 'D':
        funControle(move,campo)
        
    else:
        print('\nAre u kidding me? Type correctly please!\n')
