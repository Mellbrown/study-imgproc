import numpy as np

from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

i = 0
span = (2,4)
def snapImage(img, title):
    global i
    global span
    y, x = span
    i += 1
    plt.subplot(y, x, i)
    plt.imshow(img)
    plt.gray()
    plt.title(title)


im = misc.imread('./data/lena_256.bmp')
row, col = im.shape

alpha = 0.05
gamma_bright = 3
gamma_dark = 0.3
m = np.mean(im)
n = 50
N1 = 100
N2 = 130

im_inversion = 255 - im
im_bright = im + 30
im_dark = im -30
im_contras = im + (im -m) * alpha
im_gamma_bright = np.power(im/255, 1/gamma_bright) * 255
im_gamma_dark = np.power(im/255, 1/gamma_dark) * 255
buff = np.where( N1 > im, im, np.where(im > N2, im, im + n))


snapImage(im,'Original Image')
snapImage(im_inversion, 'Inversion Image')
snapImage(im_bright,'bright Image')
snapImage(im_dark,'dark Image')
snapImage(im_contras, 'contras Image')
snapImage(im_gamma_bright, 'gamma bright correcion')
snapImage(im_gamma_dark, 'gamma dark correcion')
snapImage(buff, 'gamma dark correcion')
plt.show()