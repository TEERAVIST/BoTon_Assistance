from gtts import gTTS
import os

# Text generated by your AI assistant
response_text = "Hello! I am your AI assistant."

# Generate audio from text
tts = gTTS(text=response_text, lang='en')
tts.save("response.wav")  # Save audio as a WAV file

# Play the audio using aplay
os.system("aplay response.wav")

