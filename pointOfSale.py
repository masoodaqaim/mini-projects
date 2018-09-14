'''
Write a program that computes how much a customer has to pay after purchasing two
items. The price is calculated according to the following rules:
• Buy one get one half off promotion: the lower price item is half price.
• If the customer is club card member, additional 10% off.
• Tax is added.
'''

item1 = int(input('Enter price of first item: '))
item2 = int(input('Enter price of second item: '))
clubCard = input("Does customer have a club card (Y/N)?: ")
tax = float(input('Enter tax rate: '))
basePrice = item1 + item2

if item1 > item2:
    discountPrice = item1 + (item2 / 2)
    if clubCard == 'Y':
        discountPrice = discountPrice - (discountPrice * .10)
else:
    discountPrice = item2 + (item1 / 2)
    if clubCard == 'Y':
        discountPrice = discountPrice - (discountPrice * .10)

totalPrice = discountPrice + (discountPrice * (tax / 100))

print('Base price: ', basePrice)
print('Price after discounts: ', discountPrice)
print('Total Price: ', totalPrice)

