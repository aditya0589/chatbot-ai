# from google import genai
# from google.genai import types

# # Set your Gemini API key
# client = genai.Client(api_key='AIzaSyBXEMKVeBWVrWA4ybPSuHmg9xO26QPl73k')
# ai_model = 'gemini-2.0-flash'

# def get_gemini_reply(prompt):
#     response = client.models.generate_content(
#     model=ai_model,
#     contents=prompt)
#     return response.text

import google.generativeai as genai
import os

# Configure API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Load the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')  # or gemini-1.5-pro, gemini-pro-vision

chat = model.start_chat()

def get_gemini_reply(prompt):
    response = chat.send_message(prompt)
    return response.text
