import cv2

### RGB -> BGR ###

img = cv2.imread("../imori.jpg")
b = img[:, :, 0].copy() # [高さ, 横, チャネル]
g = img[:, :, 1].copy() # チャネル=[B, G, R]
r = img[:, :, 2].copy() # ":"...全て選択

img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

# Save result
cv2.imwrite("./result/out1.jpg", img)
cv2.imshow("result", img)
cv2.waitKey(0)  # 任意のキーを押すまでimshowを実行
cv2.destroyAllWindows() # ここまでに作られた全てのウィンドウを閉じる