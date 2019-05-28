# 4: It printed all of the letters in front of the days because it has the for 
#    loop. then for the fifth to eight it prints because of another for loop.     
# 7: You need the second line to be 1 so that you have guesses. If it was a it 
#    won't let you play the game
# 10: You need 6000 guesses to make sure you get the right one.
# Conclusion 1: It takes up more memeory and more space
# Conclusion 2: It can easily check through all of them by making the range
#               the length of the data
# Conclusion 3: A while will keep runnning while the statement is true, a for
#               loop will go for as long as the range tells it to
# Conclusion 4: We worked really well together and I think we contributed
#               equally to finishing.
# Assignment Check: The code ran well and worked, that means we finished
'''
days()
roll_hundred_pair()
dice(5)
guess_winner()
goguess()
matches(ticket, winners)
report(guess, secret)
'''

from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

def days():
    ''' Explain the function here
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
    
def roll_hundred_pair():
    a = [] 
    a += [random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])]
    for choices in range(100):
        a += [random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])]
    bins = 1
    plt.hist(a)
    plt.savefig('1.3.7/picks')
roll_hundred_pair()

def dice(a):
    count = 0
    for i in range(a):
        count += random.randint(1,6)
    print (count)
    
def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
    

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Summarize the function in this docstring.
    
    Provide descriptions for the arguments and say what type each one is.
    Describe the type and meaning of the value returned.
    '''
    winner = random.choice(players) 

    ####
    # For the amount of players is the amount of times it runs. 
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # It runs the code as many times as there
    # are players
        print(p+', ', end='')
    print(players[len(players)-1]) # Prints how many players there are

    ####
    # If the input that you type is not the winner then you have to guess again 
    # and it adds one to your guesses. Once you break the loop it tells you how many times you took.
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses
    
def goguess():
    guess = 5
    num = random.randint(1,20)
    print(num)
    answer = int(raw_input("I have a number between 1 and 20 inclusive"))
    while num != answer and guess != 0:
        if(answer < num):
            print(answer, "is too low")
            print("Guesses:",guess)
            guess -= 1
            answer = int(raw_input("I have a number between 1 and 20 inclusive"))
        elif(answer > num):
            print(answer, "is too high")
            print("Guesses:",guess)
            guess -= 1
            answer = int(raw_input("I have a number between 1 and 20 inclusive"))
        else:
            print("Right!")
            
def matches(ticket, winners):
    count = 0
    for i in range(len(ticket)):
        for num in range(len(ticket)):
            if ticket[i] == winners[num]:
                count += 1
    print (count)


guess = ['red','red','red','green','yellow']
secret = ['red','red','yellow','yellow','black']

def report(guess, secret):  
    correct = 0
    incorrect = 0
    for i in range(len(secret)):
        if guess[i] == secret [1]: 
            correct += 1
        else:
            incorrect += 1
    print(correct, incorrect)
    
days()
roll_hundred_pair()
dice(5)
guess_winner()
goguess()
matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17])
report(guess, secret)
    


        
            
        