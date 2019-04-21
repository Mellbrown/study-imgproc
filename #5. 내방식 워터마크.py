import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
import cv2

_i = 0
span = (3, 4)
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

# 분해 함수
img_bit = lambda img, i, p : np.where((img >> i & 1) == 1, p, 0)

img = misc.imread('./data/lena_256.bmp')
water = misc.imread('./data/copyright.bmp')

# 합성 함
marked = np.where(water & 1 == 1,  img | 1, img & 254)

snapImage(img, 'original')
snapImage(water, 'copyright')
snapImage(marked, 'watermark')
snapImage(np.zeros(shape=img.shape), '')

for i in range(8): snapImage(img_bit(marked, i, pow(2, i)), '%d' % i)

plt.show()

