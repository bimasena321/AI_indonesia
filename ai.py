import url
import pyttsx3
import os as putar
from gtts import gTTS
import speech_recognition as sr


error = "ulangi pengucapan anda saya tidak dengar"
negara = 'id'
mesin = pyttsx3.init()
suara = mesin.getProperty('voice')
record = sr.Recognizer()

with sr.Microphone() as v:
    mesin.setProperty('voice', suara[0].id)
    print ("mendengarkan...")
    read = record.listen(v)
    
    try:
        read1 = record.recognize_google(read)
        url.yt(read1)
        print("anda: ", format(read1))
    except:
        error1 = gTTS(text=error, lang=id)
        error1.save('error.mp3')
        putar.system('error.mp3')
                
    
    