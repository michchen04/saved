#Part I. Nested if structures and testing
#1a. The return result comes from line 17.
#1b i. food_id('orange')
#1b ii. food_id('apple')
#1b iii. food_id('potato')
#1b iv. Nothing can be inputted to make it run line 22 unless it's string isn't in the array
#4. You would use numbers that would qualify for each like 9, 8, and 12
#

def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
            
    
def food_id_test():
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

def f(n):
    """Put a number into the parenthesis, if they fit within the goods, then do the goods. Based off of the characteristics of the number, the computer will try to guess the number"""
    if int(n)==n:
        if True:
            if n%2==0:
                if n%3==0:
                    print("n is a multiple of 6")
                else:
                    print("n is even")
            else:
                print("n is odd")
        else:
            print("n is not an integer")

def f_test():
    works = True
    if f(8) != 'n is even':
        works = 'even bug in f_test()'
    if f(9) != 'n is odd':
        works = 'odd bug in f_test()'
    if f(12) != 'n is a multiple of 6':
        works = 'multiple of 6 bug in f_test()'
    if f(1.5) != 'n is not an integer':
        works = 'multiple of 6 bug in f_test()'


        


    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False









print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
#guess_once()
#guess_once()
#quiz_decimal(4, 4.1)
#quiz_decimal(4, 4.1)
#f_challenge(1.1)
#f_challenge(2)
#f_challenge(3)
#f_challenge(6)
