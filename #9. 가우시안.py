from 레거시유틸 import *

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

for y in GaussianKernel(9, 1.0):
    for x in y:
        print('{:.4f} '.format(x), end='')
    print('')


setimsnap((2,3), 0)
img = misc.imread('./data/lena_256.bmp')
imsnap(img, 'Original')

for i in range(1, 6):
    kernel = GaussianKernel(9, i)
    imsnap(imconv(img, kernel), 'Gaussian %d.0' % i)

plt.show()
