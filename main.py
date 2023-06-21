import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    # print(cv2.getBuildInformation())
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 2, (0, 255, 0))
            if id == 0:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        right = [landmarks[374], landmarks[257]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
            print("Left",left[0].y - left[1].y)
            print("Right",right[0].y - right[1].y)
            #The above two are printed in the terminal for the user to adjust the eye click threshold as per their wish.
        if (left[0].y - left[1].y) < 0.02:
            pyautogui.click()
            pyautogui.sleep(1)
        if (right[0].y - right[1].y) < 0.057:
            pyautogui.click(button='right')
            pyautogui.sleep(2)
    cv2.imshow('MousEye', frame)
    cv2.waitKey(1)
    if 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cam.release()
        break

