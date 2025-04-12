import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Filter voices into male and female (based on name hints)
male_voices = [v for v in voices if 'male' in v.name.lower() or 'david' in v.name.lower()]
female_voices = [v for v in voices if 'female' in v.name.lower() or 'zira' in v.name.lower()]

# Create the root window FIRST
root = tk.Tk()
root.title("Text to Speech (pyttsx3)")
root.geometry("500x320")
root.resizable(False, False)

# Create a Tkinter variable AFTER root is initialized
selected_voice = tk.StringVar(value='Male')

# Function to speak the text
def speak_text():
    text = text_input.get("1.0", "end").strip()
    choice = selected_voice.get()

    if text:
        try:
            if choice == 'Male' and male_voices:
                engine.setProperty('voice', male_voices[0].id)
            elif choice == 'Female' and female_voices:
                engine.setProperty('voice', female_voices[0].id)
            else:
                engine.setProperty('voice', voices[0].id)  # Fallback if no match

            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Needed", "Please enter some text.")


tk.Label(root, text="Offline Text to Speech", font=("Arial", 16)).pack(pady=10)

text_input = tk.Text(root, wrap="word", font=("Arial", 12), height=6)
text_input.pack(padx=10, pady=5, fill="both", expand=True)

tk.Label(root, text="Choose Voice:", font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Male", variable=selected_voice, value='Male', font=("Arial", 10)).pack()
tk.Radiobutton(root, text="Female", variable=selected_voice, value='Female', font=("Arial", 10)).pack()

tk.Button(root, text="Speak", font=("Arial", 14), bg="#4CAF50", fg="white", command=speak_text).pack(pady=10)

root.mainloop()
