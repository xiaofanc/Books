"""
Recursion:
visualize a tree

"""

import turtle

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20) # turn right 20 degree
        tree(branchLen-15,t)
        t.left(40)  # turn left 40 degree to the left tree
        tree(branchLen-15,t)
        t.right(20) # left tree: turn 20 degree
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(80,t)
    myWin.exitonclick()

main()