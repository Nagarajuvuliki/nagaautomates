from google import genai
from google.genai import types
import cv2
import time
from PIL import Image
# Gemini API Key from Google AI Studio
client = genai.Client(api_key="")
# 2. Initialize Camera
cap = cv2.VideoCapture(0)
print("AI Eye is active! Press 's' to ask AI what it sees, or 'q' to quit.")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Naga Automates - AI Eye', frame) # Show the video feed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        img_path = "snapshot.jpg" # Save frame temporarily
        cv2.imwrite(img_path, frame)
        print("Thinking...")
        try:
            image_file = Image.open(img_path)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=["Describe what you see in this image in one sentence.", image_file]
            )
            print(f"AI says: {response.text}")
        except Exception as e:
            print(f"Error: {e}")
    elif key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
