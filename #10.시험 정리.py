import im

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

감마 = lambda : im.glena().plot8('lean')\
    .f32().gamma_corr32(3).u8().plot8('gamma 3')\
    .shows(2)

# cr = im.load8(im.data+'copyright.bmp')
# lena = im.glena().plot8('origin lena').plotwith8(('copyright', cr))
# [lena.plotwith8((str(i), img)) for i, img in enumerate(lena.bit_split8())]
# lena.insert_lsb8(cr).plot8('marked')
# [lena.plotwith8((str(i), img)) for i, img in enumerate(lena.bit_split8())]
# lena.shows(6)

print(im.glena().plot8('original lena')\
    .f32().conv32(im.kernel.gaussian(9, 5)).u8().plot8('embossing lena')\
    .shows(2).im.shape)