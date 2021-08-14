import random

def funControle(move,campo):
    linha = 0
    coluna = 0
    
    aux = 5
    
    simbol = 'X'
    
    for i in range(aux):
        for j in range(aux):
            if campo[i][j] == simbol:
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
        
"-------------------------------------------------"    
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
"-------------------------------------------------"

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
    
    temBolinha = False
    for i in range(aux):
        for j in range(aux):
            if campo[i][j] == 'O':
                temBolinha = True

    if temBolinha == False:
        while True:
            linhaDaBola = random.randint(0,4)
            colunaDaBola = random.randint(0,4) 
            if campo[linhaDaBola][colunaDaBola] != 'X':
                campo[linhaDaBola][colunaDaBola] = 'O'
                break
    
    for i in range(aux):
        for j in range(aux):
            print(campo[i][j], end='')
            if j != aux-1:
                print(' - ',end='')
        print()
    
    move = input('Type W,A,S,D to move the X and catch the ball. Type 0 if u wanna leave!\n')
    
    if move == '0':
        break
    elif move == 'W' or move == 'A' or move == 'S' or move == 'D':
        funControle(move,campo)
    else:
        print('\nAre u kidding me? Type correctly please!\n')
