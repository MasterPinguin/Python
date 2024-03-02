from gtts import gTTS #comandi per usare la voce di google

audio = "o dio o dio non mi ricordo" #variabile che google pronuncerà

tts = gTTS(text=audio, lang="it", tld="com") #collegamento a google traduttore/ text vuol dire frase che deve pronunciare/lang vuol dire lingua

file = "audio.mp3" #nome del file audio che verra salvato

tts.save(file) # salvataggio del file