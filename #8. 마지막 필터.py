from 레거시유틸 import *

sigma = 50.0
G = np.zeros(shape=(256), dtype=np.float)

for x in range (-127, 129):
    s = 1/(np.sqrt(2*np.pi) * sigma)
    v = -(pow(x, 2))/(2*pow(sigma, 2))
    G[x+127] = s*np.exp(v)

sigma = 50.0
G2 = np.zeros(shape=(256,), dtype=np.float)

for x in range (-127, 128):
    s = 1/(np.sqrt(2*np.pi) * sigma)
    v = -(pow(x, 2))/(2*pow(sigma, 2))
    G2[x+127] = s*np.exp(v)

G2 = G2.reshape((256, 1))
print(G.shape)
print(G2.shape)

G3 = G2 * G
print(G3.shape)


plt.plot(G)
plt.title('1-D Gaussian')
plt.show()

sigma = 10.0
x_axis = np.arange(-127, 128)
s = 1 / (np.sqrt(2 * np.pi) * sigma)
v = -(pow(x_axis, 2)) / (2 * pow(sigma, 2))
G1 = s * np.exp(v)

plt.plot(G1)
plt.title('1-D Gaussian')
plt.show()


sigma = 50.0

G2D = np.array([[1 / (2 * np.pi * sigma**2) * np.exp(-(x**2 + y**2) / (2 * sigma**2)) for x in range(-127, 128)] for y in range(-127, 128)])
plt.imshow(G2D)
plt.show()

img = misc.imread('./data/lena_256.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)

from mpl_toolkits.mplot3d import Axes3D
x = np.arange(0, 256, 1.0)
y = np.arange(0, 256, 1.0)
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, img)
plt.show()

G2D = np.array([[1 / (2 * np.pi * sigma**2) * np.exp(-(x**2 + y**2) / (2 * sigma**2)) for x in range(-4, 5)] for y in range(-4, 5)])
