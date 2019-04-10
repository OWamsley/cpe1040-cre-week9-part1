binaryString = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]


def binary_to_unsigned():
    unsigned = 0
    y = 0
    for i in range(31, -1, -1):
        unsigned += (binaryString[i] * (2**y))
        y = y + 1
    print(unsigned)


def binary_to_signed():
    global binaryString

    signed = 0
    y = 0
    print(binaryString)
    if binaryString[0] == 1:
        binaryStringInverse = []
        # flip the bits
        for i in binaryString:
            # binaryStringInverse.append(binaryString[i])
            if i == 0:
                binaryStringInverse.append(1)
            else:
                binaryStringInverse.append(0)
        print(binaryStringInverse)
        for i in range(31, 0, -1):
            signed += (binaryStringInverse[i] * (2 ** y))
            y = y + 1
        signed = signed + 1
        signed = signed * -1
    else:
        for i in range(31, 0, -1):
            signed += (binaryString[i] * (2 ** y))
            y = y + 1
    print(signed)



def binary_to_float():
    sign = 1
    exponent = 0
    mantissa = 0
    y = 0
    if binaryString[0] == 1:
        sign = -1
    for i in range(9, 0, -1):
        exponent += (binaryString[i] * (2 ** y))
        y += 1
    exponent -= 128
    y = 1
    for i in range(9, 32,):
        mantissa += (binaryString[i] * (2 ** -y))
        y += 1
    mantissa = mantissa + 1
    float_value = sign * (2 ** exponent) * mantissa
    print(sign)
    print(exponent)
    print(mantissa)
    print(float_value)


def binary_to_ascii():


binary_to_unsigned()
binary_to_signed()
binary_to_float()
