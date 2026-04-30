# Name: Estella Cheng
# Date: October 27, 2025
# Class Section: 001
# Assignment 07_Part #2b

import random

# —————————— Helper functions from Part 2a ——————————

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

# —————————— main encoder/decoder loop ——————————
while True:
    pattern = input("Enter an encoding pattern, 'end' to end: ")
    if pattern == "end":
        break

    word = input("Enter a word to encode/decode: ")

    # Accumulator
    current = word
    
    # Go through each command letter in the pattern
    for cmd in pattern:
        if cmd == 'A':
            current = add_letters(current, 1)
            print("* Added 1 character:", current)

        elif cmd == 'X':
            current = delete_characters(current, 1)
            print("* Deleted 1 character:", current)

        elif cmd == 'F':
            current = flip(current)
            print("* Flipped:", current)

        elif cmd == 'U':
            current = ascii_shift(current, 1)
            print("* ASCII shifted up:", current)

        elif cmd == 'D':
            current = ascii_shift(current, -1)
            print("* ASCII shifted down:", current)

        elif cmd == 'L':
            current = shift_left(current)
            print("* Shifted left:", current)

        elif cmd == 'R':
            current = shift_right(current)
            print("* Shifted right:", current)

    print()
       
        

        
            



        
            
    

    





