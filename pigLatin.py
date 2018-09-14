'''
create a program that takes the first letter of a word and places it at the end and adds 'ay'
ex. banana = anana-bay
'''

userInput = input('Please enter a word to be converted to pig latin: ')
newWord = userInput[1:]
print(newWord + '-' + userInput[0] + 'ay')
