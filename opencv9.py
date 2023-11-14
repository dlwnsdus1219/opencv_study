# opencv 9강: 자르기(slice)
# 관심 영역(ROI): 이미지 상에서 관심있는 영역 잘라내기
# 이미지 처리 시 객체 탐지 및 검출

# ##메인 코드 1
# import cv2

# src = cv2.imread("iu.jpg", cv2.IMREAD_COLOR)
# # 높이, 너비, 채널 --> 출력 이미지 크기 설정에 도움
# # height, width, channel = src.shape
# # print(height) //741
# # print(width) //560
# # print(channel) //3

# # 깊은 복사(.copy()) 통해 원본 손상 방지        (dst=src는 얕은 복사->원본에 영향)
# dst = src[100:500, 100:300].copy()

# cv2.imshow("src", src)
# cv2.imshow("dst", dst)
# cv2.waitKey()
# cv2.destroyAllWindows()




##메인 코드2
import cv2

src = cv2.imread("iu.jpg", cv2.IMREAD_COLOR)

dst = src.copy()
roi = src[100:500, 100:300]
dst[0:400, 0:200] = roi

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()