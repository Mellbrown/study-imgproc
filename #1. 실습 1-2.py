import numpy as np

from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

for i in range(6):
    image = misc.imread('./images/%d.jpg' % i)
    plt.subplot(2,3, i+1)
    plt.imshow(image)
    plt.axis('off')

plt.show()