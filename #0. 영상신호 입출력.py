import numpy as np

from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

lena = misc.imread('./data/lena_256.bmp')
row, col = lena.shape
plt.imshow(lena)
plt.gray()
plt.show()

misc.imsave('lena_copy.bmp', lena)