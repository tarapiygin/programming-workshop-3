from tkinter import *
from math import sin, cos, sqrt
from random import *
from time import sleep
from tkinter import colorchooser

size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()

x_center = size / 2
y_center = size / 2
rad = 200
canvas.create_oval(x_center - rad, y_center - rad, x_center + rad, y_center + rad, fill='white')
root.update()


def calc_circle_coords(r, f):
    x = r * cos(f)
    y = r * sin(f)
    return x + x_center, y + y_center


fia_orientation = -1
fia_interval = 0.009 * fia_orientation
fia_default = 360
fia = fia_default


def motion():
    global fia
    canvas.delete('anim')
    rad_dot = 20
    x_dot, y_dot = calc_circle_coords(rad, fia)
    x_dot2, y_dot2 = x_dot, y_dot

    # считаем координаты квадрата для создания овала
    if x_dot > x_center:
        x_dot2 = x_dot + rad_dot / 2
        x_dot = x_dot - rad_dot / 2
    elif x_dot < x_center:
        x_dot2 = x_dot - rad_dot / 2
        x_dot = x_dot + rad_dot / 2

    if y_dot > y_center:
        y_dot2 = y_dot + rad_dot / 2
        y_dot = y_dot - rad_dot / 2
    elif y_dot < y_center:
        y_dot2 = y_dot - rad_dot / 2
        y_dot = y_dot + rad_dot / 2

    canvas.create_oval(x_dot, y_dot, x_dot2, y_dot2, fill="red", outline="red",
                       tag='anim')

    if fia == 0:
        fia = fia_default
    else:
        fia += fia_interval
    root.after(5, motion)


motion()
root.mainloop()
