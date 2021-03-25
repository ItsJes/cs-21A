# -----------------------------------------------------------------------------
# Name:        robot
# Purpose:     class definition for robots in a square maze
#
# Author:      Rula Khayrallah
# -----------------------------------------------------------------------------

"""
Module to describe and control Robot objects in a square maze.
"""
import tkinter


class Robot(object):

    """
    Represent a robot in a maze

    Arguments:
    name (string): the robot's name
    color (string): the robot's color - in order to be shown, it has to be
                    a valid color
    row: (integer):  the initial row position of the robot in the maze grid -
        defaults to 0
    column (integer) the initial column position of the robot in the maze -
        defaults to 0

    Attributes:
    name (string): the robot's name
    color (string): the robot's color
    row: (integer):  the row position of the robot in the maze
    column (integer): the column position of the robot in the maze
    battery (integer):  current battery charge - initialized to the full
       class variable.
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
    # class variable to represent a full battery
    # A robot with a fully charged battery can take up to 20 steps
    full = 20

    def __init__(self,  name, color, row=0, column=0):
        self.name = name
        self.color = color
        if self.available(row, column):
            self.row = row
            self.column = column
        else:
            self.row, self.column = self.closest(row, column)
        self.battery = self.full

    def __str__(self):
        return '{} is a {} robot lost in the maze.'.format(self.name,
                                                           self.color)
    def __gt__(self, other):
        return self.battery > other.battery

    @classmethod
    def available(cls, row, column):
        """
        Determine whether the corresponding position is available to a robot.
        To be available, the position must be within the boundaries
        of the maze and must be free of obstacles.
        Parameters:
        row (int) - row denoting the given position
        column (int) - column  denoting the given position

        Return:
        (Boolean): True if the position is available to a robot
                    False otherwise
        """
        return (row in range(cls.maze_size) and
                column in range(cls.maze_size) and
                cls.maze[row][column])




    def recharge(self):
        """
        Recharge the robot's battery to full
        Parameter: None
        Return (Robot): the updated robot object
        """
        self.battery = self.full
        return self

    def one_step_forward(self):
        """
        Take the robot one step forward within the boundaries
        of the maze if there are no obstacles.
        Parameter: None
        Return:  None
        """
        if self.battery and self.available(self.row + 1, self.column):
            self.row += 1
            self.battery -= 1

    def one_step_back(self):
        """
        Take the robot one step back within the boundaries
        of the maze if there are no obstacles.
        Parameter: None
        Return:  None
        """
        if self.battery and self.available(self.row - 1, self.column):
                self.row -= 1
                self.battery -= 1


    def one_step_right(self):
        """
        Take the robot one step to the right within the boundaries
        of the maze if there are no obstacles.
        Parameter: None
        Return:  None
        """
        if self.battery and self.available(self.row, self.column + 1):
                self.column += 1
                self.battery -= 1

    def one_step_left(self):
        """
        Take the robot one step back within the boundaries
        of the maze if there are no obstacles.
        Parameter: None
        Return:  None
        """
        if self.battery and self.available(self.row, self.column - 1):
                self.column -= 1
                self.battery -= 1

    def forward(self, steps):
        """
        Move the robot as far as possible up to the specified number
        of steps forward.
        Parameter:
        steps (int): number of steps to move the robot
        Return:  None
        """
        for each_step in range(steps):
            self.one_step_forward()

    def backward(self, steps):
        """
        Move the robot as far as possible up to the specified number
        of steps back.
        Parameter:
        steps (int): number of steps to move the robot
        Return:  None
        """
        for each_step in range(steps):
            self.one_step_back()

    def right(self, steps):
        """
        Move the robot as far as possible up to the specified number
        of steps to the right.
        Parameter:
        steps (int): number of steps to move the robot
        Return:  None
        """
        for each_step in range(steps):
            self.one_step_right()

    def left(self, steps):
        """
        Move the robot as far as possible up to the specified number
        of steps to the left.
        Parameter:
        steps (int): number of steps to move the robot
        Return:  None
        """
        for each_step in range(steps):
            self.one_step_left()

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
        root.title (self.name + ' in the Maze')
        canvas= tkinter.Canvas(root, background = 'light green',
                               width = self.unit_size * self.maze_size,
                               height = self.unit_size * self.maze_size)
        canvas.grid()

        # draw a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size /  20
            eye_y = upper_y + self.unit_size / 10

        else: # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y -  3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill = self.color)
        # draw the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill = 'black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill = 'black')
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
                               self.maze_size * self.unit_size )
        root.mainloop()

    @classmethod
    def closest(cls, ideal_row, ideal_column):
        """
        Find the closest available location to a given position
        Parameters:
        ideal_row (int) - row denoting the ideal position
        ideal_column (int) - column  denoting the ideal position

        Return:
        (tuple): (row, column) corresponding to the closest available position
        """
        # find all the available positions
        available_locations = set()
        for each_row in range(cls.maze_size):
            for each_col in range(cls.maze_size):
                if cls.maze[each_row][each_col]:
                     available_locations.add((each_row, each_col))
        if available_locations:
            return min(available_locations,
                   key=lambda position: (position[0] - ideal_row)**2 +
                                        (position[1] - ideal_column)**2 )
        else:
            print('Maze is full of obstacles')
            return None, None

class UnderwaterRobot(Robot):

    """
    Represent an underwater robot in a maze

    Super class: Robot

    Arguments:
    name (string): the robot's name
    color (string): the robot's color - in order to be shown, it has to be
                    a valid color
    depth (integer) the depth of the robot underwater
    row: (integer):  the initial row position of the robot in the maze grid -
        defaults to 0
    column (integer) the initial column position of the robot in the maze -
        defaults to 0

    Attributes:
    name (string): the robot's name
    color (string): the robot's color
    depth (integer): the depth of the robot underwater
    row: (integer):  the row position of the robot in the maze grid
    column (integer): the column position of the robot in the maze
    battery (integer):  current battery charge - initialized to the full
       class variable.
    """

    def __init__(self,  name, color, depth, row=0, column=0):
        self.depth = depth
        super().__init__(name, color, row, column)

    def __str__(self):
        return self.name + ' is a ' + self.color + ' robot diving under water.'

    def dive(self, distance):
        """
        Move the robot down underwater.
        Parameter:
        distance (int): number of units to add to the depth of the robot
        Return:  None
        """
        self.depth += distance
