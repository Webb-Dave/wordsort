# Chapter 12, Exercise 4
"""
Exercise 12-4
"""

def readwordlist(filename):
    """ passed a text file filename where the words are on individual lines, returns
    a dictionary of the words and the characters in the word"""
    dictionary = {}
    filehandle = open(filename)
    for word in filehandle:
        dictionary[word.strip()] = word.strip()
    filehandle.close()
    return dictionary 

def wordchildren(word):
    """ given a word word, returns the children of the word"""
    wordset = []
    for letter in range(len(word)):
        wordset.append(word[:letter]+word[letter+1:])
    return wordset
    
def is_reducible(word):
    """ determine if a word is reducible"""
    if word == '':
        return True
    anytrue = False
    for nextword in wordchildren(word):
        if nextword in word_dictionary or reducible_dict.get(nextword,False):
            anytrue = is_reducible(nextword)
    reducible_dict[word] = anytrue
    return reducible_dict[word]
                 
global reducible_dict 
global word_dictionary

reducible_dict = {'':True}
word_dictionary = readwordlist('words.txt')
for word in word_dictionary:
    reducible_dict[word] = is_reducible(word)
longest = 0
longestwords = []
for word in reducible_dict:
    if reducible_dict[word] == True:
        if len(word) > longest:
            longestwords = []
            longest = len(word)
            longestwords.append(word)
        elif len(word) == longest:
            longestwords.append(word)
print(longest, longestwords) 