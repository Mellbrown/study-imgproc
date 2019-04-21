import im

def 예제1_1 ():
    im.g.lena.show().save8('레나사본.bmp')

def 실습1_1_1 ():
    pass

def 실습1_1_2 ():
    pass

# def 영상반전테스트():
#     im.plots({
#         'original lena': im.lena,
#         'inverse lena': im.g.lena.inverse().im8
#     })
#
# def 영상밝기조절테스트():
#     레나밝기32 = 영상밝기조절32(레나32, 밝기=100)
#     setimplot(1, 2)
#     implot(레나8)
#     implot(im8(레나밝기32))
#     imshow()
#
# def 영상명암비테스트():
#     레나명암8 = im8(영상명암비조절32(레나32, 명암비=2))
#     setimplot(1, 2)
#     implot(레나8)
#     implot(레나명암8)
#     imshow()
#
# def 감마테스트():
#     레나감마 = 영상감마보정32(레나32, 감마=3)
#     im
im.g(im.lena).show8().save8('레나사본.bmp')

영상반전 = lambda: im.g(im.lena)\
    .plot('original lena')\
    .inverse8().plot('inverse lena')\
    .shows(2)

