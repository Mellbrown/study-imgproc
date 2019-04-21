import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
import cv2
from mpl_toolkits.mplot3d import Axes3D

# 0. 자료형 처리
imf32 = lambda im8: np.float32(im8)
imu8 = lambda im32: np.uint8(np.where(im32 > 255, 255, np.where(im32 < 0, 0, im32)))

# 1. 영상신호의 입출력
_implot_i = 0
_implot_size = (1, 1)

def implot(im8, title=None):
    global _implot_i
    global _implot_size
    y, x = _implot_size
    _implot_i += 1
    plt.subplot(y, x, _implot_i)
    plt.imshow(im8)
    plt.gray()
    plt.axis('off')
    plt.title(title if title is not None else str(_implot_i))

def setimplot(h, w, i = 0):
    global _implot_i
    global _implot_size
    _implot_i = i
    _implot_size = (h, w)

def im3D (im8):
    x = np.arange(0, 256, 1.0)
    y = np.arange(0, 256, 1.0)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, im8)

imshow = lambda: plt.show()
imload8 = lambda name: misc.imread(name)
imsave8 = lambda name, im8: misc.imsave(name, im8)

# 2. 영상화질 조절 및 픽셀 처리 기법
영상반전8 = lambda im8: 255 - im8
영상밝기조절32 = lambda im32, 밝기: im32 + 밝기
영상명암비조절32 = lambda im32, 명암비: im32 + (im32 - 128) * 명암비
영상감마보정32 = lambda im32, 감마: np.float_power(im32 / 255, 감마) * 255

영상중간강조32 = lambda im32, 임계1, 임계2, 강조: \
    np.where(임계1 <= im32, np.where(im32 < 임계2, im32 + 강조, im32), im32)
영상이진화8 = lambda im8, 임계: np.where(임계 <= im8, 255, 0)
영상슬라이스8 = lambda im8, 임계1, 임계2: np.where(임계1 <= im8, np.where(im8 < 임계2, 255, im8), im8)
def 영상등명도선8 (im8, 임계s, 시작=0):
    result = np.ones(shape=im8.shape) * 시작
    for 임계 in 임계s:
        시작 = 255 - 시작
        result = np.where(im8 < 임계, result, 시작)
    return result
def 영상명도단계변환8 (im8, 임계s):
    result = np.zeros(shape=im8.shape)
    for 임계 in 임계s:
        result = np.where(im8 < 임계, result, 임계)
    return result
영상중간제거 = lambda im8, 임계1, 임계2: np.where(임계1 <= im8, im8, np.where(im8 < 임계2, 0, im8))
영상중간통과 = lambda im8, 임계1, 임계2: np.where(임계1 <= im8, 0, np.where(im8 < 임계2, im8, 0))

# 3. 영상의 산술 및 논리 연산
영상덧셈32 = lambda im32f, im32g: im32f + im32g
def 평균노이즈32 (im32s):
    result = np.zeros(shape=im32s[0].shape, dtype=np.float32)
    for im32 in im32s:
        result += im32 / len(im32s)
    return result
영상뺄셈32 = lambda im32f, im32g: np.abs(im32f - im32g)
영상논리곱8 = lambda im8f, im8g: np.bitwise_and(im8f, im8g)
영상논리합8 = lambda im8f, im8g: np.bitwise_or(im8f, im8g)
비트평면 = lambda 십진수: np.array([pow(2, i) * (십진수 >> i & 1) for i in range(7, -1, -1)])
영상비트평면분할8 = lambda im8, 비트: np.where((im8 >> 비트 & 1) == 1, 1, 0) * np.power(2, 비트)
영상최하위비트삽입8 = lambda im8f, im8g: np.where(im8g & 1 == 1, im8f | 1, im8f & 254)

# 4. 공간영역 필터링
def 영상콘볼루션32(im32, 커널):
    h, w = im32.shape
    p = 커널.shape[0] // 2
    pimg = np.pad(im32, ((p, p), (p, p)), 'constant', constant_values=(0))
    return np.array([[
        np.sum(pimg[y-p:y+p+1, x-p:x+p+1] * 커널)
        for x in range(p, w + p) ] for y in range(p, h + p)
    ])
엠보싱커널 = lambda: np.array([[-1, 0, 0], [0, 0, 0], [0, 0, 2]])
평균값커널 = lambda ksize: np.ones(shape=(ksize, ksize)) / (ksize ** 2)
def 가중평균값커널 (커널일부):
    k = np.array(커널일부)
    k = np.hstack(k, np.fliplr(k[:][:k.shape[1]-1]))
    k = np.vstack(k, np.flipud(k[:k.shape[0]-1][:]))
    return k / sum(k)
def 가우시안커널(ksize, sigma):
    ss = sigma**2
    k = ksize//2
    return np.array([[
        1 / (2*np.pi*ss) * np.exp(-(x**2+y**2)/(2 * ss))
        for x in range(-k, k+1) ] for y in range(-k, k+1)
    ])

# 이미지 소스들
데이터 = './data/'
이미지레나 = './data/lena_256.bmp'