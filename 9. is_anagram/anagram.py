# coding=utf-8

def clean_word(to_clean):
    """Normalizes and cleans a non-ascii string.

    Args:
        to_clean (string): the string to clean and normalize.

    Returns:
        A cleaned and normalized string
    """
    import string
    import unicodedata
    # turning string into utf-8 unicode.
    # normalizing it - removing all accents and extra nuisances.
    # encoding it into ascii - ignoring cases, removing extra blank spaces.
    # removing punctution
    return unicodedata.normalize('NFKD',
        to_clean).encode('ASCII',
            'ignore').lower().strip().replace(" ", "").translate(None,
                string.punctuation)

def is_anagram(first_word, second_word):
    """Determining if two strings are anagrams of each other.

    Args:
        first_word (string): a string to test for anagram property
        second_word (string): a string to test for anagram property against
                              the first.

    Returns:
        True or False, based on whether the strings are anagram of each other
    """
    clean_first_word = clean_word(first_word)
    clean_second_word = clean_word(second_word)

    # anagrams must have the same length - after being cleaned up
    if len(clean_first_word) != len(clean_second_word):
        return False

    # turning clean second word into an iterator
    clean_second_iter = iter(clean_second_word)
    while True:
        try:
            # making sure every character is contained in the first clean word
            if next(clean_second_iter) not in clean_first_word:
                # if any character is not contained, the words are not anagrams
                return False
        except StopIteration:
            # all words from the second word is contained in the first word
            # therefore, they are anagrams of each other
            return True
