
# generic import
# import random
#
# print(random.randint(1, 10))

# # function import when a specific function is import from a module
# from random import randint
# print(randint(10, 20))

# universal import is when you import every function from a module
# and you do not need to type the name of that function
# from random import *
#
# print(random())

from random import randint
# generate random integer between and inclusive of 10 and 25 to represent

fuel = randint(10, 25)

miles = randint(200, 400)
# MPG of the car
print("the car can travel " + str(miles) + " miles per gallon")
# display number of gallon of fuel that the car fuel tank can hold
print("the car fuel tank can hold " + str(fuel) + " gallon")
# display the number of miles that the car can travel
print("the car can travel " + str(miles) + " miles on a fuel tank")


