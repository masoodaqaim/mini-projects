def leapYear(year):
    if year % 4 == 0:  # use == to compare values. = is to assign
        if (year % 100 != 0) or (year % 400 == 0):  # make sure the conditions are correct. you had 100 != instead of 100 ==
                print(year, " is a leap year")
        else:
            print(year, 'is not a leap year')
    else:
        print(year, 'is not a leap year')


userYear = int(input('Please enter a year to check if it is a leap year or not: '))
leapYear(userYear)

'''
a leap year is on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
def leapYear(year):
    if year % 4 == 0:  # use == to compare values. = is to assign
        if (year % 100 == 0) and (year % 400 != 0):  # 
                print(year, " is a leap year")
        else:
            print(year, 'is not a leap year')
'''