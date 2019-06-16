import cv2
import numpy as np

img = cv2.imread("../imori.jpg").astype(np.float)

b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out.astype(np.uint8)

out[np.where(out < 128)] = 0
out[np.where(out >= 128)] = 255

cv2.imwrite("./result/out3.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()