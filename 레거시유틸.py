import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
import cv2

_i = 0
_span = (3, 4)
def imsnap(img, title):
    global _i
    global _span
    y, x = _span
    _i += 1
    plt.subplot(y, x, _i)
    plt.imshow(img)
    plt.gray()
    plt.axis('off')
    plt.title(title)

def setimsnap(snap, i):
    global _i
    global _span
    _i = i
    _span = snap


def GaussianKernel(ksize, sigma):
    ss = sigma**2
    k = ksize//2
    return np.array(
        [
            [
                1 / (2*np.pi*ss) * np.exp(-(x**2+y**2)/(2 * ss))
                for x in range(-k, k+1)
            ]
            for y in range(-k, k+1)
        ]
    )


def imconv(img, kernel):
    h, w = img.shape
    p = kernel.shape[0] // 2
    pimg = np.pad(img, ((p,p), (p,p)), 'constant', constant_values=(0))
    return np.array(
        [
            [
                np.sum(pimg[y-p:y+p+1, x-p:x+p+1] * kernel)
                for x in range(p, w + p)
            ]
            for y in range(p, h + p)
        ]
    )