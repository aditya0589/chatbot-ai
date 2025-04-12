from flask import Flask, request, jsonify, render_template
from gemini_ai import get_gemini_reply
from tts import speak_text

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"reply": "Please enter a message."})
    
    try:
        response = get_gemini_reply(user_input)

        if not response:
            return jsonify({"reply": "Sorry, I didn't get a response."})

        speak_text(response)
        return jsonify({"reply": response})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": f"An error occurred: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
