'''
Write a program that:
• Asks the user for their name.
• Asks the user to input their graduation year.
• Asks the user to input the current year.
Assume the student is in a four-year undergraduate program. Display the current status the
student is in. Possible status include: not in college yet, freshman, sophomore, junior, senior,
graduated.
'''

name = input('Please enter you name: ')
gradYear = int(input('When do you graduate?: '))
currentYear = int(input('What is the current year?: '))

if gradYear - currentYear <= 0:
    print(name, ', you have already graduated.')
elif gradYear - currentYear == 1:
    print(name, ', you are a senior.')
elif gradYear - currentYear == 2:
    print(name, ', you are a junior.')
elif gradYear - currentYear == 3:
    print(name, ', you are a sophomore.')
elif gradYear - currentYear == 4:
    print(name, ', you are a freshman.')
else:
    print(name, ', you are not in college yet.')