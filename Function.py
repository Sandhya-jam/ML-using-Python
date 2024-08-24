# Q1
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    return round(num,2)

#Q2
#The help for round says that ndigits (the second argument) may be negative
num=round(212,-2)
print(num) #200
num=round(212,-1)
print(num) #210
#-1:rounds to nearest 10,-2:rounds to nearest 100 so on..

#Q3.
# Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.
def to_smash(total_candies,friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % friends

# Check your answer
to_smash(92,5) #2
to_smash(140) #2

#Q4.Identify errors
#a.round_to_two_places(9.9999)
# ans:
round(9.9999) #10

#b.x = -10
# y = 5
# Which of the two variables above has the smallest absolute value?
# smallest_abs = min(abs(x,y))
#ans:
x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x),abs(y))

#C.def f(x):
#     y = abs(x)
#return y

# print(f(5))
#Ans:
def f(x):
    y = abs(x)
    return y

print(f(5))