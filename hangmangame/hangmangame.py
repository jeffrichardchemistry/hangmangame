import random
import numpy as np
import os

forca = ['''
    ------
    |    |
    |    |
    |     
    |
    |
    |
============
''','''
    ------
    |    |
    |    |
    |    O 
    |
    |
    |
============
''','''
    ------
    |    |
    |    |
    |    O 
    |    |
    |    |
    |
============
''','''
    ------
    |    |
    |    |
    |    O 
    |    |
    |    |
    |   /
============
''','''
    ------
    |    |
    |    |
    |    O 
    |    |
    |    |
    |   / \\
============
''','''
    ------
    |    |
    |    |
    |    O 
    |    |\\
    |    |
    |   / \\
============''','''
    ------
    |    |
    |    |
    |    O 
    |   /|\\
    |    |
    |   / \\
============
''']

class hangman():
    def __init__(self, quadro=forca):
        self.forca = quadro
        self.choiceword = ''        
        

    def runHangman(self):
        self.mode = str(input('Single player/Multiplayer [0/1]: '))    
        if self.mode == '0':
            self.choiceword = hangman.Words(self)
            self.underline = hangman.makeUnderline(self)
            hangman.main(self)
        
        elif self.mode == '1':
            self.choiceword = str(input('Type a word: '))
            os.system('clear')
            self.underline = hangman.makeUnderline(self)
            hangman.main(self)

        else:
            print('Wrong option, please for single player type 0 and multiplayer type 1.')        

    def main(self):
        start = True
        chutes = []
        poses = []
        lose = 0
        all_chutes = []

        while start:            
            print(self.forca[lose])
            print(self.underline)
            
            chute = str(input('\nDigite sua letra:'))

            all_chutes.append(chute.lower())
              
            if chute.lower() in self.choiceword.lower():
                chutes.append(chute.lower())                
                poses.append(hangman.testepos(self,chute))
                            
                self.underline = hangman.makeUnderline(self,pos=poses, chut=chutes)       

                if '_' not in self.underline:
                    print('\n*************\nYOU WIN!!!!!!\n*************\n')
                    print('The word is: {}\n'.format(self.choiceword))

                    start = False
     
            else:
                lose += 1
                if lose == len(self.forca) - 1:
                    print(self.forca[len(forca)-1])
                    print('\nYOU LOSE !!!!!!!\n')
                    print('The word is: {}'.format(self.choiceword))
                    start = False

            print('All chutes = ',all_chutes) 

    def Words(self):
        palavras = ['cachorro', 'gato', 'elefante', 'passaro', 'peixe',
                    'coelho', 'papagaio', 'sapo', 'aranha', 'galinha',
                    'hiena', 'tartaruga', 'formiga', 'pato', 'leao',
                    'guepardo', 'tubarao']

        return random.choice(palavras)
    
    def makeUnderline(self, pos=[0,0], chut=['_','_']):
        under = np.array(['_' for i in range(len(self.choiceword))])
        for i,chute in enumerate(chut):
            under[pos[i]] = chute

        return under

    def testepos(self, char):
        positions = []
        for pos, letra in enumerate(self.choiceword):
            if letra == char:
                positions.append(pos)
        return positions
