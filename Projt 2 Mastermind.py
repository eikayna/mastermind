#MASTERMIND
#MVP
from random import randint
from random import choice

print("les couleurs possibles a utilise: RED_:'R'\n WHITE_:'W'\n BLACK:'B'\n GRUEE:'G'\n BLUE:'L'\n PURPURLE:'P'\n")
print ('Veuillez entrer quatre couleurs un par un : ')
couleurs=[' RED',' WHITE','BLACK','GRUEEN',' BLUE','PURPURLE']

def select_random(couleurs):
    random.choice(couleurs, 4, False)
for i in range(4):
    couleur=input(f'veuilliez entrez couleur {i}:')
    i+=1
    print(couleur)

def select_random(code_size):
    if code_size <= 6:
        return couleurs[:code_size]
    else:
        return couleurs

def secret_code(code_size, couleurs):
    S = ''
    for _ in range(code_size):
        S += choice(couleurs)
def check_guess(guess, code_size, coulors):
    verifier_couleurs = [ i in couleurs for i in guess ]
    return len( guess ) == code_size and False not in verifier_couleurs
def score_guess(code, guess):
    n_correct = 0
    n_partiel = 0
    if len( code ) == len( guess ):
        for i in range( len(code) ):
            if code[i] == guess[i]:
                n_correct += 1
            elif guess[i] in code:
                n_partiel += 1
        
        return n_correct , n_partiel
def play(code_size, nb_couleurs):
    print(f'Les différentes couleurs possibles sont: {select_random(nb_couleurs)}.')
    print(f'Le code à trouver est de longueur {code_size}.')
    c = 0
    to_find = secret_code(code_size, select_random(nb_couleurs))
    while True:
        guess = input(f'{c} --> ').upper()
        if not check_guess(guess, code_size, select_random(nb_couleurs)):
            print('erreur')
        elif guess != to_find:
            print( score_guess(to_find, guess) )
            c += 1
        else:
            print( f'bravo, vous avez fait {n+1} essais' )
            break
def changer(guess,changement):
changement=[]
while geuss[i






        
        

    
                         
 
