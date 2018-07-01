def v0_is_anagram(word1, word2):
    """Return True if the given words are anagrams.

    That won't work for words that have the same letters but they occur
    a different number of times.
    """
    return set(word1) == set(word2)

def count_letters(word):
    letters = {}
    for char in word:
        letters.setdefault(char, 0)
        letters[char] += 1
    return letters

def v1_is_anagram(word1, word2):
    """Return True if the given words are anagrams.

    Instead of set, we could make a function that accepts a string and
    returns a dictionary of character counts for the string.
    """
    return count_letters(word1) == count_letters(word2)

from collections import Counter

def v2_is_anagram(word1, word2):
    """Return True if the given words are anagrams.

    Using Counter which does exactly the same as count_letters.
    """
    return Counter(word1) == Counter(word2)

def v3_is_anagram(word1, word2):
    """Return True if the given words are anagrams.

    Using the built-in python function - sorted.
    """
    return sorted(word1) == sorted(word2)

def v4_is_anagram(word1, word2):
    """Return True if the given words are anagrams.

    Normalizing the words by lower-casing them.
    """
    word1, word2 = word1.lower(), word2.lower()
    return sorted(word1) == sorted(word2)

def v5_is_anagram(word1, word2):
    """Return True if the given words are anagrams.

    Solving the first bonus: make sure we ignore spaces.
    """
    word1, word2 = word1.lower(), word2.lower()
    return Counter(word1.replace(' ', '')) == Counter(word2.replace(' ', ''))

def v6_is_anagram(word1, word2):
    """Return True if the given words are anagrams.

    Solving the second bonus: ignoring extra stuff.
    """
    word1, word2 = word1.lower(), word2.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters1 = sorted(c for c in word1 if c in alphabet)
    letters2 = sorted(c for c in word2 if c in alphabet)
    return letters1 == letters2

def v7_is_anagram(word1, word2):
    """Return True if the given words are anagrams.

    Replacing the alphabet.
    """
    word1, word2 = word1.lower(), word2.lower()
    letters1 = sorted(c for c in word1 if c.isalpha())
    letters2 = sorted(c for c in word2 if c.isalpha())
    return letters1 == letters2

def letters_in(string):
    """Return sorted list of letters in given string."""
    return sorted(
        char
        for char in string.lower()
        if char.isalpha()
    )

def v8_is_anagram(word1, word2):
    """Return True if the given words are anagrams.

    Moving sorted(...) into a function - for clean up purposes
    """
    return letters_in(word1) == letters_in(word2)

def count_letters(string):
    """Return sorted list of letters in given string."""
    return Counter(
        char
        for char in string.lower()
        if char.isalpha()
    )

def v9_is_anagram(word1, word2):
    """Return True if the given words are anagrams.

    Using Counter instead of sorted.
    """
    return count_letters(word1) == count_letters(word2)

import unicodedata

def remove_accents(string):
    """Return decomposed form of the given string."""
    return unicodedata.normalize('NFKD', string)

def letters_in(string):
    """Return sorted list of letters in given string."""
    string = remove_accents(string.lower())
    return sorted(
        char
        for char in string
        if char.isalpha()
    )

def v10_is_anagram(word1, word2):
    """Return True if the given words are anagrams.

    Last bonus: removing accents.
    """
    return letters_in(word1) == letters_in(word2)
