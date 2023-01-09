import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone(1) as fala:
    frase = rec.listen(fala)


falei = (rec.recognize_google(frase, language = 'pt'))
print (str(falei))
