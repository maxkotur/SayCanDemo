import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to capture audio and recognize speech
def listen_and_recognize():
    with sr.Microphone() as source:
        print("Please speak something...")
        audio = recognizer.listen(source)
        print("Recognizing...")

    try:
        text = recognizer.recognize_google(audio)  # You can change the recognition engine if needed
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

# Main program loop
while True:
    listen_and_recognize()
