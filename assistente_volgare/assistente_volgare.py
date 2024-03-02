from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from datetime import datetime
import webbrowser
from random import choice
import subprocess

#setto la voce 
engine = init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[22].id)
#parla
engine.say("che cavolo vuoi")
engine.runAndWait()
#per pigrizia riduco i caratteri da utilizzare
r = Recognizer()

#ascolta
with Microphone() as source:
    print("pronto ad ascoltare...")
    #registra l'audio
    audio = r.listen(source)
    #trasforma l'audio in testo
    testo = r.recognize_google(audio, language="it-IT").lower()
    #risposta di defout
    risposta = "ma esprimiti meglio che non si capisce una mazza"
    print(testo)
    #sceglie la risposte piu adatta
    if "ricetta" in testo:
        file_path = "/Users/newmac/Desktop/ricetta.txt"
        #crea e scrive un file di testo
        with open(file_path, "w") as f:
            f.write("scemo chi legge")
        risposta = "ho creato per te, un testo con la ricetta"
    elif any(parola in testo for parola in ["ora", "ore", "orario"]):                                                                   #ti da l'orario corretto
        risposta = choice(["vai a comprarti un orologio...", "è l\'ora di ieri a quest\'ora", f" sta volta ti è andata bene sono le ore {datetime.now().strftime('%H e %M')}"])
        if "orologio..." in risposta:
            #apre amazon 
            webbrowser.open("https://www.amazon.it/s?k=orologio")
    elif testo.startswith(("cosa", "come", "quanto")):
        risposta = choice(["e che ne so", "chiedi ad Alexa, a Siri o a Google non stare a scassare proprio a me", "ma che te frega"])
    #parla
    engine.say(risposta)
    engine.runAndWait()
    #apre il file ricetta
    try:
        subprocess.run(['open', file_path])
    except Exception as e:
        pass