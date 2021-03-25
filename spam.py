# -----------------------------------------------------------------------------
# Name:        spam
# Purpose:     Assignment 4
#
# Author:      Jessica Sendejo
# Date:        May 4, 2017
# -----------------------------------------------------------------------------
"""
Checks a list of SPAM WORDS to see if the message is spam.

Ask user for a message. Checks the words in the message and uses intersection
on a tuple of spam words to see decide whether the message is SPAM or HAM(not
spam) Anything .10 or less is HAM anything above that is spam. Using a ratio
to determine if spam or not.
"""
SPAM_WORDS = {'opportunity', 'inheritance', 'money', 'rich', 'dictator',
              'discount', 'save', 'free', 'offer', 'credit',
              'loan', 'winner', 'warranty', 'lifetime', 'medicine',
              'claim', 'now', 'urgent', 'expire', 'top',
              'plan', 'prize', 'congratulations', 'help', 'widow'}


def spam_indicator(text):
    """
    Checks user input with the words from SPAM_WORDS. Gets the length
    of words found and uses it to compute the ratio. If user input
    has 0 function returns 0.0 otherwise computes the ratio and returns
    it rounded to the nearest 2 decimals. 
    """
    # This function returns the spam indicator rounded to two decimals

    list_of_words = text.split()  # Spits under input so a list
    spam_count = len(SPAM_WORDS.intersection(set(list_of_words)))  # gets len

    words_len = len(set(list_of_words))  # Gets the length of user input

    if words_len == 0:  # Checks to make sure user input isn't 0
        return 0.0      # Returns 0.0 if 0

    ratio = spam_count / words_len  # Ratio to compute spam
    ratio = round(ratio, 2)  # Rounds ratio to two decimals
    return ratio  # Returns ratio


def classify(indicator):
    """
    Calls spam_indicator to compare ratio amount with the constant 
    SPAM_THRESHOLD to determine if it's SPAM OR HAM(not spam)
    """
    # This function prints the spam classification

    SPAM_THRESHOLD = .10  # Constant to determine if spam or not

    if spam_indicator(indicator) <= SPAM_THRESHOLD:  # Less then .1 it's HAM
        is_it_spam = 'HAM'
    else:  # If greater the SPAM_THRESHOLD. It's SPAM
        is_it_spam = 'SPAM'

    return is_it_spam  # Returns SPAM or HAM


def get_input():
    """
    Gets message from user. converts it to lower case to compare
    all words with SPAM_WORDS. 
    """
    # Prompt the user for input and return the input

    get_message = True

    while get_message:
        user_input = input('Please enter your message: ')  # Gets user input
        input_lowercase = user_input.lower()  # Converts to lowercase
        words = input_lowercase.split()  # Turns to list
        number_of_words = len(words)  # Gets length
        if number_of_words > 0:  # Checks to make sure input isn't empty
            get_message = False
            return input_lowercase


def main():
    # Get the user input and save it in a variable
    # Call spam_indicator to compute the spam indicator and save it
    # Print the spam_indicator
    # Call classify to print the classification

    user_input = get_input()  # Save input from get input
    the_indicator = spam_indicator(user_input)  # Saves ratio
    print('SPAM indicator ', the_indicator)  # Prints ratio
    print('This message is ', classify(user_input))  # prints if spam or not


if __name__ == '__main__':
    main()
