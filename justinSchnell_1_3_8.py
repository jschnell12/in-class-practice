'''from __future__ import print_function
import random

def guess_winner(players = ('Amy', 'Bill', 'Cathy', 'Dale')):
    '''This function will take a list as a parameter and return a random winner from the list'''
    
    winner = random.choice(players)
    
    ####
    # This will print each of the players in a list
    ####
    print('Guess which of these people won the lottery: ', end = '')
    for p in players[:len(players) - 1]: # This will run through the players list
        print(p + ', ', end = '')
    print(players[len(players) - 1]) #This will print the winner
    
    ####
    # This will determine the amount of guesses that will be used to get the correct answer
    ####
    guesses = 1
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessesd in', guesses, 'guesses!')
    return guesses
