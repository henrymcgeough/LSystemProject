#!/usr/bin/env python

# L-Systems Turtle Graphics System

# By Henry McGeough

# Choose L-System config file from menu
# Read config file
# implement turtle L Systems primatives
# implement rule expansion code
# implement one rule L System - a,b,c are one rule
# implement two rule L System - d to h are all two rule
# Step through successive iterations using + Hotkey
# Convert L-System parameters into trutle Graphics

import turtle  # Turtle Graphics Library
import configparser  # code for reading config file

# L Systems - Class
class Lsystem:
    def __init__(self, n, var, const, axiom, rule1, rule2, angle):
        self.n = n          # number of iterations to use to draw image
        self.var = var      # Variables used to build string
        self.const = const  # Constants used to build string
        self.axiom = axiom  # starting string
        self.rule1 = rule1  # first rule
        self.rule2 = rule2  # second rule, will be null if there is only one rule
        self.angle = angle  # angle used for drawing
        self.length = 25    # length of line to draw
        self.recursion = axiom # input string used for draw each iteration
        self.production = axiom # output string used to draw each iteration
        self.stack = [0] # stack
        # init turtle graphics - we want it pointing up or north
        # self.ts = turtle.getscreen()
        turtle.clearscreen()
        turtle.reset()
        # turtle.setheading(90)
        # turtle.bgcolor("blue")
        # turtle.setpostion(0, 0)
    # Turtle Graphics used by L System

    def clear(self):
        # clearscreen before iteration
        turtle.clearscreen()
        turtle.reset()
        # not sure about this yet
        turtle.penup()
        turtle.setposition(0, -350)
        turtle.setheading(90)
        turtle.pendown()
    # F is variable for move forward and draw a line
    # fd : Turtle - move forward
    def fd(self):
        # print ('fd ')
        turtle.forward(self.length) # may need to change this value
    # X and Y are variables for move forward
    # mv : Turtle - move forward
    def mv(self):
        # print ('mv ')
        turtle.penup()
        turtle.forward(self.length)
        turtle.pendown()
    # - is constant for turn right, it uses angle from config file
    # rt : Turtle - Right Turn
    def rt(self):
        # print ('lt %d ' % self.angle)
        turtle.right(self.angle)
    # + is constant for turn right, it uses angle from config file
    # lt : Turtle - Left Turn
    def lt(self):
        # print ('lt %d ' % self.angle)
        turtle.left(self.angle)
    # start a branch
    def branch(self):
        # print (' [ ')
        x, y = turtle.position()
        a = turtle.heading()
        # self.push(x, y, a)
        # push 3 items on stack
        # print("[ x:%s y:%s a:%d " % (x, y, a))
        self.stack.append(x)
        self.stack.append(y)
        self.stack.append(a)
    # complete a branch
    def complete(self):
        # print (' ] ')
        # x, y, a = self.pop()
        # return 3 items from stack
        a = self.stack.pop()
        y = self.stack.pop()
        x = self.stack.pop()
        # print(" x:%s y:%s a:%d ]" % (x, y, a))
        turtle.setposition(x, y)
        turtle.setheading(a)
    def iterate(self, n):
        # iterate through recursion string
        for i in range(n):
            if n == 0:
                # This first iteration so copy axion into recursion string
                self.production = self.axiom

            else:
                # build new production string that will be used to draw
                # new turtle graphic iteration
                self.production = ""
                # print(r'rec: %d %s' % (len(self.recursion), self.recursion))

                # get current iteration string being used in recursion
                # step through string and apple rules
                for j in range(0, len(self.recursion)):
                    rule = self.check_rule(self.recursion[j])
                    # print(r'rule: %d %d %s' % (i, j, rule))
                    if rule:
                        # Rule found, apply rule to production string
                        # self.apply_rule(rule, production[j])
                        self.production += rule[2:]
                    else:
                        # just copy character without substitution
                        self.production += self.recursion[j]
        # update recursioon string for next iteration
        self.recursion = self.production
        # return production string for turtle graphics drawing
        return self.production
    # Draw World - draw production string after iteration using turtle graphics
    def draw_world(self):
        for i in range(len(self.production)):
            c = self.production[i]
            if c == "F":
                # Draw line
                self.fd()
            # G added for sierpinski
            elif c == "G":
                # Draw line
                self.fd()
            elif c == "X":
                # move line
                self.mv()
            elif c == "Y":
                # move line
                self.mv()
            elif c == "+":
                # left turn
                self.lt()
            elif c == "-":
                # right turn
                self.rt()
            elif c == "[":
                # branch - save state on stack
                self.branch()
            elif c == "]":
                # complete - get state from stack
                self.complete()
    # Print Text of L System with n iterations
    def text(self, n):
        for i in range(n):
            self.iterate(i)
            print(r'n = %d : %s' % (i, self.production))
    # Draw Turtle Graphic of L System with n iterations
    def draw(self, n):
        for i in range(n):
            self.clear()
            if i != 0:
                self.length = 100 / i
            self.iterate(i)
            self.draw_world()
            print(r'n = %d : %s' % (i, self.production))
            # print(r'n = %d' % i)
        # self.draw_world()
   # Check if either rules apply
    def check_rule(self, var):
        if var == self.rule1[0]:
            # Rule 1 applies here
            return self.rule1
        elif len(self.rule2) > 0:
            if var == self.rule2[0]:
                return self.rule2
        else:
            return

