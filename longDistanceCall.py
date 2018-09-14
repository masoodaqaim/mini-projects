'''
Write a program that computes the cost of a long-distance call. The cost of the call is
determined according to the following rate schedule:
• Any call started between 8:00 A.M. and 6:00 P.M., Monday through Friday, is billed at a
rate of $0.40 per minute.
• Any call starting before 8:00 A.M. or after 6:00 P.M., Monday through Friday, is charged
at a rate of $0.25 per minute.
• Any call started on a Saturday or Sunday is charged at a rate of $0.15 per minute.
The input will consist of the day of the week, the time the call started, and the length of the
call in minutes.
The output will be the cost of the call.
Notes:
1. The time is to be input in 24-hour notation, so the time 1:30 P.M. is input as 13:30
2. The day of the week will be read as one of the following two character string: Mo Tu
We Th Fr Sa Su
3. The number of minutes will be input as a positive integer.
'''


def longDistanceCall():
    day = input('What day did the call start? (Mo, Tu, We, Th, Fr, Sa, Su): ')
    time = int(input('What time did the call start? (24 hour format): '))
    length = int(input('How long was the call? '))
    # cost = 0

    if day == 'Mo' or 'Tu' or 'We' or 'Th' or 'Fr':
        if time >= 800 and time <= 1800:
            cost = length * .40
        else:
            cost = length * .25
    elif day == 'Su' or 'Sa': # had to use 'elif' instead of 'if'. For some reason cost kept being length * .15
        cost = length * .15
    print('The cost of the call is', cost)


longDistanceCall()
