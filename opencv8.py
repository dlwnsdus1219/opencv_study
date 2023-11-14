# OpenCV8: 크기 조절
# 이미지 확대 - 픽셀에 대한 보간법 / 이미지 축소 - 픽셀에 대한 병합법
## 1. 사용자 요구 절대 크기로 변경
## 2. 비율에 맞게 상대 크기 변경

import cv2

#이미지 불러오기
src = cv2.imread("iu.jpg", cv2.IMREAD_COLOR)

# 이미지 크기 조절 함수: 이미지 피라미드(2배만 가능)와 달리 원하는 크기로 변환 가능!!
# cv2.resize(src(입력 이미지), dstSize(절대 크기), fx(상대 크기), fy(상대 크기), interpolation(보간법))
# 상대 크기로 이미지 변경?: 절대 크기에 (0, 0) 할당 후에 조정!!
dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)   # 영역 보간법
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)    #쌍 선형 보간법

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()
