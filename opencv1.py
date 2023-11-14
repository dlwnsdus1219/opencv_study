import cv2
print(cv2.__version__)

# 이미지 입력 함수 cv2.imread
image = cv2.imread("iu.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("IU", image)
cv2.waitKey(0)
cv2.destroyAllWindows()