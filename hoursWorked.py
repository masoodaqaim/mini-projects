'''
Suppose John and Bill worked for some time and we want to calculate the total time both of
them worked. Write a program that reads number of days, hours, minutes each of them
worked, and prints the total time both of them worked together as days, hours, minutes.
'''

daysJ = int(input('Please enter the number of days John has worked: '))
hoursJ = int(input('Please enter the number of hours John has worked: '))
minutesJ = int(input('Please enter the number of minutes John has worked: '))

daysB = int(input('Please enter the number of days Bill has worked: '))
hoursB = int(input('Please enter the number of hours Bill has worked: '))
minutesB = int(input('Please enter the number of minutes Bill has worked: '))

minutesT = int((1440 * (daysJ + daysB)) + (60 * (hoursJ + hoursB)) + (minutesJ + minutesB))

daysT = int(minutesT / 1440)
minutesT -= int(daysT * 1440)
hoursT = int(minutesT / 60)
minutesT -= int(hoursT * 60)

print('The total time both have worked together is:', daysT, 'days', hoursT, 'hours', minutesT, 'minutes')