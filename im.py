import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
import cv2
from mpl_toolkits.mplot3d import Axes3D

# 0. 자료형 처리
f32 = lambda im8: np.float32(im8)
u8 = lambda im32: np.uint8(np.where(im32 > 255, 255, np.where(im32 < 0, 0, im32)))

# 1. 영상신호의 입출력
_implot_i = 0
_implot_span = (1, 1)

def plot(im8, title=None):
    global _implot_i
    global _implot_span
    y, x = _implot_span
    _implot_i += 1
    plt.subplot(y, x, _implot_i)
    plt.imshow(im8)
    plt.gray()
    plt.axis('off')
    plt.title(title if title is not None else '')

def setplot(col, row, i = 0):
    global _implot_i
    global _implot_span
    _implot_i = i
    _implot_span = (row, col)

show = lambda: plt.show()


def __set_plots__(col, l):
    setplot(col, (l // col) + (0 if (l % col == 0) else 1), 0)

def __dic_plots__(col, dic_im8s):
    __set_plots__(col, len(dic_im8s))
    for name, im8 in dic_im8s: plot(im8, name)
    show()

def __lst_plots__(col, lst_im8s):
    __set_plots__(col, len(lst_im8s))
    for im8 in lst_im8s: plot(im8)
    show()

def plots(col, *im8s):
    if len(im8s) == 1:
        if isinstance(im8s, dict): __dic_plots__(col, *im8s[0])
        elif isinstance(im8s, list): __lst_plots__(col, *im8s[0])
    __lst_plots__(col, im8s)

load8 = lambda name: misc.imread(name)
load32 = lambda name: f32(load8(name))
save8 = lambda name, im8: misc.imsave(name, im8)

def mean_noise32(im32s):
    result = np.zeros(shape=im32s[0].shape, dtype=np.float32)
    for im32 in im32s:
        result += im32 / len(im32s)
    return result

bitplan = lambda deci: np.array([pow(2, i) * (deci >> i & 1) for i in range(7, -1, -1)])
bit_split8 = lambda im8, bit: np.where((im8 >> bit & 1) == 1, 1, 0) * np.power(2, bit)


class g:
    def __init__(self, im8):
        self.im = im8

    def f32(self):
        self.im = f32(self.im)
        return self

    def u8(self):
        self.im = u8(self.im)
        return self

    def show8(self, title=None):
        plot(self.im, title)
        return self

    load8 = lambda name: g(load8(name))
    load32 = lambda name : g(load32(name))
    lena = (lambda: g(lena))()
    def save8(self, name):
        save8(name, self.im8)
        return self

    def inverse8(self):
        self.im = 255 - self.im8
        return self

    def bright32(self, bright):
        self.im = self.im + bright
        return self

    def contra32(self, contra):
        self.im = self.im + (self.im - 128) * contra
        return self

    def gamma_corr32(self, gamma):
        self.im = np.float_power(self.im / 255, gamma) * 255
        return self

    def mid_emph8(self, thres1, thres2, emph):
        self.im = np.where(thres1 <= self.im,
               np.where(self < thres2, self.mi + emph, self.im), self.im)
        return self

    def binary8(self, thres):
        self.im = np.where(thres <= self.im, 255, 0)
        return self

    def slice8(self, thres1, thres2):
        self.im = np.where(thres1 <= self.im,
               np.where(self.im < thres2, 255, self.im), self.im)
        return self

    def leadwire8(self, thress, start=0):
        result = np.ones(shape=self.im.shape) * start
        for thres in thress:
            start = 255 - start
            result = np.where(self.im < thres, result, start)
        self.im = result
        return self

    def brightstep8(self, thress):
        result = np.zeros(shape=self.im.shape)
        for thres in thress:
            result = np.where(self.im < thres, result, thres)
        self.im = result
        return self

    def mid_block8(self, thres1, thres2):
        self.im = np.where(thres1 <= self.im,
               self.im, np.where(self.im < thres2, 0, self.im))
        return self

    def mid_pass8(self, thres1, thres2):
        self.im = np.where(thres1 <= self.im, 0,
               np.where(self.im < thres2, self.im, 0))
        return self

    def bit_split8(self):
        return [g(bit_split8(self.im, bit)) for bit in range(8)]

    def insert_lsb8(self, im8):
        self.im = np.where(im8 & 1 == 1, self.im | 1, self.im& 254)
        return

    def conv32(self, kernel):
        h, w = self.im.shape
        p = kernel.shape[0] // 2
        pimg = np.pad(self.im, ((p, p), (p, p)), 'constant', constant_values=(0))
        self.im = np.array([[
            np.sum(pimg[y - p:y + p + 1, x - p:x + p + 1] * kernel)
            for x in range(p, w + p)] for y in range(p, h + p)
        ])

class kernel:
    embossing = lambda: np.array([[-1, 0, 0], [0, 0, 0], [0, 0, 2]])
    mean = lambda ksize: np.ones(shape=(ksize, ksize)) / (ksize ** 2)
    @staticmethod
    def weight_mean(seed):
        k = np.array(seed)
        k = np.hstack(k, np.fliplr(k[:][:k.shape[1] - 1]))
        k = np.vstack(k, np.flipud(k[:k.shape[0] - 1][:]))
        return k / sum(k)
    @staticmethod
    def gaussian(ksize, sigma):
        ss = sigma ** 2
        k = ksize // 2
        return np.array([[
            1 / (2 * np.pi * ss) * np.exp(-(x ** 2 + y ** 2) / (2 * ss))
            for x in range(-k, k + 1)] for y in range(-k, k + 1)
        ])

data = './data/'
lena = load8(data+'lena_256.bmp')
lena32 = f32(lena)