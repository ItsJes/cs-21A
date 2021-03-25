# -----------------------------------------------------------------------------
# Name:        language
# Purpose:     Assignment 7
#
# Author:      Jessica Sendejo
# Date:        June 4, 2017
# -----------------------------------------------------------------------------
"""
Creates a random sentence from a text file

"""
import random
# Enter your imports here
import string

def learn(filename):
    """
    Creates a dict from text file given

    Parameter:
    filename: text file

    returns:
    first word in text file and a dict with keys
    """
    word_dict = {}  # Create empty dictionary
    first = None
    prev = None
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            list_words = line.lower().split()
            text = []
            for word in list_words:
                # take out leading and trailing punctuation characters
                words = word.strip(string.punctuation + string.digits)
                word_len = len(words)
                if word_len >= 1:
                    text.append(words)

                    if first is None:
                        # Get the first word in the text file
                        first = text[0]
            # iterate over text
            if prev:
                text.insert(0, prev)
            for counter, word in enumerate(text):
                if word not in word_dict:
                    word_dict[word] = list()
                if counter < (len(text) - 1):
                    following = counter + 1
                    word_dict[word].append(text[following])
            prev = text[-1]
        return first, word_dict     # return a tuple

def sentence_generator(filename, length=10):
    """
    Makes a random sentence from dict made from learn

    parameter:
    filename: text file
    length: length of sentence defaulted to 10

    """
    random.seed(1)  # Set the seed for the random generator - do not remove
    # Enter your code here

    ret = learn(filename)      # stores learn function in var
    sort = sorted(ret[1])     # Sort the dictionary
    curr = random.choice(sort)   # selects first word
    sent = [curr]
    sent_len = len(sent)    # length
    end_loop = False

    while not end_loop:  # infinite loop
        curr = sent[-1]  # Word to start with
        sent_len += 1
        get_word = next_word(ret[1][curr], ret[0])

        sent.append(get_word)  # puts words in sent
        if sent_len == length:  # checks length
            sentence = ' '.join(sent)  # joins sentence
            return sentence


def next_word(selection, default):
    """
    gets next word

    Parameter:
    selection: gets word from learn
    default: sets default word

    Return:
        returns either default word or next random word
    """

    if len(selection) != 0:
        return random.choice(selection)
    else:
        return default

