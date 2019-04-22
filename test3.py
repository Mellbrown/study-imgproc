import numpy as np
import im

def LoG_128(sigma):
    a = -1 / (np.pi * (sigma ** 4))
    result = []
    for y in range(-128, 128):
        result_row = []
        for x in range(-128, 128):
            b = 1 - ( ((x ** 2) + (y ** 2)) / (2 * (sigma ** 2)) )
            c = np.exp(-((x ** 2) + (y ** 2)) / (2 * (sigma ** 2)))
            result_row.append(a*b*c)
        result.append(result_row)
    return np.array(result)

# test 3.a
im.g(LoG_128(sigma=30)).plot8('LoG(x, y)').shows(1)

# test 3.b
im.plot3D(LoG_128(30), 'LoG(x, y) 3D')

def LoG9(sigma):
    a = -1 / (np.pi * (sigma ** 4))
    result = []
    for y in range(-4, 5):
        result_row = []
        for x in range(-4, 5):
            b = 1 - ( ((x ** 2) + (y ** 2)) / (2 * (sigma ** 2)) )
            c = np.exp(-((x ** 2) + (y ** 2)) / (2 * (sigma ** 2)))
            result_row.append(a*b*c)
        result.append(result_row)
    return np.array(result)

# test 3.c
for y in LoG9(0.8):
    for x in y:
        print('{:+.4f} '.format(x), end='')
    print('')

# test 3.d
im.glena().plot8('original')\
    .conv32(LoG9(0.8)).plot8('LoG(x, y)')\
    .shows(2)
