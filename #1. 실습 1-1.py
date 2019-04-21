import numpy as np

from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

lena = misc.imread('./data/lena_256.bmp')
lena_copy = misc.imread('./lena_copy.bmp')


plt.subplot(1, 2, 1)
plt.imshow(lena)
plt.title('lena_256.bmp')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(lena)
plt.title('lena_copy.bmp')
plt.axis('off')

plt.show()