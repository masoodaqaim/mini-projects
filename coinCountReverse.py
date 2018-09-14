'''
Write a program that asks the user to enter an amount of money in the format of dollars and
remaining cents. The program should calculate and print the minimum number of coins
(quarters, dimes, nickels and pennies) that are equivalent to the given amount.
'''

dollar = int(input('Please enter the dollar amount: '))
cent = int(input('Please enter the cent amount: '))

total = (100 * dollar) + cent

quarters = int(total / 25)
total -= int(quarters * 25)
dimes = int(total / 10)
total -= int(dimes * 10)
nickels = int(total / 5)
total -= int(nickels * 5)

print(dollar, 'dollars and', cent, "cents are:")
print(quarters, 'quarters')
print(dimes, 'dimes')
print(nickels, 'nickels')
print(total, 'pennies')