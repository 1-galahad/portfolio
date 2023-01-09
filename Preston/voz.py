import pyttsx3
en = pyttsx3.init()
en.say("oi Lara")
en.setProperty('voice', b'brazil')
en.runAndWait()
