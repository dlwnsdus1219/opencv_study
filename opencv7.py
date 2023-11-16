# OpenCV 7강: 이미지 피라미드(Image Pyramid)
# 입력 이미지의 크기 변경해서 영상을 처리한다
# 업 샘플링: 원본 이미지에서 크기 확대
# 다운 샘플링: 원본 이미지에서 크기 축소

#이미지 피라미드 2종류: 가우시안 피라미드, 라플라시안 피라미드

import cv2

#이미지 불러들이기
src = cv2.imread("iu.jpg", cv2.IMREAD_COLOR)
# 높이, 너비, 채널 --> 출력 이미지 크기 설정에 도움
height, width, channel = src.shape

# 이미지 확대 함수(cv2.pyrUp(src(입력 이미지), dstSize(출력 이미지 크기), borderType(테두리 외삽법)))으로 이미지 2배 확대
dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)
# 이미지 축소 함수(cv2.pyrDown(src(입력 이미지), dstSize(출력 이미지 크기), borderType(테두리 외삽법)))
dst2 = cv2.pyrDown(src, borderType=cv2.BORDER_WRAP)

print(dst.height)
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imwrite("pyrup.jpg", dst)
cv2.imshow("dst2", dst2)
cv2.imwrite("pyrdown.jpg", dst2)
cv2.waitKey()
cv2.destroyAllWindows()

