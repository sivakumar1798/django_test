import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150) # set the speaking speed to 150 words per minute
engine.setProperty('volume', 0.8) # set the speaking volume to 80%
engine.setProperty('voice', 'english-us') # set the speaking voice to a US English accent
#f = open("/Users/sivakumar/Documents/text.txt", "r")

#value = f.read()
#print(value)
engine.say("hello how are you?")
engine.runAndWait()