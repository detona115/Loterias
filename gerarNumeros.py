'''
Created on 26 de jul de 2019

@author: ANDY
'''
from random import randint

def gerarMega(restrict):
    
    """esta função é responsável por gerar números aleatórios 
    e gerênciar os números a serem eliminados caso selecionado"""
    
    aleat = randint(1, 60) 
    
    if restrict[0].isChecked() == True:
                        
        while aleat in range(1, 11):
            aleat = randint(1, 60)
        
    if restrict[1].isChecked() == True:
                    
        while aleat in range(11, 21):
            aleat = randint(1, 60)   
    
    if restrict[2].isChecked() == True:
                    
        while aleat in range(21, 31):
            aleat = randint(1, 60)
            
    if restrict[3].isChecked() == True:
                    
        while aleat in range(31, 41):
            aleat = randint(1, 60)
    
    if restrict[4].isChecked() == True:
                    
        while aleat in range(41, 51):
            aleat = randint(1, 60)
            
    if restrict[5].isChecked() == True:
                    
        while aleat in range(51, 61):
            aleat = randint(1, 60)        
    
    if restrict[6].isChecked() == True:
                    
        while aleat in range(1, 31):
            aleat = randint(1, 60)     
            
    if restrict[7].isChecked() == True:
                    
        while aleat in range(31, 61):
            aleat = randint(1, 60)          
    
    return aleat

def gerarLoto(restrict):
    
    aleat = randint(1, 25)
    
    if restrict[0].isChecked() == True:
                        
        while aleat in range(1, 6):
            aleat = randint(1, 25)
        
    if restrict[1].isChecked() == True:
                    
        while aleat in range(6, 11):
            aleat = randint(1, 25)   
    
    if restrict[2].isChecked() == True:
                    
        while aleat in range(11, 16):
            aleat = randint(1, 25)
            
    if restrict[3].isChecked() == True:
                    
        while aleat in range(16, 21):
            aleat = randint(1, 25)
    
    if restrict[4].isChecked() == True:
                    
        while aleat in range(21, 26):
            aleat = randint(1, 25)
    
    return aleat