import im

sum = 0
for row in im.lena:
    for col in row:
        sum += col

h, w = im.lena.shape
mean = sum / (h * w)

# 1.a
print(mean)

# 1.b
이진화레나 = im.glena().binary8(mean)\
    .plot8('binary').shows(1).im

# 1.c
im.glena().insert_lsb8(이진화레나).save8('최하위비트.bmp')

# 1.d
im.g(im.load8('최하위비트.bmp')).bit_split8()[0]\
    .plot8('lsb').shows(1)