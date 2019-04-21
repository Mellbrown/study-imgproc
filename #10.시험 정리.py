import im

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

예제1_1 = lambda: im.g(im.lena).show8().save8('레나사본.bmp')
영상반전 = lambda: im.g(im.lena)\
    .plot8('original lena')\
    .inverse8().plot8('inverse lena')\
    .shows(2)

밝기 = lambda: im.g(im.lena).plot8('lena')\
    .f32().bright32(100).u8().plot8('bright 100')\
    .shows(2)

명암 = lambda : im.glena().plot8('lena')\
    .f32().contra32(2).u8().plot8('contra 2')\
    .shows(2)

감마 = im.glena().plot8('lean')\
    .f32().gamma_corr32(3).u8().plot8('gamma 3')\
    .shows(2)

cr = im.load8(im.data+'copyright.bmp')
lena = im.glena().plot8('origin lena').plotwith8(('copyright', cr))
[lena.plotwith8((str(i), img)) for i, img in enumerate(lena.bit_split8())]
lena.insert_lsb8(cr).plot8('marked')
[lena.plotwith8((str(i), img)) for i, img in enumerate(lena.bit_split8())]
lena.shows(6)