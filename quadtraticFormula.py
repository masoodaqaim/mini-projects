'''
write a program that does the following:
• Ask user to input three Real numbers a, b and c. They represent the parameters of a
quadratic equation 𝑎𝑥# + 𝑏𝑥 + 𝑐 = 0
• Classify to one of the following:
- ’Infinite number of solutions’ (for example, 0𝑥# + 0𝑥 + 0 = 0 has infinite
number of solutions)
- ’No solution’ (for example, 0𝑥# + 0𝑥 + 4 = 0 has no solution)
- ’No real solution’ (for example, 𝑥# + 4 = 0 has no real solutions)
- ’One real solution’
- ’Two real solutions’
• In cases there are 1 or 2 real solutions, also print the solutions.
'''

import math


a = int(input('Please enter the value for "a": '))
b = int(input('Please enter the value for "b": '))
c = int(input('Please enter the value for "c": '))
d = (b**2) - (4*a*c) # this is the discriminate
dSqrt = math.sqrt(d) # square root of the discriminate

if a == 0 and b == 0 and c == 0:
    print('There are infinite solutions')
if a == 0 and b == 0 and c > 0:
    print('There are no solutions')

if d < 0:
    print('There are no real solutions')
elif d == 0:
    d0 = ((-b) + dSqrt) / (2*a)
    print('There is one solution,', d0)
elif d > 0:
    d1 = ((-b) + dSqrt) / (2*a)
    d2 = ((-b) - dSqrt) / (2*a)
    print('There are two solutions,', d1, ',', d2)