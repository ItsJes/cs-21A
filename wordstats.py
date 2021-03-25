# -----------------------------------------------------------------------------
# Name:        wordstats
# Purpose:     Assignment 5
#
# Author:      Jessica Sendejo
# Date:        May 13,2017
# -----------------------------------------------------------------------------
"""
Opens a large file. 

This opens a large file. It is able to find the largest word,
find the 5 most common words, and give count to how many times
they are use.
"""
import string
import operator
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


# Enter your own helper function definitions here

def filter_word(word):
    """     Gets only alphabet char
         parameter: word             """
    # Returns word filtered to just alphabet chars
    word = word.lower()

    if(len(word) < 1):
        return word  # returns if word is 0

    while(not word[0].isalpha()):  # while first word not a alphabet char
        word = word[1:]   # stores from index 1 onward
        if(len(word) < 1):  # check for len returns in less then 1
            return word

    while(not word[len(word) - 1].isalpha()):  # checks last for alphabet char
        word = word[:-1]  # stores alphabet chars
        if(len(word) < 1):  # check for len returns if less then 1
            return word

    return word


def count_words(filename):
    """     Counts words in file
         parameter: filename
         returns: a dic of the file    """
    # build and return the dictionary for the given filename

    with open(filename, 'r', encoding='utf-8') as file:  # opens file
      dict = {}  # Stores word in dic
      for line in file.readlines():  # reads by lines
        for word in line.split():  # splits so list
            word = filter_word(word)  # calls filter_word
            if(word == ''):
                continue
            if(word in dict):
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1
    return dict


def report(word_dict):
    """     Finds the longest word, finds the 5
         most common words and counts how often they are use 
          parameter: word_dict                                 """
    # report on various statistics based on the given word count dictionary

    with open('out.txt', 'w', encoding='utf-8') as file:
     firstLine = True
     for word in sorted(word_dict):  # sorts dict
        if(not firstLine):
            file.write('\n')  # new line
        firstLine = False
        file.write(word + ': ' + str(word_dict[word]))  # writes to file

     longestWord = ''
     for word in word_dict:
         if(len(word) > len(longestWord)):  # looks for longest word
             longestWord = word  # stores longest word in longestWord
    print('The longest word is: ' + longestWord)  # prints longest word

    print('The 5 most common words are:')
    print_count = 0
    for word in sorted(word_dict, key = word_dict.get, reverse = True):  # sort
        print(word + ': ' + str(word_dict[word]) )
        print_count = print_count + 1  # increment word count by 1
        if(print_count >= 5):
            break

def main():
    # get the input filename and save it in a variable
    filename = input('Enter filename: ')
    # call count_words to build the dictionary for the given file
    # save the dictionary in the variable word_count
    word_count = count_words(filename)
    # call report to report on the contents of the dictionary word_count
    report(word_count)

    # If you want to generate a word cloud, uncomment the line below.
    # draw_cloud(word_count)


if __name__ == '__main__':
    main()
