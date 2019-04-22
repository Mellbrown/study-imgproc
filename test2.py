import im
import 유틸

# 2.a
im.g(유틸.영상덧셈32(
    im.lena32,
    유틸.영상뺄셈32(
        im.lena32,
        im.glena().conv32(im.kernel.mean(3)).im
    )
)).plot8('y(x, y)')\
    .plotwith8(('f(x,y)', im.lena)).shows(2)