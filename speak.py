
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
speak.speak("Welcome Hacker, on my pc")


