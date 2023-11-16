# 카메라 출력(데이터를 실시간으로 받아오고 분석하는 경우 사용)
import cv2
import numpy as np

capture = cv2.VideoCapture(0)   # 카메라 장치 번호와 연결(내장 카메라는 0)
# capture.set(propid, value) // propid: 카메라 설정, value: 속성값
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# while문 통해 카메라 프레임 지속적으로 받기
while cv2.waitKey(33) != ord('q'):              # waitKey(키 입력 대기 시간)
    ret, frame = capture.read()         # capture.read() 메서드 통해 카메라의 상태 및 프레임을 받아온다 // ret = True(카메라 정상작동), False(카메라 작동X)
    #cv2.imshow(창 이름(변수와 비슷한 역할), 이미지)
    cv2.imshow("VideoFrame", frame)    

capture.release()       # 메모리 해제
cv2.destroyAllWindows()     # 모든 윈도우 창 제거