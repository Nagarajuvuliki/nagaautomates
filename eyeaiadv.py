#-----------------------------------
#first install required libraries 
#-----------------------------------
# pip install google-genai==1.49.0
# pip install opencv-python==4.13.0.90
# pip install pyttsx3==2.99
# pip insatll pillow==12.1.0
from google import genai
from google.genai import types
import cv2
import pyttsx3
from PIL import Image
import time
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Normal speed
    print(f"AI: {text}")
    engine.say(text)
    engine.runAndWait()
client = genai.Client(api_key=API_KEY)
chat = client.chats.create(model="gemini-2.5-flash")
# 3. Setup Camera (The Eye)
cap = cv2.VideoCapture(0) #example IP cam usage cv2.VideoCapture("http://192.168.2.129:4747/video")
# Create folder for saved images
if not os.path.exists("saved_images"):
    os.makedirs("saved_images")
image_history = []  # Keep track of saved image paths
speak("I am ready. Press Space to capture, 'h' for history, or 'q' to quit.")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('JARVIS Vision', frame)
    key = cv2.waitKey(1) & 0xFF
    # --- SPACEBAR: Capture new image and chat ---
    if key == 32:  # Spacebar
        filename = f"saved_images/img_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)
        image_history.append(filename)
        img = Image.open(filename)
        while True:  # Sub-loop for repeated Q&A on same image
            user_prompt = input("Ask your question (or type 'next' for new image, 'q' to quit): ")
            if user_prompt.lower() in ["next", "n"]:
                break  # Exit sub-loop, go back to main loop for new image
            elif user_prompt.lower() in ["q", "quit"]:
                cap.release()
                cv2.destroyAllWindows()
                exit()

            if user_prompt.strip() == "":
                user_prompt = "Describe what you see briefly."
            print("Thinking...")
            try:
                response = chat.send_message([user_prompt, img])
                speak(response.text)
            except Exception as e:
                print(f"Error: {e}")
    elif key == ord('h'):
        if not image_history:
            print("No images saved yet.")
            continue
        print("Image History:")
        for i, path in enumerate(image_history):
            print(f"{i}: {path}")
        choice = input("Select image index to chat with: ")
        if choice.isdigit() and int(choice) < len(image_history):
            img = Image.open(image_history[int(choice)])
            while True:  # Sub-loop for repeated Q&A on chosen history image
                user_prompt = input("/n Ask your question (or type 'back' to return, 'q' to quit): ")
                if user_prompt.lower() in ["back", "b"]:
                    break  # Exit sub-loop, go back to main loop
                elif user_prompt.lower() in ["q", "quit"]:
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()
                if user_prompt.strip() == "":
                    user_prompt = "Describe what you see briefly."
                print("Thinking...")
                try:
                    response = chat.send_message([user_prompt, img])
                    speak(response.text)
                except Exception as e:
                    print(f"Error: {e}")
        else:
            print("Invalid choice.")
    elif key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
