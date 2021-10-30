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
        dictionary[word.strip()] = [None,[]]
    filehandle.close()
    dictionary.update({'':[True,[]],'a':[True,['']],'i':[True,['']]})
    return dictionary 

def checkwordset(word,word_dict):
    """ given a word word, returns the children of the word that are in the dictionary word_dict"""
    wordset = []
    for letter in range(len(word)):
        # return only valid words
        if word[:letter]+word[letter+1:] in word_dict:
            wordset.append(word[:letter]+word[letter+1:])
    return wordset

def is_reducible(word, word_dict):
    """ recursive function to determine if a word is reducible to '' """
    # if the word has already been checked return whether it reduces
    if word_dict[word][0] is not None:
            return word_dict[word][0]
    # otherwise check all possible valid removals of a single character
    for checkword in checkwordset(word,word_dict):
        if checkword not in word_dict[word][1]:
            word_dict[word][1].append(checkword)
        word_dict[checkword][0] = is_reducible(checkword,word_dict)
        if word_dict[checkword][0] is True:
            for entry in word_dict[checkword][1]:
                if entry not in word_dict[word][1]:
                   word_dict[word][1].append(entry)
                   word_dict[word][1].sort(key=len,reverse=True)
    return '' in word_dict[word][1]
    
def reducibledictionary(word_dict):
    """ determine if a word is reducible"""
    for word in word_dict:
        word_dict[word][0] = is_reducible(word, word_dict)

def printresults(word_dict):
    """ print results in a readable format"""
    results_dict = {}
    # invert the word_dict to create a results dictionary
    for word in word_dict:
        if word_dict[word][0] is True:
            if len(word) not in results_dict:
                results_dict[len(word)] = [word]
            else: 
                results_dict[len(word)].append(word)
    # determine the largest result from the results dictionary
    largestresult = (max(iter(results_dict.keys())),results_dict[max(iter(results_dict.keys()))])
    # print the results
    for result in results_dict:
        print(f'Word length {result}... Found {len(results_dict[result])}.')
    print(f'Length of longest word is {largestresult[0]} and there are {len(largestresult[1])} words(s) of that length.')
    print(f'Answer:  {next(iter(largestresult[1]))}') 
             
# initialize variables.                
word_dictionary = readwordlist('words.txt')
reducibledictionary(word_dictionary)
printresults(word_dictionary)

 