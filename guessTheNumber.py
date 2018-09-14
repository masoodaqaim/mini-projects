import random

number = random.randrange(1, 101)

print('We are going to play a number guessing game.')
userNumber = int(input('Please guess a number between 1-100: '))  # by default, intput() is a string. must use int(input()) to cast it

while userNumber != number:
    if userNumber < number:
        # print('Please guess again. The number is higher: ') # i commented this code out. keeping it just for learning purposes
        userNumber = int(input('Please guess again. The number is higher: '))  # you can print text in the parameter of input()
    elif userNumber > number:
        # print('Please guess again. The number is lower: ')
        userNumber = int(input('Please guess again. The number is lower: '))

if userNumber is number:
    print(number, 'is the correct guess!!')
