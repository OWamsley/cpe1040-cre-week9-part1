# binaryString = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
from microbit import *

binaryString = []

for x in range(26):
    x_axis = x % 5
    y_axis = x / 5
    # bit 0 is at (0,0)
    changeBit(x, x_axis, y_axis, binaryString)

microbit.display.clear()

for x in range(26, 33):
    y = x
    y = y - 26


def changeBit(x, x_axis, y_axis, binaryString):
    microbit.display.set_pixel(x_axis, y_axis, 0)
    z = 0
    while true:

        if button_a.is_pressed() and z == 0:
            microbit.display.set_pixel(x_axis, y_axis, 0)
            z = 0
        if button_a.is_pressed() and z == 1:
            microbit.display.set_pixel(x_axis, y_axis, 9)
            z = 1
        if button_b.is_pressed():
            break
    binaryString.append(z)


