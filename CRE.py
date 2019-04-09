from microbit import *
import time

screen = 0
binaryString = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bitPatternScreen1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bitPatternScreen2 = [0, 0, 0, 0, 0, 0, 0]
stage = 0


# stage 0 is selecting bits, 1 is other stuff

def displayBit():
    display.scroll("good")


def binary_to_unsigned():
    unsigned = 0
    y = 0
    for i in range(31, -1, -1):
        unsigned += (binaryString[i] * (2**y))
        y = y + 1
    print(unsigned)


def changeBit(x, x_axis, y_axis, binaryString, screen):
    z = binaryString[x]
    if screen == 0:
        bitPatternValue = bitPatternScreen1[x]
    if screen == 1:
        bitPatternValue = bitPatternScreen2[(x-25)]
    display.set_pixel(x_axis, y_axis, bitPatternValue)
    while True:
        #display.set_pixel(x_axis, y_axis, bitPatternValue)
        #sleep(250)
        #display.set_pixel(x_axis, y_axis, 5)
        #sleep(250)
        # was_pressed() doesn't work for some reason here, and blinker lines break the code?
        if button_a.is_pressed() and z == 1:
            display.set_pixel(x_axis, y_axis, 0)
            z = 0
            bitPatternValue = 0
            sleep(150)
        if button_a.is_pressed() and z == 0:
            display.set_pixel(x_axis, y_axis, 9)
            z = 1
            bitPatternValue = 9
            sleep(150)
        if button_b.was_pressed():
            break
    if screen == 0:
        bitPatternScreen1[x] = bitPatternValue
        binaryString[x] = z
    if screen == 1:
        # first value in this if nest will be x = 25, this is right for the binaryString
        bitPatternScreen2[(x-25)] = bitPatternValue
        binaryString[x] = z

def changeSequence():
    bps1 = [str(c) for c in bitPatternScreen1]
    bps1i = ''.join(bps1[0:5]) + ":" + ''.join(bps1[5:10]) + ":" + ''.join(bps1[10:15]) + ":" + ''.join(
        bps1[15:20]) + ":" + ''.join(bps1[20:25])
    screen1 = Image(bps1i)
    display.show(screen1)
    screen = 0

    for x in range(25):
        x_axis = x % 5
        y_axis = x // 5
        # bit 0 is at (0,0)
        changeBit(x, x_axis, y_axis, binaryString, screen)
        if button_b.is_pressed():
            time_start = running_time()
            while button_b.is_pressed():
                sleep(5)
            time_stop = running_time()
        b_length = time_stop - time_start
        if b_length > 500:
            displayBit()

    screen = (screen + 1) % 2
    bps2 = [str(d) for d in bitPatternScreen2]
    bps2i = ''.join(bps2[0:5]) + ":" + ''.join(bps2[5:10]) + ":" + ''.join(bps2[10:15]) + ":" + ''.join(
        bps2[15:20]) + ":" + ''.join(bps2[20:25])
    screen2 = Image(bps2i)
    display.show(screen2)

    for x in range(25, 32):
        y = x
        y = y - 25
        x_axis = y % 5
        y_axis = y // 5
        changeBit(x, x_axis, y_axis, binaryString, screen)
        if button_b.is_pressed():
            time_start = running_time()
            while button_b.is_pressed():
                sleep(5)
            time_stop = running_time()
        b_length = time_stop - time_start
        if b_length > 500:
            displayBit()

while True:
    changeSequence()

# for x in range(25):
#    x_axis = x % 5
#   y_axis = x // 5
# bit 0 is at (0,0)
#  changeBit(x, x_axis, y_axis, binaryString)

# display.clear()

# for x in range(26, 33):
#   y = x
#  y = y - 26
# x_axis = y % 5
# y_axis = y //5
# changeBit(x, x_axis, y_axis, binaryString)
