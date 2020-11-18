from gtts import gTTS
import os    

tts = gTTS(text="Welcome hacker On My Pc, Show i am happy show lucky", lang='en')
tts.save("pcvoice.mp3")
# to start the file from python
os.system("start pcvoice.mp3")