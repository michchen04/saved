# 5. Float and int can represent six million. 
# 6. The first one is two strings so when they add them together it becomes a string. The second one adds a string and an int which just doesn't work because they are different booleans. h
# 7. The first character is M. The third character is a space. The ninth is 1 and there is no twenty seventh letter. The letter two from the end is s. The nevagtive seven is seventh from the end which is H.
# 8. slogan[17:23]
# 9. slogan[17:23] + ' is what you call my school!'
# 10a. The output is seven because it counted how long the string Theater was but since it starts at zero it subtracts one form the real length.
# 10b. It made the limitations the first letter all the way to the length of the string minus one. That is Theater without the last letter so theatre. 
# 11. Since the string 'test goo' is found in the string 'Greatest good for the greatest number!', it came out as true.
# Assignment Check 1. Because my code worked and printed 4 and 1. It worked. 

slogan = 'My school is the best'
def how_eligible(essay):
    count = 0;
    if ',' in essay:
        count += 1;
    if '!' in essay:
        count += 1;
    if '?' in essay:
        count += 1;
    if '"' in essay:
        count += 1;
    print count; 
    
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))
    
        





