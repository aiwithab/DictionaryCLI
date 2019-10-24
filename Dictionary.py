"""
Dictionary CLI application made by AbdulAhad || (aiwithab) 
date: 24th of January 2018
Instructions: Run file in commandline enter word you want to search as commandline argument hit enter. #SAF (keep data.json file in same directory)
"""

from difflib import get_close_matches
import json

data = json.load(open("data.json"))  # loaded the word def key value pair json


def translate(words):
    words = words.lower() # for lower case input

    if words in data:
        return data[words]
    elif len(get_close_matches(words, data.keys())) > 0:
        yesno = input("did you mean %s instead, Enter Y if yes, N if no." % get_close_matches(words, data.keys())[0])

        if yesno == "Y":
            return data[get_close_matches(words, data.keys())[0]]

        elif yesno == "N":
            return "Try again, please double check no such word found in database."
        else:
            return "We did not understand your entry please try again."

    else:
        return "Word does not exist please try again! please double check your spelling"


word = input("***************************************\n\nEnter word here:  ")
print('\n***************************************')
output = translate(word)

if type(output) == list:

    for items in output:
        print('***************************************\n\n')
        print('Meaning of given word is : {}\n\n'.format(items))
        print('***************************************\n\n')
else:
    print('***************************************\n\n')
    print('Meaning of given word is : {}'.format(output))


