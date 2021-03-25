# -----------------------------------------------------------------------------
# Name:        translate
# Purpose:     Assignment 3 solution
#
# Author:      Rula Khayrallah
# -----------------------------------------------------------------------------
"""
Convert a message to a secret language

Each word in the text is translated according to the following rules:
If the word starts with a vowel 'zus' is added to the end of the word.
Otherwise, the first letter of the word is moved to the end
and followed by 'ix'.
"""

VOWELS = ['a', 'e', 'i', 'o', 'u']


def starts_with_vowel(word):
    """
    Determine whether a given word starts with a vowel

    Parameter: word (string)
    Returns:  boolean
    """
    return word[0] in VOWELS


def encode(word):
    """
    Translate a single word into the secret language

    Parameter: word (string)
    Returns: translated word (string)
    """
    if starts_with_vowel(word):
        result = word + 'zus'
    else:
        result = word[1:] + word[0] + 'ix'
    return result


def translate(text):
    """
    Translate a given text into secret language

    Parameter: text(string) - a string containing one or more words separated
        by space character(s)
    Returns: a string containing all the translated words
    """
    words = text.split()   # Get a list of the words
    new_words = []         # List of translated words
    for each_word in words:     # Go over each of the words
        new_words.append(encode(each_word))  # aAd translated word
    result = ' '.join(new_words)  # Put translated words in a single string
    return result


def get_input():
    """
    Prompt the user for input and return the input

    Parameter: None
    Returns: the user input (string)
    """
    more_input = True
    while more_input:
        input_text = input("Please enter your message: ")
        if input_text:   # if a string was entered
            more_input = False
    return input_text


def main():
    message = get_input()
    secret_message = translate(message)
    print('The secret message is: ', secret_message)


if __name__ == '__main__':
    main()
