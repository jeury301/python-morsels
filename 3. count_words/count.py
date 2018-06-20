
def count_words(string_to_map):
    """Determine the frequency of each word on a given string

    Args:
        string_to_map: A string to convert to a map of frequencies

    Returns:
        A map of frequencies of the words in the given string
    """
    formatted_string = string_to_map.lower().split(" ")
    map_of_freq = {}

    for word in formatted_string:
        # cleaing the word AKA removing punctionation
        clean_word = word_cleaner(word)

        # check if new word
        if map_of_freq.get(clean_word) is None:
            # new word found
            map_of_freq[clean_word] = 0
        map_of_freq[clean_word]+=1

    return map_of_freq

def word_cleaner(word_to_clean):
    """Removes any punctuation from word

    Args: 
        word_to_clean: Dirty word

    Returns
        A word without punctionation [a...zA...Z]
    """
    clean_word = ""

    first = 0 # position of first word
    last = len(word_to_clean) - 1 # position of last word
    count = 0 # counter for current position
    for letter in word_to_clean:
        # checking for first or last only
        if count == first or count == last:
            # check if letter is within valid range AKA ignore punctuation
            if letter > "Z" and letter < "z":
                # letter is valid, append to final cleaned word
                clean_word+=letter
        else:
            # not first or last letter
            clean_word+=letter
        count+=1
    return clean_word


