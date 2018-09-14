'''
Write a program that prompts for weight (in pounds) and height (in inches) of a person, and
prints the weight status of that person.
Body mass index (BMI) is a number calculated from a person’s weight and height using the
following formula: 𝑤𝑒𝑖𝑔ℎ𝑡/ℎ𝑒𝑖𝑔ℎ𝑡^2. Where 𝑤𝑒𝑖𝑔ℎ𝑡 is in kilograms and ℎ𝑒𝑖𝑔ℎ𝑡 is in meters.
Note: 1 pound is 0.453592 kilograms and 1 inch is 0.0254 meters.
'''


def bmi():
    weight = int(input('Please enter your weight in pounds: '))
    height = int(input('Please enter your height in inches: '))
    x = (weight * 0.453592) / ((height * 0.0254) ** 2)  # this is the formula to calculate bmi (wight/height^2)
    if x < 18.5:
        print('Your bmi is ', x, 'and you are underweight')
    elif x >= 18.5 and x < 25:
        print('Your bmi is ', x, 'and your weight is normal')
    elif x >= 25 and x < 30:
        print('Your bmi is ', x, 'and you are overweight')
    else:
        print('Your bmi is ', x, 'and you are obese')


bmi()
