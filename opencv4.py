# OpenCV 4강: 비디오 출력
# FFmpeg 지원 -> *.avi, *.mp4 등 다양한 형식 동영상 파일 읽기 가능

import cv2

#동영상 파일 불러오기
capture = cv2.VideoCapture("iuaena.mp4")

# #capture.get으로 비디오의 속성 반환
## cv2.CAP_PROP_POS_FRAMES: 동영상의 현재 프레임 수
## cv2.CAP_PROP_FRAME_COUNT: 동영상의 총 프레임 수
while cv2.waitKey(33) < 0:
    if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0) # 마지막 프레임 도달 시 동영상의 현재 프레임 초기화
    
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    
capture.release()
cv2.destroyAllWindows()

print(cv2.CAP_PROP_FRAME_COUNT)


#VideoCapture 메서드
##capture.isOpened(): 동영상 파일 열기 성공 여부 확인
##capture.open(filename): 동영상 파일 열기
##capture.set(propid, value): 동영상 속성 설정
##capture.get(propid): 동영상 속성 반환
##capture.release(): 동영상 파일 닫고 메모리 해제