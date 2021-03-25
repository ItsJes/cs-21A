# -----------------------------------------------------------------------------
# Name:    grader
# Purpose: Assignment # 2 solution
#
# Author:  Rula Khayrallah
#
# Copyright © Rula Khayrallah, 2014-2017
# -----------------------------------------------------------------------------
"""
Calculate the letter grade earned in a given course.

Prompt the user to enter the grades earned on different components of the
course.  Valid grades range from 0 to 100.
If 4 or more grades are entered, drop the lowest grade.
Calculate the average assuming equal weights.
The average is rounded to the nearest decimal.
The letter grade is determined based on the following scale:
90 and above: A
80 - 89.9:  B
70 - 79.9: C
60 - 69.9: D
below 60: F
"""
MIN_GRADES_REQ_FOR_DROP = 4  # Minimum grades required for lowest to be dropped
END_OF_INPUT = 'end'  # End of user input marker
grades = []  # Keep the grades entered in a list
more_grades = True
while more_grades:  # prompt for input repeatedly
    user_input = input('Please enter a grade: ')
    if user_input == END_OF_INPUT:
        more_grades = False
    else:
        grade = float(user_input)
        # If the grade is outside the valid range, ignore it
        if 0 <= grade <= 100:
            grades.append(grade)  # Add the grade to the list
        else:
            print('Invalid grade entered:', grade)

if grades:  # If the user entered at least one grade
    lowest = min(grades)
    if len(grades) >= MIN_GRADES_REQ_FOR_DROP:  # If there are enough grades
        grades.remove(lowest)  # Remove the lowest
        print('The lowest grade dropped:', lowest)

    average = sum(grades) / len(grades)  # Average of grades left in the list
    average = round(average, 1)
    print('Course Average', average)

    # compute the letter grade
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    print('Letter Grade:', letter_grade)

    print('Based on the following grades: ')
    for each_grade in grades:
        print(each_grade)
