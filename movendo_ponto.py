import random

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
    campo[linha+1][coluna] = 'X'
def funLeft(move,linha,coluna,campo):
    campo[linha][coluna-1] = 'X'
def funRight(move,linha,coluna,campo):
    campo[linha][coluna+1] = 'X'

linha = random.randint(0,4)
coluna = random.randint(0,4)

campo = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']] 
campo[linha][coluna] = 'X'

aux = 5

laco = None
while(not laco):
    for i in range(aux):
        for j in range(aux):
            print(campo[i][j], end='')
            if j != aux-1:
                print(' - ',end='')
        print()
    
    move = input('Type W,A,S,D:')
    
    if move == '0':
        break
    
    funControle(move,campo)
    

