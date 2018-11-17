import speech_recognition as sr

r= sr.Recognizer()

audio = 'blabla.wav'

with sr.AudioFile(audio) as source :
    print ('its reading the file ...!')
    audio = r.record(source)
    print ('now its done from reading !')

try:
    print ('converting ... ')
    text = r.recognize_google(audio)
    print('ur audio said : ')
    print (text)

except Exception as e:
    print (e)        

print ('c ya ')
print ('wait it deserves 2 pizza (mega)')