from plyer import notification
import time
import pyttsx3 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
notification.notify(
            title="Take a Break",
            message="You have not to drink water for half an hour. So kindly drink it",
            app_icon=None,
            timeout=5
)

speak("Janaki! Please drink water and stay hydrated")