# Select Recursion for list

# Text Menu for L System Tree selection
# menu = ["L Systems - pick a Tree",
#        "1. A tree",
#        "2. B Tree",
#        "3. C Tree",
#        "4. D Tree",
#        "5. E Tree",
#        "6. F Tree",
#        "7. Koch",
#        "8. Hilbert",
#        "9. Quit"]

# Display Text Menu
def menulist():
    #  while (target in list):
    # for i in range(9):
    #    print(menu[i])

    # Menu Text
    print(r'L Systems - pick a Tree')
    print(r'1. A Tree')
    print(r'2. B Tree')
    print(r'3. C Tree')
    print(r'4. D Tree')
    print(r'5. E Tree')
    print(r'6. F Tree')
    print(r'7. Koch')
    print(r'8. Seipinski Triangle')
    print(r'9. Quit')

    target = input("Pick an item from the menu:")
    config = configparser.RawConfigParser()

    # Check which option was selected
    # and load the config file
    if target == "0":
        config.read('test.ini')
    elif target == "1":
        config.read('a.ini')
    elif target == "2":
        config.read('b.ini')
    elif target == "3":
        config.read('c.ini')
    elif target == "4":
        config.read('d.ini')
    elif target == "5":
        config.read('e.ini')
    elif target == "6":
        config.read('f.ini')
    elif target == "7":
        config.read('g.ini')
    elif target == "8":
        config.read('h.ini')
    elif target == "9":
        print("good bye")
        quit()

    # Read in information from Tree config file
    ls_n = config.getint('Section1', 'n')
    ls_var = config.get('Section1', 'var')
    ls_const = config.get('Section1', 'const')
    ls_axiom = config.get('Section1', 'axiom')
    ls_rule1 = config.get('Section1', 'rule1')
    ls_rule2 = config.get('Section1', 'rule2')
    ls_angle = config.getfloat('Section1', 'angle')

    ls = Lsystem(ls_n, ls_var, ls_const, ls_axiom, ls_rule1, ls_rule2, ls_angle)
    # print(ls_n, ls_var + ls_const + ls_axiom + ls_rule1 + ls_rule2 + " %d" % ls_angle)

    if ls.rule2:
        print ('This is a Rule 2 based L System')
    else:
        print ('This is a Rule 1 based L System')

    if target == '0':
        # This is Text Only Test
        ls.text(8)
    else:
        ls.draw(ls_n)

#main loop
def run_lsystem():
    #esc = menulist()
    forever = 1

    while forever:
        menulist()

run_lsystem()

# menulist()
