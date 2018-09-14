'''
have a user enter a word and print it in reverse
'''

userInput = input('Please enter a word to be printed in reverse: ')
print(userInput[::-1]) # you can use [::-1]
                       # This is extended slice syntax. It works by doing [begin:end:step]
                       # by leaving begin and end off and specifying a step of -1, it reverses a string

'''
this is the code i had earlier
for i in userInput:
    length = len(userInput)
    i = 1
    print(userInput[length-i])
    i += 1
'''
