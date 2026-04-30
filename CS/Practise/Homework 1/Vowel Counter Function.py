# Vowel Counter Function

# Get user input
s = input("Enter a string: ")

# Convert to lower case
s = s.lower()

count = 0
vowels_found = ""

# Go through each character in the string
for char in s:
    if char in "aeiou": # Check if there is a vowel
        count += 1
        vowels_found = vowels_found + char
        
# Output
print("Number of vowels:", count, "(" + vowels_found + ")")


