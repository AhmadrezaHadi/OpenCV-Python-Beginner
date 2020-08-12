import cv2
from datetime import datetime
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html

# Mode or video path that we want to open
cap = cv2.VideoCapture(0)
fourCC = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi', fourCC, 20.0, (640, 480))

# resizing window
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
#
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        # Converting frame from colored to gray
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # get method, for getting fps of the video
        # print(cap.get(cv2.CAP_PROP_FPS))
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        dt = str(datetime.now())
        frame = cv2.putText(frame, dt, (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

        out.write(frame)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
