import cv2
import mediapipe as mp
import pyautogui
import math

# Setup Mediapipe hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
# Screen size for cursor mapping
screen_w, screen_h = pyautogui.size()
cap = cv2.VideoCapture(0)
# Flags for gestures
dragging = False
right_clicking = False
while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Fingertip positions
            index_x, index_y = hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y
            thumb_x, thumb_y = hand_landmarks.landmark[4].x, hand_landmarks.landmark[4].y
            middle_x, middle_y = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y
            # Map hand coords to screen
            cursor_x, cursor_y = int(index_x * screen_w), int(index_y * screen_h)
            pyautogui.moveTo(cursor_x, cursor_y)
            # Distances for gestures
            dist_index_thumb = math.hypot(index_x - thumb_x, index_y - thumb_y)
            dist_middle_thumb = math.hypot(middle_x - thumb_x, middle_y - thumb_y)
            # Drag gesture (index + thumb pinch)
            if dist_index_thumb < 0.05 and not dragging:
                pyautogui.mouseDown()
                dragging = True
            elif dist_index_thumb >= 0.05 and dragging:
                pyautogui.mouseUp()
                dragging = False
            # Right-click gesture (middle + thumb pinch)
            if dist_middle_thumb < 0.05 and not right_clicking:
                pyautogui.rightClick()
                right_clicking = True
            elif dist_middle_thumb >= 0.05:
                right_clicking = False
                # Draw landmarks
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow("Hand Mouse Control", img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()


