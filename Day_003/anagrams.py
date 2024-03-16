#!/usr/bin/env python3
"""
Python module that checks if given two strings
are anagrams """


def is_anagram(s1, s2):
    """ Function that takes two strings s1 and s2 and checks
    if they are anagrams """

    if len(s1) != len(s2):
        return False

    # convert the two string to be compare to all in lowercase
    s1 = s1.lower()
    s2 = s2.lower()

    # Creating an array that will store the count of each character
    # Used 256 since it covers the ASCII range
    letters = [0] * 256

    # Count the occurrences of each character in the first string
    for c in s1:
        letters[ord(c)] += 1

    # Decrease the count of each character in the second string
    for c in s2:
        letters[ord(c)] -= 1

    # check if any character count is not zero and in that case
    # If that's the case the strings are not anagrams
    for count in letters:
        if count != 0:
            return False

    # Now, if all character count are zero, the strings are anagrams
    return True


# Usage on calling the function
s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))
