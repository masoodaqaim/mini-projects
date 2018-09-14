'''
Define the following constants:
const int FLOOR_ROUND = 1;
const int CEILING_ROUND = 2;
const int ROUND = 3;
Write a program that asks the user to enter a Real number, then it asks the user to enter the
method by which they want to round that number (floor, ceiling or to the nearest integer).
The program will then print the rounded result.
Use a switch method. Python does not have a specific method for switch so work around it
'''

def rounding(x):
    return {
        '1': number / 1,
        '2': (number / 1) + 1,
    }


number = float(input('Please enter a number: '))
round = input('Please enter a method to round: ')

rounding(round)                     