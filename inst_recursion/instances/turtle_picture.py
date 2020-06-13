# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/23 17:37
# @FileName : turtle_picture.py
# @SoftWare : PyCharm


import turtle


def init_turtle(*args, pen_color='red', pen_size=4):
    t = turtle.Turtle()
    t.pencolor(pen_color)
    t.pensize(pen_size)
    return t


def draw_spiral(t, line_len):
    if line_len > 0:
        t.forward(line_len)
        t.right(90)
        draw_spiral(t, line_len - 5)


def draw_tree(branch_len, right_deg=20, left_deg=40):
    if branch_len > 5:
        t2.forward(branch_len)

        t2.right(right_deg)
        draw_tree(branch_len - 15)

        t2.left(left_deg)
        draw_tree(branch_len - 15)

        t2.right(right_deg)
        t2.backward(branch_len)


if __name__ == '__main__':
    # t1 = init_turtle()
    # draw_spiral(t1, 100)
    # ts = t1.getscreen()
    # ts.getcanvas().postscript(file='../images/spiral.eps')

    t2 = turtle.Turtle()
    t2.left(90)
    t2.penup()
    t2.backward(100)
    t2.pendown()
    t2.pencolor('green')
    t2.pensize(2)
    draw_tree(100)
    t2.hideturtle()
    turtle.done()

