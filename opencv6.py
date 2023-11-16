# OpenCV 6강: 회전(Rotate)
# 회전 변환 행렬 통해 진행!!
# 회전 변환 행렬(좌푯값 회전, 좌표축 회전)

import cv2
#이미지 파일 불러오기
src = cv2.imread("iu.jpg", cv2.IMREAD_GRAYSCALE)

#이미지의 높이, 너비, 채널의 값 지정
##높이와 너비 사용하여 회전 중심점을 설정한다
height, width = src.shape

#2*3 회전 행렬 생성 함수로 회전 변환 행렬 계산(getRotationMatrix2D(center(회전 기준점), angle(회전 각도), scale(확대 및 축소 비율)))
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

#아핀 변환 함수로 회전 변환 계산(warpAffine(src(이미지), M(아핀 맵 행렬), dsize(출력 이미지 크기)))
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imwrite("rotate.jpg", dst)
cv2.waitKey()
cv2.destroyAllWindows()
