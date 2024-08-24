#Q1

# In the cell below, define a function called sign which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.
def sign(num):
    if(num>0):
        return 1
    elif(num<0):
        return -1
    else:
        return 0

# Q2
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies==1:
        print("Splitting 1 candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)

# Q3
# To prove that prepared_for_weather is buggy, come up with a set of inputs where either:

# the function returns False (but should have returned True), or
# the function returned True (but should have returned False).
# To get credit for completing this question, your code should return a Correct result.

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

#Q4 come up with an equivalent body that uses just one line of code
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
     # Your code goes here (try to keep it to one line!)
         return (number<0)

#Q5.A
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return (ketchup and mustard and onion)

#Q5.B
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not(ketchup or mustard or onion)

#Q5.C
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or(mustard and not ketchup)

#Q6
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (ketchup+mustard+onion==1)
