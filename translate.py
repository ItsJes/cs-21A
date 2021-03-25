# -----------------------------------------------------------------------------
# Name:        translate
# Purpose:     assignment # 3
#
# Author:      Jessica Sendejo
# Date:        April 27, 2017
# -----------------------------------------------------------------------------
"""
Translates words to a secret message

Asks user for input. Checks to see if words start with a vowel or 
consonant. If vowel adds zus to end. If consonant moves first letter to 
the end then adds ix. 
"""


def starts_with_vowel(word):
    """
    Checks to see if word starts with vowel or consonant.
    If starts with vowel returns true 
    if starts with consonant returns false
    """
    vowels = 'aeiou'  # Vowels
    first = word[0]  # Used to get first letter

    if first.lower() in vowels:  # Used to get if first word is a vowel
        return True  # Returns true if starts with a vowel
    else:
        return False  # Returns false if starts with consonant


def encode(word):
    """
    Calls starts_with_vowel and checks to see if it started with 
    a vowel or consonant to decide which pattern to use to 
    make translated word. Then returns it.
    """

    vowels = 'zus'
    consonant = 'ix'

    if starts_with_vowel(word[0]):  # Calls start with vowel check first letter
        secret_word = str(word) + vowels  # If vowel adds zus
        return secret_word  # Returns encoded word
    else:  # If consonant adds ix
        secret_word = str(word[1:]) + str(word[0]) + consonant
        return secret_word


def translate(text):
    """
    Translates a whole sentence to coded form.
    splits the sentence into a list. Goes through 
    the list then calls encode to encode the words.
    Puts encoded words into a new list then joins
    them into a sentence and returns it.
    """

    sentence = []  # Used to store encoded words

    words = text.split()  # Splits sentence to list
    for word in words:  # Loop to go through list
        sentence.append(encode(word))  # Puts encoded word into sentence

    new_sentence = ' '.join(sentence)  # Turns list back to sentence
    return new_sentence


def get_input():
    """
    Gets input from the user. Gets the length of the user input
    and checks to make sure it's not empty. If not empty returns
    input.
    """

    get_word = True  # Used to set while loop true

    while get_word:
        user_input = input('Please enter your message: ')  # Ask user for input
        words = user_input.split()
        number_of_words = len(words)  # Gets length
        if number_of_words > 0:  # Checks if input is greater then 0]
            get_word = False
            return user_input


def main():
    # get input from the user and save it in a variable
    # translate the saved input by calling translate - save result
    # print the result

    user_input = get_input()  # Save input from get input
    coded_sentence = translate(user_input)  # Saves translated input
    print(user_input)  # Prints inputted text
    print(coded_sentence)  # Prints translated word

if __name__ == '__main__':
    main()