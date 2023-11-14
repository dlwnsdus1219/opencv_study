# OpenCV 5강: 대칭(filp, symmetry)
# R^2(2차원 유클리드 공간) 위의 선형 변환

import cv2

#이미지 읽어오기
src = cv2.imread("iu.jpg", cv2.IMREAD_ANYCOLOR)

#이미지 대칭(cv2.flip(src, flipcode))
##flipcode < 0: XY축 대칭/flipcode = 0: X축 대칭/flipcode > 0: Y축 대칭
dst = cv2.flip(src, -1)

cv2.imshow("src", src)
#대칭된 이미지 출력
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()