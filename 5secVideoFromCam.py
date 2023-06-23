import cv2
import time

cap = cv2.VideoCapture(0)  #Use 0 for the default webcam

duration = 5  #5 seconds
fps = cap.get(cv2.CAP_PROP_FPS)
num_frames = int(duration * fps)

frames = []  #List to store frames

while(True):
    for _ in range(num_frames):
        ret, frame = cap.read()
        frames.append(frame)
        cv2.imshow('5 second video', frame)

        if cv2.waitKey(1) == 27:  #Press 'Esc' to stop capturing
            break

    cap.release()
    cv2.destroyAllWindows()
    output_filename = 'captured_video.mp4'
    output_fps = 30  #Frames per second for the output video
    output_size = (frames[0].shape[1], frames[0].shape[0])  # Frame size

    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(output_filename, fourcc, output_fps, output_size)

    for frame in frames:
        out.write(frame)

    out.release()