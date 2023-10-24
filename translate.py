import speech_recognition as sr
import spacy

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
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

sentence = None

# I spilled my coke can you bring me something to clean it up
while not sentence:
    sentence = listen_and_recognize()

print(sentence)
nlp = spacy.load("en_core_web_sm") 


def verb_noun_finder(sentence):
    verbs = []
    nouns = []
    doc = nlp(sentence)
    
    for token in doc:
        if token.pos_ == "VERB":
            verbs.append(token.text)
        elif token.pos_ == "NOUN" or "PROPN":
            nouns.append(token.text)
        # else:
        #     print(token.text, "is a", token.pos_)
    
    return verbs, nouns

verbs, nouns = verb_noun_finder(sentence)
print(verbs)
print(nouns)