'''
An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter. Ex lumberjack
'''

def isogram(word):
    c = word[0]
    for index in word:
        # print(word[index]) just to test if the code will iterate through each index/element
        if word[index] == word[index:]:
            print(word, 'is not an isogram')

isogram('masod')