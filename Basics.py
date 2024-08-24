# Q.0
# create a variable called color with an appropriate value on the line below
# (Remember, strings in Python must be enclosed in 'single' or "double" quotes)"
color="blue"

#Q.1
pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius=diameter/2
# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area=pi*radius*radius

#Q2
a = [1, 2, 3]
b = [3, 2, 1]

# Your code goes here. Swap the values to which a and b refer.
c=a
a=b
b=c

# Q3.a
# Add parentheses to the following expression so that it evaluates to 1.
(5 - 3 )// 2   #o/p:0

#Q3.b
# Add parentheses to the following expression so that it evaluates to 0.
(8 - 3 )*( 2 - (1 + 1))

#Q4.
# Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
# Write an arithmetic expression below to calculate how many candies they must smash for a given haul.
# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
candy=(121+77+109)//3
alice_candies=candy
bob_candies = candy
carol_candies = candy
to_smash =(121+77+109)%3
