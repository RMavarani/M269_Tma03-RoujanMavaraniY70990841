from data import *
from os import *

def transform_punctuation(line: str):
    # """ transform any punctuation characters in line into spaces
    #     returns the transformed line
    # """
    # You do not need to change this function or understand it in detail
    for  p in ['(','[', '{',')', ']','}', '.',',',';',':','_']:
        line = line.replace(p, ' ')
    return line




# """  You will need to complete this function so it carries out the
#      specified purpose. You should also set the return type annotation.
# """

def get_excluded_words(filename: str):
    """Return the excluded words occurring in filename in a suitable data
       structure.

       filename is a string with the name of a text file
    """

     #  replace with your code

    # We have provided the necessary file handling code below to extract
    # each word from the file, since there should be no punctuation or
    # extraneous characters in the file
    words=[]
    # open the file in read-only mode
    with open(filename, 'r', encoding ='utf-8') as file:

        # go through the file line by line
        for line in file:

            # use space to separate the words in a line
            for word in line.split():
                words.append(word)  #  replace with your code

    return words


"""  You will need to amend this function so that the excluded
     words passed to the function are not added to the bag of words
     that is returned. You should also set the type annotation
     for the excluded words argument.
"""
def bag_of_words(filename: str, excluded_words):
    """Return the words occurring in filename as a bag-of-words.

       filename is a string with the name of a text file
    """
    # You do not need to understand the file handling code in detail
    words = Bag()
    # open the file in read-only mode
    with open(filename, "r", encoding="utf-8") as file:
        # go through the file line by line
        for line in file:
            # transform punctuation into space
            line = transform_punctuation(line)
            if not (line==''):
            # use space to separate the words in a line
                for word in line.split():
                    # remove quote marks and other characters
                    word = word.strip("'\"!?+-*/#‘’—")
                    # put in lowercase
                    word = word.lower()
                    if not(word ==''):
                        if not (word in excluded_words):
                            words.add(word)
    return words


print("Collecting excluded words in Shakespeare's Hamlet...")
"""  Replace the following line by your code to read the excluded words from text file
     'hamlet_excluded_words.txt' and to store them in a suitable data structure.
"""
excluded_words = get_excluded_words('hamlet_excluded_words.txt')  # This is just a placeholder

print("Collecting words in Shakespeare's Hamlet...")
"""  You should not need to amend the following function call.
"""
all_words = bag_of_words('hamlet.txt', excluded_words)


print('Sorting the words by decreasing frequency...')
#  Add your code here to produce the ordered list
data=all_words.ordered()

TOP = 20
print("The", TOP, "most frequent words are:")
#  Add your code here to print out the start of the ordered listf

i=0
for i in range(20):
    n=i+1
    print(n,data[i])
    i+=1
    
    
