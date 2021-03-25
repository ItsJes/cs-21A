# -----------------------------------------------------------------------------
# Name:        wordstats
# Purpose:     compute some language statistics -  Solution
#
# Author:      Rula Khayrallah
# -----------------------------------------------------------------------------
"""
Compute some language statistics based on the contents of a file

Prompt the user to enter a file name.
Print out some language statistics based on the content of the file:
- the five most common words used in the file
- the longest word used in the file
- the word count of all the words in the file, sorted alphabetically
    this last output is written to a file in the current working directory
    with the name 'out.txt'
- Produce a word cloud based on the file.
The program ignores capitalization and leading and trailing punctuation
characters and numbers in words.
"""
import string
# The following imports are needed for the draw_cloud function.
import tkinter
import tkinter.font
import random


# The draw_cloud function is only needed for the optional part:
# to generate a word cloud.
# You don't need to change it.
def draw_cloud(input_count, min_length=0):
    """
    Generate a word cloud based on the input count dictionary specified.

    Parameters:
    input_count (dict): represents words and their corresponding counts.
    min_length (int):  optional - defaults to 0.
         minimum length of the words that will appear
         in the cloud representation.
    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """
    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
        word: input_count[word] for word in input_count
        if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame = tkinter.Frame(root)
    frame.grid()
    my_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[0:20]:
        color = '#' + str(hex(random.randint(256, 4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word] * ratio))
        label = tkinter.Label(frame, text=word, font=word_font, fg=color)
        label.grid(row=my_row % 5, column=my_row // 5)
        my_row += 1
    root.mainloop()


def count_words(filename):
    """
    Count the words in the file specified ignoring capitalization and
    leading and trailing punctuation characters and numbers.

    Parameter:  filename (string) name of the input file
    Return: a dictionary with items of the form word: count
    """
    count_dict={}  # Initialize the dictionary
    with open(filename, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            line = line.lower()
            for word in line.split():
                # take out leading and trailing punctuation characters
                word = word.strip(string.punctuation + string.digits)
                if word:   # if there is anything left
                    if word in count_dict:  # we have seen this word before
                        count_dict[word] += 1
                    else:                 # this is a new word
                        count_dict[word] = 1
    return count_dict


def alpha_output(input_count):
    """
    Write the words alphabetically with their count
    to a file 'out.txt' in the current working directory.

    Parameter:
    input_count - a dictionary with items of the form word: count
    """
    with open('out.txt', 'w', encoding='utf-8') as output_file:
        alpha_list = sorted(input_count)
        for word in alpha_list[0:-1]:
            output_file.write('{}: {}\n'.format(word, input_count[word]))
        # don't print new line after last word
        last_word = alpha_list[-1]
        output_file.write('{}: {}'.format(last_word, input_count[last_word]))


def most_common(input_count, n):
    """
    return a list containing the n most common words in the given input
    dictionary.

    Parameters:
    input_count - a dictionary with items of the form word: count
    n (int) - the number of most common words to be returned
    Return: a list containing the n most common words.
    """
    sorted_by_count = sorted(input_count, key=input_count.get, reverse=True)
    return sorted_by_count[0:n]  # return the top most n words only


def longest_word(input_count):
    """
    Return one of the longest words in the dictionary

    Parameter:
    input_count - a dictionary with items of the form word: count
    Return: a string - one of the longest words in the given dictionary
    """
    return max(input_count, key=len)


def report(input_count):
    """
    Generate some statistics based on the given dictionary

    Parameter:
    input_count - a dictionary with items of the form word: count
    Return: None
    """
    print('The longest word is: ', longest_word(input_count))
    print('The 5 most common words are: ')
    for word in most_common(input_count, 5):
        print('{}: {}'.format(word, input_count[word]))
    alpha_output(input_count)


def main():
    # get the input filename and save it in a variable
    filename = input('Please enter the input file name: ')
    # call count_words to build the dictionary for the given file
    # save the dictionary in the variable word_count
    word_count = count_words(filename)
    # call report to report on the contents of the dictionary
    report(word_count)
    # If you want to generate a word cloud, uncomment the line below.
    draw_cloud(word_count)

if __name__ == '__main__':
    main()