import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
import cv2

_i = 0
span = (2, 4)
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



bit_plane = lambda x : np.array([pow(2, i) * (x >> i & 1) for i in range(7, -1, -1)])

imgbit = lambda img, i, p : np.where((img >> i & 1) == 1, p, 0)

im = misc.imread('./data/lena_256.bmp')
row, col = im.shape

num_bitslice = 8
img_bitplane = np.ndarray(shape=(num_bitslice, row, col), dtype=np.uint8)
img_restore =np.zeros(shape=(row, col), dtype=np.uint8)

# for y in range(row):
#     for x in range(col):
#         val = im[y, x]
#         c = bit_plane(val)
#
#         for i in range(num_bitslice):
#             img_bitplane[i, y, x] = c[i]
#
# for i in range(num_bitslice):
#     img = img_bitplane[i, :, :]
#     img_restore = img + img_restore
#
    # snapImage(img_restore, '%d' % i)

for i in range(8):
    img_restore = imgbit(im, i, pow(2, i)) + img_restore
    snapImage(img_restore, '%d' % i)

plt.show()