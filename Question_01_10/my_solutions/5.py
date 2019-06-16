import cv2
import numpy as np

img = cv2.imread("../imori.jpg").astype(np.float) / 255.

out = np.zeros_like(img)    # 引数と同じ形の中身が全て0のリストを作成

### HSVに変換 ###
max_v = np.max(img, axis=2).copy()
min_v = np.min(img, axis=2).copy()
min_arg = np.argmin(img, axis=2)

H = np.zeros_like(max_v)
H[np.where(max_v == min_v)] = 0
ind = np.where(min_arg == 0)    # Bが最小のときの場所
H[ind] = 60 * (img[:, :, 1][ind] - img[:, :, 2][ind]) / (max_v[ind] - min_v[ind]) + 60
ind = np.where(min_arg == 1)    # Gが最小のときの場所
H[ind] = 60 * (img[:, :, 2][ind] - img[:, :, 0][ind]) / (max_v[ind] - min_v[ind]) + 300
ind = np.where(min_arg == 2)    # Rが最小のときの場所
H[ind] = 60 * (img[:, :, 0][ind] - img[:, :, 1][ind]) / (max_v[ind] - min_v[ind]) + 180

S = max_v.copy() - min_v.copy()
V = max_v.copy()
### ここまで ###

# 色相Hを反転
H = (H + 180) % 360

### RGBに再変換 ###

C = S
H_dash = H / 60
X = C * (1 - np.abs(H_dash % 2 - 1))

Z = np.zeros_like(H)

vals = [[Z,X,C], [Z,C,X], [X,C,Z], [C,X,Z], [C,Z,X], [X,Z,C]]

for i in range(len(vals)):
    ind = np.where((i <= H_dash) & (H_dash < (i+1)))
    out[:, :, 0][ind] = (V-C)[ind] + vals[i][0][ind]
    out[:, :, 1][ind] = (V-C)[ind] + vals[i][1][ind]
    out[:, :, 2][ind] = (V-C)[ind] + vals[i][2][ind]

out[np.where(max_v == min_v)] = 0
out = (out * 255).astype(np.uint8)

cv2.imwrite("./result/out5.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()