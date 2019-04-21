from 레거시유틸 import *

def imconv(img, kernel):
    h, w = img.shape
    p = kernel.shape[0] // 2
    pimg = np.pad(img, ((p,p), (p,p)), 'constant', constant_values=(0))
    rimg = np.zeros(shape=img.shape, dtype=np.uint8)
    # for y in range(p, h + p):
    #     for x in range(p, w + p):
    #         s = np.sum(pimg[y-p:y+p+1, x-p:x+p+1] * kernel)
    #         rimg[y-p][x-p] = (s if s >=0 else 0) if s < 256 else 255
    # return rimg
    return np.array([ [ np.sum(pimg[y-p:y+p+1, x-p:x+p+1] * kernel) for x in range(p, w + p)] for y in range(p, h + p)])


lena = misc.imread('./data/lena_256.bmp')

setimsnap((3,3), 0)

imsnap(lena, 'origin')

imsnap(imconv(lena, np.array([
    [-1, 0, 0],
    [0, 0, 0],
    [0, 0, 2]
])), 'embossing')

for i in range(12):
    if (i % 2 == 1):
        imsnap(imconv(lena, np.ones(shape=(i, i))  / pow(2,i)), '%dx%d blur' % (i, i))

plt.show()