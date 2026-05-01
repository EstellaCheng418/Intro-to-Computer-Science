# Name: Estella Cheng
# Date: November 20, 2025
# Class Section: 001
# Assignment 10_Part #0: Alphabet Dictionary

#———————————— Problem 0b ————————————
# function: cleanup_string
# input: a string to clean up
# processing: (1) makes the entire string lowercase.
#             (2) retains only alphabetic and numeric characters
#                 all punctuation, spaces, and special characters removed
# output:      returns the cleaned up string

def cleanup_string(data):
    data = data.lower()
    cleaned = ""
    for c in data:
        if c.isalnum():
            cleaned += c
    return cleaned

"""
# TEST CODE
test1 = cleanup_string("Hello World! This is a simple test of this function!")
print (test1)
# helloworldthisisasimpletestofthisfunction
test2 = cleanup_string("ABC123abc this is Another TEST!!!#@@")
print (test2)
# abc123abcthisisanothertest
"""

#———————————— Problem 0a ————————————
phrase = input("Enter a phrase: ")
# call the cleaned up string function on user phrase
clean = cleanup_string(phrase)

# create empty dictionary
dictionary = {}

# loop over cleaned string
for char in clean:
    # if we've seen the char before, increment count
    if char in dictionary.keys():
        dictionary[char] += 1
    # if we haven't seen the char before, add to count
    else:
        dictionary[char] = 1
        
print("Report in ascending order by ASCII value: ")
for k,v in sorted(dictionary.items()):
    print(k,v)

