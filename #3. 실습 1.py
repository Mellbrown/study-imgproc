import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
import cv2

_i = 0
span = (4, 5)
def snapImage(img, title):
    global _i
    global span
    y, x = span
    _i += 1
    plt.subplot(y, x, _i)
    plt.imshow(img)
    plt.gray()
    plt.axis('off')
    plt.title(title)

aero = misc.imread('./data/aero2.bmp')
hole = misc.imread('./data/hole.bmp')
hole2 = misc.imread('./data/hole2.bmp')
lena = misc.imread('./data/lena_256.bmp')
diff1 = misc.imread('./data/diff1.bmp')
diff2 = misc.imread('./data/diff2.bmp')
gray127 = misc.imread('./data/gray127.bmp')
gray128 = misc.imread('./data/gray128.bmp')

faero = np.float32(aero)
fhole = np.float32(hole)
fhole2 = np.float32(hole2)
flena = np.float32(lena)
fdiff1 = np.float32(diff1)
fdiff2 = np.float32(diff2)

acc_lean_areo = np.uint8(np.where(faero + flena > 255, 255, faero + flena))
acc_lean_hole = np.uint8(np.where(fhole + flena > 255, 255, fhole + flena))

sub_lean_hole = np.uint8(np.where(flena - fhole2 < 0, 0, flena - fhole2))
sub_hole_lena = np.uint8(np.where(-flena + fhole2 < 0, 0, -flena + fhole2))
diff = np.uint8(abs(fdiff1 - fdiff2))

gray_and = np.bitwise_and(lena, gray128)
gray_or = np.bitwise_or(lena, gray127)


noise = [np.float32(misc.imread('./data/noise%d.bmp' % i)) for i in range(1,9)]

for i in range(1, 8): noise[0] += noise[i]
noise[0] = np.uint8(noise[0] / 8)

snapImage(aero, 'aero')
snapImage(hole, 'hole')
snapImage(lena, 'lena')

snapImage(acc_lean_areo, 'lena+aero')
snapImage(acc_lean_hole, 'lena+hole')

snapImage(sub_lean_hole, 'lena-hole2')
snapImage(sub_hole_lena, 'hole2-lena')

snapImage(diff1, 'diff1')
snapImage(diff2, 'diff2')
snapImage(diff, 'diff')

snapImage(gray_and, 'gray_and')
snapImage(gray_or, 'gray_or')

for i in range(8):
    snapImage(noise[i], 'noise %d' % i)

plt.show()