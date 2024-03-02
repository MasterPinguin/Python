from pyttsx3 import init

engine = init()
voices = engine.getProperty("voices")
x=[1, 10, 22, 32]
for y in x:
    engine.setProperty("voice", voices[y].id)
    engine.say("ciao a scemo gay")
    engine.runAndWait()

#x=0 1 10 22 32
#for voice in voices:
#    print(voice)
#    print(x)
#    x=x+1