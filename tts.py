import pyttsx3
import re
from multiprocessing import Process

def speak_worker(msg):
    try:
        engine = pyttsx3.init()

        # Optional: Pick a male voice
        voices = engine.getProperty("voices")
        for voice in voices:
            if "male" in voice.name.lower():
                engine.setProperty("voice", voice.id)
                break

        # Use the whole message (no chunking unless needed)
        engine.say(msg)
        engine.runAndWait()

    except Exception as e:
        print("TTS Error:", e)

def speak_text(text):
    # Create the process
    process = Process(target=speak_worker, args=(text,))
    process.start()
    
    # Wait a bit to ensure speech starts and completes
    process.join(timeout=10)  # Max 10 seconds, adjust as needed
