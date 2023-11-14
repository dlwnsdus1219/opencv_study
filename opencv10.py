# OpenCv 10강: 색상 공간 변환
# 본래의 색상에서 다른 공간으로 변환할 때 사용(데이터 타입은 같게 유지, 채널 변환!!)
# 입력 이미지: 8/16/32비트 정밀도의 배열
# 출력 이미지: 입력 이미지의 이미지 크기와 정밀도가 동일한 배열
# 데이터 값 변경 or 채널 순서 변경 가능

import cv2

#이미지 불러오기
src = cv2.imread("iu.jpg", cv2.IMREAD_COLOR)
#색상 공간 변환함수(cv2.cvtColor(src(입력 이미지), code(색상 변환 코드), dstCn(출력 채널)))
#색상 변환 코드: 원본 이미지 색상 공간 2 결과 이미지 색상 공간
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2Lab)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2Luv)
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2HLS)
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2XYZ)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()