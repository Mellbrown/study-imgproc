import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
import cv2

# 0. 자료형 처리
imf32 = lambda im8: np.float32(im8)
imu8 = lambda im32: np.uint8(np.where(im32 > 255, 255, np.where(im32 < 0, 0, im32)))

# 1. 영상신호의 입출력
_implot_i = 0
_implot_size = (1, 1)

def implot(im8, title=''):
    global _implot_i
    global _implot_size
    y, x = _implot_size
    _implot_i += 1
    plt.subplot(y, x, _implot_i)
    plt.imshow(im8)
    plt.gray()
    plt.axis('off')
    plt.title(title)

def setimplot(h, w, i = 0):
    global _implot_i
    global _implot_size
    _implot_i = i
    _implot_size = (h, w)

imshow = lambda: plt.show()
imload8 = lambda name: misc.imread(name)
imsave8 = lambda name, img: misc.imsave(name, img)

# 2. 영상화질 조절 및 픽셀 처리 기
영상반전8 = lambda im8: 255 - im8
영상밝기조절32 = lambda im32, 밝기: im32 + 밝기
영상명암비조절32 = lambda im32, 명암비: im32 + (im32 - 128) * 명암비
영상감마보정32 = lambda im32, 감마: np.float_power(im32 / 255, 감마) * 255

영상중간강조32 = lambda im32, 중간1, 중간2, 강조: \
    np.where(im32 > 중간2, im32, np.where(im32 < 중간1, im32, im32 + 강조))
영상이진화8 = lambda im8, 임계값: np.where(im8 > 임계값, 255, 0)


# 3. 영상의 산술 및 논리 연산
영상덧셈32 = lambda im32f, im32g: im32f + im32g
def 평균노이즈32 (im32s):
    result = np.zeros(shape=im32s[0].shape, dtype=np.float32)
    for im32 in imf32: result += im32 / len(im32s)
    return result
영상뺄셈32 = lambda im32f, im32g: np.abs(im32f - im32g)

영비트평면분할 = lambda x : np.array([pow(2, i) * (x >> i & 1) for i in range(7, -1, -1)])


# 4. 공간영역 필터링
def 영상콘볼루션32(im32, kernel):
    h, w = im32.shape
    p = kernel.shape[0] // 2
    pimg = np.pad(im32, ((p, p), (p, p)), 'constant', constant_values=(0))
    return np.array(
        [
            [
                np.sum(pimg[y-p:y+p+1, x-p:x+p+1] * kernel)
                for x in range(p, w + p)
            ]
            for y in range(p, h + p)
        ]
    )

엠보싱커널 = lambda: np.array([[-1, 0, 0], [0, 0, 0], [0, 0, 2]])
평균값커널 = lambda ksize: np.ones(shape=(ksize, ksize)) / (ksize ** 2)
가중평균값커널 = None
def 가우시안커널(ksize, sigma):
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

