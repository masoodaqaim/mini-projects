'''
enter a string and count the number of vowels. Report the sum of each vowel
'''

userInput = input('Please enter a word: ')

vowelT = 0
vA = 0
vE = 0
vI = 0
vO = 0
vU = 0
for i in userInput:
    if 'a' in userInput:
        vA += 1
    elif 'e' in userInput:
        vE += 1
    elif 'i' in userInput:
        vI += 1
    elif 'o' in userInput:
        vO += 1
    elif 'u' in userInput:
        vU += 1

print(vowelT)
print(vA)
