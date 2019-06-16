import cv2

img = cv2.imread("../imori.jpg")

out = img.copy()
out = out // 64 * 64 + 32

cv2.imwrite("./result/out6.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()