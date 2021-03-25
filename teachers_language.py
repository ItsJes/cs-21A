# -----------------------------------------------------------------------------
# Name:        language
# Purpose:     Assignment 7 Solution
#
# Author:      Rula Khayrallah
# -----------------------------------------------------------------------------
"""
An infinite random sentence generator.

The generator function sentence_generator yields nonsensical sentences
of a given length, loosely modelled after some specified text file.
"""

import string
import random

def learn(filename):
    """
    Read a text file and build a dictionary to model its language and
    structure.  Case and punctuation are ignored.

    Parameter:
    filename (string) - name of the file to be read

    Returns:
    A tuple:
    The first word (str)
    learned_words (dictionary): each word is mapped to a list of all the words
                  that immediately follow it in the input file.
    """
    learned_words = {}
    previous = None
    first = None
    with open(filename, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            words = line.lower().split()
            words = [word.strip(string.punctuation) for word in words
                     if word.strip(string.punctuation)]
            for word in words:
                if previous:  # If this is not the very first word read
                    learned_words[previous].append(word)
                else:
                    first = word
                # if this is the first time we encounter this word
                if word not in learned_words:
                    learned_words[word] = []
                previous = word
    return first, learned_words

def sentence_generator(filename, length=10):
    """
    yield nonsensical sentences of a given length, loosely modelled
    after the text in the specified file.

    Parameters:
    filename (string): the file to imitate
    length (int): number of words in the generated sentence, default to 10.

    Yields:
    string:  a sentence of the specified length
    """
    random.seed(1)
    first, words = learn(filename)
    # sort the keys and save them to avoid sorting again with every sentence
    keys = sorted(words)

    while True:
        # start with a random word from the keys
        new_word = random.choice(keys)
        generated = [new_word]
        # get the remaining length - 1 words
        for count in range(length - 1):
            # If the list of words that follow word is non-empty
            if words[new_word]:
                new_word = random.choice(words[new_word])
            else:  # the list is empty, pick the first word
                new_word = first
            # add the word to the generated list
            generated.append(new_word)

        yield ' '.join(generated)
