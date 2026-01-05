"""
homework_1.3.py

Prints all characters that appear more than once in a given string.
Assumes input is a string.

Author: Christopher Romo
Created: 2023-06-21
"""

the_original_string = input('Input: ')
the_string = the_original_string.lower()
the_dict = dict()
string_length = len(the_string)

# iterate through the string to count occurrences of each character
for char in the_string:
    if char in the_dict.keys():
        the_dict[char] += 1
    else:
        the_dict[char] = 1

# print characters that appear more than once
for key, value in the_dict.items():
    if value > 1:
        print(key, end = ' ')