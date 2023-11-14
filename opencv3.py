# OpenCV 3강: 이미지 출력
# 래스터 그래픽스 이미지 파일 포맷(JPEG, PNG, GIF)을 쉽게 불러올 수 있는 별도의 함수 제공

import cv2

# 각종 이미지 파일 플래그 알아보기
img = cv2.imread("iu.jpg", cv2.IMREAD_UNCHANGED) #원본 사용
# img = cv2.imread("iu.jpg", cv2.IMREAD_GRAYSCALE) #1채널, 그레이스케일(흑백) 적용
# img = cv2.imread("iu.jpg", cv2.IMREAD_COLOR) #3채널, BGR 이미지 적용
# img = cv2.imread("iu.jpg", cv2.IMREAD_ANYDEPTH) #이미지에 따라 정밀도를 16/32비트 or 8비트로 사용
# img = cv2.imread("iu.jpg", cv2.IMREAD_ANYCOLOR) #가능한 3채널, 색상 이미지로 사용
# img = cv2.imread("iu.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_2) #1채널, 1/2크기, 그레이스케일 적용
# img = cv2.imread("iu.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_4) #1채널, 1/4크기, 그레이스케일 적용
# img = cv2.imread("iu.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_4) #1채널, 1/8크기, 그레이스케일 적용
# img = cv2.imread("iu.jpg", cv2.IMREAD_REDUCED_COLOR_2) #3채널, 1/2크기, BGR이미지 
# img = cv2.imread("iu.jpg", cv2.IMREAD_REDUCED_COLOR_4) #3채널, 1/4크기, BGR이미지
# img = cv2.imread("iu.jpg", cv2.IMREAD_REDUCED_COLOR_8) #3채널, 1/8크기, BGR이미지
cv2.imshow("IU", img)
cv2.waitKey()   # 키 입력 대기 함수
cv2.destroyAllWindows() # 모든 윈도우창 제거 함수

# 이미지 추가 정보
height, width, channel = img.shape
print(height, width, channel)   #결과: 864  1536  3

# 이미지 속성: 크기(높이/너비), 정밀도, 채널(색상 정보)
