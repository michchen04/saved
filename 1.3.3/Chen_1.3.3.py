from __future__ import print_function # use Python 3.0 printing 

def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT) 
    
def report_grade(percent): 
    if percent < 80:
        print(percent, 'percent does not indicate mastery. Seek extra practice or help.')
    else:
        print(percent, 'percent indicates mastery. Keep up the good work!')
        
def letter_in_word(guess, word):
    if guess in word:
        return True
    else: 
        return False
    
def hint(color, secret):
    if color in secret:
        print(color, 'IS in the secret sequence of colors.')
    else:
        print(color, 'IS NOT in the secret sequence of colors.')


#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)