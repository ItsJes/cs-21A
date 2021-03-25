# -----------------------------------------------------------------------------
# Name:        spam
# Purpose:     Assignment 4 solution
#
# Author:      Rula Khayrallah
# -----------------------------------------------------------------------------
"""
Label a message as spam or ham

Compute a spam indicator which is the ratio of spam words over
all unique words used in the message.  If this indicator
is greater than a spam threshold (0.1), the
message is labeled as spam.  Otherwise it is labeled as ham.
"""
import string  # needed for the optional challenge

SPAM_WORDS = {'opportunity', 'inheritance', 'money', 'rich', 'dictator',
              'discount', 'save', 'free', 'offer', 'credit',
              'loan', 'winner', 'warranty', 'lifetime', 'medicine',
              'claim', 'now', 'urgent', 'expire', 'top',
              'plan', 'prize', 'congratulations', 'help', 'widow'}

SPAM_THRESHOLD = 0.10


def spam_indicator(text):
    """
    Compute the spam indicator of the given text.

    Parameter:
    text (string): string possibly containing several words separated
        by one or more space characters
    Returns:
    float - ratio of spam words to unique words rounded to 2 decimals
    """
    lower_text = text.lower()  # Convert input to lower case
    # Replace punctuation characters with a space character - optional
    for char in string.punctuation:
        lower_text = lower_text.replace(char, ' ')

    words = set(lower_text.split())  # Get the set of the words in the text
    spam_count = len(words & SPAM_WORDS)  # Spam words are in both sets
    if words:
        result = round(spam_count / len(words), 2)
    else:  # An empty message is considered HAM
        result = 0
    return result


def classify(indicator):
    """
    Print a classification based on the given indicator and the SPAM_THRESHOLD.

    Parameter:
    indicator - float - spam indicator
    Returns:
    None
    """

    if indicator > SPAM_THRESHOLD:
        print('This message is: SPAM')
    else:
        print(('This message is: HAM'))


def get_input():
    """
    Prompt the user for input and return the input

    Parameter: None
    Returns:
    string - the user input
    """
    user_input = input("Please enter your message: ")
    return user_input


def main():
    message = get_input()
    ratio = spam_indicator(message)
    print('SPAM indicator: ', ratio)
    classify(ratio)


if __name__ == '__main__':
    main()
