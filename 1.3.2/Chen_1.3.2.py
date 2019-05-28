def add_tip(total, tip_percent): 
    tip = tip_percent*total
    return total + tip
    
def hyp(leg1, leg2):
    hypotenuse = leg1**2.0 + leg2**2.0 
    return hypotenuse**0.5

def mean(a, b, c):
    num = a + b + c
    return num/3.0
    
def perimeter(base, height):
    sum = 2.0 * base + 2.0 * height
    return sum
    
#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)