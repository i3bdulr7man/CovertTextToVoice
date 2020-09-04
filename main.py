from gtts import gTTS
from playsound import playsound

print("اكتب النص هنا")

#Arabic
mytext_ar = input()
myobj = gTTS(text=mytext_ar, lang='ar')
myobj.save("out_ar.mp3")
playsound("out_ar.mp3")