import cv2
import numpy as np

img = cv2.imread("../imori.jpg").astype(np.float)

H, W, C = img.shape

b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out.astype(np.uint8)

max_sigma = 0
max_t = 0

for _t in range(1, 255):
    c0 = out[np.where(out < _t)]
    m0 = np.mean(c0)    if len(c0) > 0  else 0.
    w0 = len(c0) / (H * W)  # クラス0の割合
    c1 = out[np.where(out >= _t)]
    m1 = np.mean(c1)    if len(c1) > 0  else 0.
    w1 = len(c1) / (H * W)  # クラス1の割合

    sigma = w0 * w1 * ((m0 - m1) ** 2)  # このしきい値の時の最大分散
    if sigma > max_sigma:
        max_sigma = sigma
        max_t = _t

print("sigma >>", max_sigma)
print("threshold >>", max_t)

th = max_t
out[out < th] = 0
out[out >= th] = 255

cv2.imwrite("./result/out4.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()