# -----------------------------------------------------------------------------
# Name:        Grader
# Purpose:     Assignment 2
#
# Author:
# Date:        04/16/2017
# -----------------------------------------------------------------------------
"""
Average Grade Calculator

This calculates the overall grade for a course
First asks for the grades.
Then calculates the average and rounds to the nearest one decimal place.
Also drops lowest score if more then four grades were entered
Ignores grades below 0 and over 100
Gives grade based on the average
Lets you know what scores were used to calculate overall grade

and a more detailed description here.
"""
# Enter your code here
grade_list = []  # holds grades entered

get_grades = True  # used to set while loop true
loop_end = 'end'  # used to exit loop
min_num_drop = 4  # constant for checking to see if grades are 4 or more

while get_grades:
    user_input = input('Please enter a grade: ')  # ask user for grades
    if user_input != loop_end:
       number = float(user_input)  # turns string numbers into floats
       if number >= 0 and number <= 100:  # makes sure grades are between 0-100
           grade_list.append(number)  # stores grades in grade_list
    elif user_input == loop_end:  # checks if user input is end
        get_grades = False  # if user input is end. loop breaks

        length = len(grade_list)  # stores the length of grades
        if length >= min_num_drop:  # checks to see if length if more then 4
            min_grade = min(grade_list)  # gets lowest grade
            grade_list.remove(min_grade)  # removes lowest grade
            print('Lowest Grade Dropped: ', min_grade)  # give grade dropped

        total = sum(grade_list)  # adds the grades up
        new_len = len(grade_list)  # get new length if one was dropped
        average_grade = (total/new_len) # gets overall score

        average_grade = round(average_grade, 1)  # rounds to nearest 1 decimal
        print('Coure Average: ', average_grade)  # prints average grade
        if average_grade >= 90:
            print('Letter Grade: A')  # gets A over 90
        elif average_grade >= 80:
            print('Letter Grade: B')  # gets B over 80 - 89.9
        elif average_grade >= 70:
            print('Letter Grade: C')  # gets C over 70 - 79.9
        elif average_grade >= 60:
            print('Letter Grade: D')  # gets D over 60 - 69.9
        else:
            print('Letter Grade: F') # gets F 59.9 and below
        print('Based off the following grades: ')

        for grades in grade_list:
            print(grades)  # prints grades that average was based off





