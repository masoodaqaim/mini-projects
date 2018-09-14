'''
Write a program that reads from the user two positive integers, and prints the result of
when we add, subtract multiply, divide, div and mod them.
'''

num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))
numAdd = num1 + num2
numSub = num1 - num2
numMul = num1 * num2
numDiv = int(num1 / num2)
numMod = num1 % num2

print(num1, '+', num2, '=', numAdd)
print(num1, '-', num2, '=', numSub)
print(num1, '*', num2, '=', numMul)
print(num1, '/', num2, '=', numDiv)
print(num1, '%', num2, '=', numMod)
