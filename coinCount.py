'''
Write a program that asks the user to enter a number of quarters, dimes, nickels and
pennies and then outputs the monetary value of the coins in the format of dollars and
remaining cents
'''

print('Please enter the number of coins for each of the following:')
quarters = 0.25 * int(input('Quarters: '))
dimes = 0.10 * int(input('Dimes: '))
nickels = 0.05 * int(input('Nickels: '))
pennies = 0.01 * int(input('Pennies: '))

total = quarters + dimes + nickels + pennies

print('You have a total of:', '$', total)