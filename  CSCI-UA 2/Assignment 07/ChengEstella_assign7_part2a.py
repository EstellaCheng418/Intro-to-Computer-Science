# Name: Estella Cheng
# Date: October 27, 2025
# Class Section: 001
# Assignment 07_Part #2a: Cryptography

import random

# function 1: ascii_shift
# input: a word to shift(str), an amount to shift(int)
# processing: 1. Shifts each character in the supplied word to another position in the ASCII table.
#             2. The new position is dictated by the supplied integer.
#             3. No shift will occur in case of an empty string. 
# output: returns the newly generated word or the empty string

def ascii_shift(word, num):
    if word == "":
        return ""
    new_word = ""
    for char in word:
        new_word += chr(ord(char) + num)
    return new_word

'''
word = "ABCDEFG"
for i in range(-5,6):
    print("ASCII shifting", word, "by", i, "=>", ascii_shift(word, i))
'''

# function 2: shift_right
# input: a word to shift (str)
# processing: 1. Shift all characters in the string to the right.
#             2. The last character in the string will be shifted to the beginning of the string.
#             3. No shift will occur in case of an empty string. 
# output: returns the newly generated word or the empty string

def shift_right(word):
    if word == "":
        return ""
    return word[-1] + word[:-1]

'''
word = "hello world!"
print("Shifting right", word, "=>", shift_right(word))
'''

# function 3: shift_left 
# input: a word to shift (str)
# processing: 1. Shift all characters in the string to the left.
#             2. The first character in the string will be shifted to the end of the string.
#             3. No shift will occur in case of an empty string. 
# output: returns the newly generated word or the empty string

def shift_left(word):
    if word == "":
        return ""
    return word[1:] + word[0]

'''
word = "hello world!"
print("Shifting left", word, "=>", shift_left(word))
'''

# function 4: flip
# input: a word to flip (str)
# processing: 1. If the word has an even number of characters,
#                split it in half and swap the two halves.
#             2. If the word has an odd number of characters,
#                the middle character stays in its original place,
#                and the parts before and after it are swapped. 
#             3. No flip will occur in case of an empty string. 
# output: returns the newly generated word or the empty string

def flip(word):
    if word == "":
        return ""

    length = len(word)
    mid = length // 2

    if length % 2 == 0:
        return word[mid:] + word[:mid]
    else:
        return word[mid+1:] + word[mid] + word[:mid]

'''
word = "ABCDEFG"
print("Flipping", word, "=>", flip(word))

word = "123456"
print("Flipping", word, "=>", flip(word))
'''

# function 5: add_letters
# input: a word to scramble (str), a number of letters (int)
# processing:
# 1. Use a loop to go through each character and the random module to generate letters.
# 2. Adds a number of random letters (A-Z; a-z) after each letter in the supplied word. 
# output: returns the newly generated word 

def add_letters(word, num):
    if word == "":
        return ""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_word = ""
    
    for char in word:
        new_word += char
        for i in range(num):
             new_word += random.choice(letters)

    return new_word

'''
original = "Hello!"
for num in range(1, 5):
    scrambled = add_letters(original, num)
    print("Adding", num, "random characters to", original, "->", scrambled)
'''

# function 6: delete_characters
# input: a word to analyze (str), the number of characters to remove (int)
# processing:
# 1. Start at the beginning of the string.
# 2. Keep the current character.
# 3. Then skip the next character.
# 4. Repeat until there are no characters.
# output: returns the newly unscrambled word

def delete_characters(word, num):
    if word == "":
        return ""
    return word[::num+1]

'''
word1 = "HdeulHlHom!t"
word2 = "HTLedklFNljioMH!bi"
word3 = "HHHZeZrflqSflzOiosNU!jBk"
word4 = "HFtRKeivFllRNlUlGTaooYwoH!JpXL"

unscrambled1 = delete_characters(word1, 1)
print("Removing 1 character from", word1, "->", unscrambled1)

unscrambled2 = delete_characters(word2, 2)
print("Removing 2 characters from", word2, "->", unscrambled2)

unscrambled3 = delete_characters(word3, 3)
print("Removing 3 characters from", word3, "->", unscrambled3)

unscrambled4 = delete_characters(word4, 4)
print("Removing 4 characters from", word4, "->", unscrambled4)
'''

'''
print(ascii_shift("python",2))
print(ascii_shift("python",-3))
print(shift_right("python"))
print(shift_left("python"))
print(flip("python"))
print(flip("1234567"))
print(add_letters("python",1))
print(delete_characters("python",2))
'''





