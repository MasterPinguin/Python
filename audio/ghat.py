import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound


# Inizializza il riconoscitore vocale
recognizer = sr.Recognizer()

# Funzione per registrare l'audio e ottenere il testo
def record_audio():
    with sr.Microphone() as source:
        print("Di qualcosa:")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Non ho capito"
        except sr.RequestError:
            return "Non sono in grado di connettermi al servizio di riconoscimento vocale"

# Funzione per generare una risposta vocale
def speak_response(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    playsound("response.mp3")

# Loop principale per l'interazione
while True:
    user_input = record_audio()
    print("Utente:", user_input)
    response = "Hai detto: " + user_input  # Sostituisci con l'elaborazione reale del linguaggio naturale
    print("Risposta:", response)
    speak_response(response)
