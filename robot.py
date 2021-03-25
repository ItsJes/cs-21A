# -----------------------------------------------------------------------------
# Name:       robot
# Purpose:    class definition for robots
#
# Author:
# Date:
# -----------------------------------------------------------------------------

"""
Module to describe and control robot objects in a maze.
"""
import tkinter


class Robot(object):
    """
    Robot lost in a maze and a robot that dives underwater

    Arguments:
    list the arguments here (__init__'s arguments)
    name(string) robots name
    color(string) robot color
    row(int) row in maze
    column(int) column in maze

    Attributes:
    list ALL the attributes here (ALL the instance variables)
    name(string) robots name
    color(string) robot color
    row(int) row in maze
    column(int) column in maze
    """

    # class variable used by the show method
    unit_size = 60

    # Class variable describing the maze
    # False represents an obstacle, True represents open space
    maze = [[True, True, False, True, True, True, False, True, True, True],
            [True, True, False, True, True, True, False, True, True, True],
            [True, False, True, True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, False, False, False, False, True, True, True, True, True],
            [True, True, False, True, True, True, True, True, False, True],
            [True, False, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True]]

    maze_size = len(maze)
    # class variable to represent a full charge
    # A robot with a fully charged battery can take up to 20 steps
    full = 20

    def __init__(self,  name, color, row=0, column=0):
        self.name = name
        self.color = color
        self.row = row
        self.column = column
        self.battery = Robot.full

    def __str__(self):
        return self.name + ' is a ' + self.color + ' robot lost is the maze.'

    def __gt__(self, other):
        return self.battery > other.battery #  compares battery

    def recharge(self):
        """
        Recharges Battery
        """
        self.battery = Robot.full  # recharges battery
        return self

    def one_step_forward(self):
        """
        Moves a step forward in the row section
        :return: True if no obstruction, False if hit wall / obsticle
        """
        r = self.row; c = self.column
        if self.battery > 0 and r > 0:  # checks battery and low boundaries
            if Robot.maze[r-1][c]:  # checks maze boundaries
                self.row -= 1  # steps forward
                self.battery -= 1  # decreases battery
                return True
        return False

    def one_step_back(self):
        """
        Moves a step back in the row section
        :return: True if no obstruction, False if hit wall / obsticle
        """
        r = self.row; c = self.column
        if self.battery > 0 and r < Robot.maze_size - 1:
            if Robot.maze[r+1][c]:   # checks maze boundaries
                self.row += 1  # steps backwards
                self.battery -= 1  # decreases battery
                return True
        return False

    def one_step_right(self):
        """
        Moves a step right in the col section
        :return: True if no obstruction, False if hit wall / obsticle
        """
        r = self.row; c = self.column
        if self.battery > 0 and c < Robot.maze_size - 1:
            if Robot.maze[r][c+1]:  # checks maze boundaries
                self.column += 1  # steps right
                self.battery -= 1  # decreases battery
                return True
        return False

    def one_step_left(self):
        """
        Moves a step left in the col section
        :return: True if no obstruction, False if hit wall / obsticle
        """
        r = self.row; c = self.column
        if self.battery > 0 and c < Robot.maze_size - 1:
            if Robot.maze[r][c-1]:  # checks maze boundaries
                self.column -= 1  # steps light
                self.battery -= 1  # decreases battery
                return True
        return False

    def forward(self, steps):
        """
        Moves forward as many steps as possible
        :param: steps(int) - steps to move
        :return: True if no obstruction, False if hit wall / obsticle
        """
        for i in range(0, steps):
            if not self.one_step_forward():
                return False
        return True


    def backward(self, steps):
        """
        Moves back as many steps as possible
        :param: steps(int) - steps to move
        :return: True if no obstruction, False if hit wall / obsticle
        """
        for i in range(0, steps):
            if not self.one_step_back():
                return False
        return True

    def right(self, steps):
        """
        Moves right as many steps as possible
        :param: steps(int) - steps to move
        :return: True if no obstruction, False if hit wall / obsticle
        """
        for i in range(0, steps):
            if not self.one_step_right():
                return False
        return True

    def left(self, steps):
        """
        Moves left as many steps as possible
        :param: steps(int) - steps to move
        :return: True if no obstruction, False if hit wall / obsticle
        """
        for i in range(0, steps):
            if not self.one_step_left():
                return False
        return True

    # The method below has been written for you
    # You can use it when testing your class

    def show(self):
        """
        Draw a graphical representation of the robot in the maze.

        The robot's position and color are shown.
        The color is assumed to be one of the colors recognized by tkinter
        (https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm)
        If the robot's battery is empty, the robot is shown in a
        horizontal position. Otherwise the robot is shown in an upright
        position.
        The obstacles in the maze are shown in red.

        Parameter: None
        Return: None
        """
        root = tkinter.Tk()
        root.title(self.name + ' in the Maze')
        canvas = tkinter.Canvas(root, background='light green',
                                width=self.unit_size * self.maze_size,
                                height=self.unit_size * self.maze_size)
        canvas.grid()

        # draw a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size / 20
            eye_y = upper_y + self.unit_size / 10

        else: # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y - 3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill=self.color)
        # draw the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill='black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill='black')
        # draw the obstacles in the maze
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                if not self.maze[row][col]:
                    canvas.create_rectangle(col * self.unit_size,
                                            row * self.unit_size,
                                            (col + 1) * self.unit_size,
                                            (row + 1) * self.unit_size,
                                            fill='red')
        for row in range(self.maze_size):
            canvas.create_line(0,
                               row * self.unit_size,
                               self.maze_size * self.unit_size,
                               row * self.unit_size)
        for col in range(self.maze_size):
            canvas.create_line(col * self.unit_size,
                               0,
                               col * self.unit_size,
                               self.maze_size * self.unit_size)
        root.mainloop()

class UnderwaterRobot(Robot):
    def __init__(self, name, color, depth=0, row=0, column=0):
        super(self.__class__, self).__init__(name, color, row, column)
        self.depth = depth

    def __str__(self):
        return self.name + ' is a ' + self.color + ' robot diving underwater.'

    def dive(self, distance):
        """
        Dives a certain number of units down
        :param: distance(int) - steps to dive
        """
        self.depth += distance
