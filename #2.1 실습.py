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
    print(i)
    plt.subplot(y, x, i)
    plt.imshow(img)
    plt.gray()
    plt.title(title)

im = misc.imread('./data/lena_256.bmp')
row, col = im.shape

# 실습 1
n = 50
N1 = 100
N2 = 150
중간강조 = np.where( N1 > im, im, np.where(im > N2, im, im + n))
snapImage(중간강조, '중간강조')

# 실습 2
평균값 = np.mean(im)
이진화 = np.where(평균값 < im, 255, 0)
snapImage(이진화, '이진화')

# 실습 3
N1 = 100
N2 = 150
슬라이스 = np.where( N1 > im, im, np.where(im > N2, im, 255))
snapImage(슬라이스, '슬라이스')

# 실습 4
N1 = 50
N2 = 100
N3 = 150
N4 = 200
등명도선 = np.where (
    im > N4, 255,
    np.where (
        im > N3, 0,
        np.where (
            im > N2, 255,
            np.where(
                im > N1, 0, 255
            )
        )
    )
)
snapImage(등명도선, '등명도선')

# 실습 5
N1 = 100
N2 = 150
N3 = 200
명도단계변화 = np.where (
    im < N1, 0,
    np.where (
        im < N2, N1,
        np.where (
            im > N3, N2, N3
        )
    )
)
snapImage(명도단계변화,'명도단계변화')

# 실습 6
N1 = 100
N2 = 150
중간제거 = np.where( N1 > im, im, np.where(im > N2, im, 0))
중간통과 = np.where( N1 > im, 0, np.where(im > N2, 0, im))
# print(중간제거)
snapImage(중간제거, '중간제거')
snapImage(중간통과, '중간통과')

plt.show()