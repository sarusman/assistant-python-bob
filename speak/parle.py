import pyttsx3


engine=pyttsx3.init()


def repond(text):
	engine.say(text)
	engine.runAndWait()
	


