from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3
import json
import os

app = Flask(__name__)
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
knowledge_base = {}
# Define languages
languages = {
    "sw": "sw-TZ",  # Swahili
    "rw": "rw-RW",  # Kinyarwanda
}

def load_custom_knowledge():
    global knowledge_base
    if os.path.exists('custom_knowledge.json'):
        with open('custom_knowledge.json', 'r') as file:
            knowledge_base = json.load(file)
    else:
        knowledge_base = {
            "hello": {
                "sw": "Habari, nafarijika kukuona!",
                "rw": "Bwakire, nishimiye kukubona!"
            },
            "how are you?": {
                "sw": "Niko salama, asante!",
                "rw": "Ndiho neza, urakoze!"
            },
            "info on crops": {
                "sw": "Kuhusu mazao, tunaweza kujadili maelezo zaidi.",
                "rw": "Ku bijyanye n'ibijumba, dushobora kuganira ku bisobanuro birambuye."
            }
            # ... extend with more queries and responses
        }

@app.route('/ask', methods=['POST'])
def ask():
    command = request.json.get("command")
    lang = request.json.get("language", "sw")  # Default to Swahili
    
    # Check if command exists
    response = knowledge_base.get(command.lower(), {"sw": "Samahani, sina majibu kwa hiyo.", "rw": "Mbabarira, sinzi igisubizo kuri ibyo."})
    response_text = response.get(lang, response["sw"])  # Get response in preferred language
    
    # Text-to-Speech
    tts_engine.setProperty('voice', 'english' if lang == 'sw' else 'female')  # Placeholder for voice setting
    tts_engine.say(response_text)
    tts_engine.runAndWait()
    
    return jsonify({"response": response_text})

@app.route('/listen', methods=['POST'])
def listen():
    # Recognize Speech
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='sw')  # Default to Swahili recognition
            return jsonify({"command": command})
        except sr.UnknownValueError:
            return jsonify({"error": "Could not understand audio."})
        except sr.RequestError as e:
            return jsonify({"error": f"Could not request results; {e}"})

def run_app():
    load_custom_knowledge()
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
