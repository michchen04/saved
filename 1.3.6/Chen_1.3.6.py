# 5. One of the conventions that my teacher makes us use is indenting and making it so text shouldn't go off screen to make it easier to grade
# 5. He wants our variables to be lowercased or a single letter
# 6a. I think it will bring out b becuase it is the second one in order
# 6b. It will bring a and b because it goes from the first to the third but doesn't include the third.
# 7a. It will retrun true becuase the second one in order is ten.
# 7b. It will return 15 becuase now that you retype the assigning to a it resets the value
# 8. It will retrun b and 3 because it returns from the second in order to the last
# 9. It will be false because it sets it to a string and a string isn't equal to a float/int. 
# 10a. It added on the extra strings into the list
# 10b. It adds the values to the end of the list
# 11. This doesn't work because you can't add different types. This instance a list to an int. 
# 12. It is multiply equal so it multiplies the current value of a by three and resets a to that integer. 
# Conclusion 1. The things around the output will be different. They will be either none, () or [].
# Conclusion 2. That will limit it too much and wouldn't be specific enough. 
# Conclusion 3. A function can be run as many times as you wuld like. Deleting local variables that aren't needed clear up memory and space. If 
#               you multiply by a float, you get a decimal while if you use a integer you get no decimal points. I alo learned how to form string 
#               put them together. Also functions and boolean. Also the differences between all the types and how to add things to lists. 
# Assignment Check. I believe I have finished becuase it prints a number that adds two random dice. 

import random

a = (4,3,5,3,2)

def roll_two_dice():
    a = random.randint(1,6);
    b = random.randint(1,6);
    print a + b; 
    
print(roll_two_dice())



