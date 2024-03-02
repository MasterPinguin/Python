import face_recognition as fr 
from glob import glob
from shutil import move

immagine_nota = fr.load_image_file("/Users/newmac/Documents/PROG/Pythone/riconoscimento_facciale/don_matteo.jpg")
encoding_noto = fr.face_encodings(immagine_nota)[0]

for foto in glob("/Users/newmac/Documents/PROG/Pythone/riconoscimento_facciale/foto_varie/*.jpg"):
    print(foto)
    immagine = fr.load_image_file(foto)
    encoding = fr.face_encodings(immagine)[0]
    match = fr.compare_faces([encoding_noto], encoding)[0]
    print(match)
    if match:
        move(foto, "/Users/newmac/Documents/PROG/Pythone/riconoscimento_facciale/don_matteo")
        print("trovato")

print("yeeee")