# AI-enabled-voice-assistant-multilingual-flask-app
## Robust and free IVR system advisor (no api key)

Testing the IVR System

    Start your Flask application using python app.py.
    Open a web browser and navigate to http://127.0.0.1:5000.
    Select your preferred language and click on "Start Listening" to interact with the AI.

Notes on potential improvement

    Voice Configuration: The TTS voice settings in pyttsx3 may need to be adjusted to find appropriate voices for Swahili and Kinyarwanda. You might explore other TTS options like Google TTS for improved quality.
    Speech Recognition: Make sure that the recognize_google function is able to accurately pick up Swahili and Kinyarwanda by changing the language parameter accordingly.
    Extensive Knowledge Base: Build a more extensive knowledge base tailored specifically for East African agricultural practices and issues for farmers to gain relevant support.
    Deployment: For real deployment, you'll need a server where you can host the Flask application, consider using Heroku or DigitalOcean.

This coded flask app deployed on an HTML web interface helps laying the foundation for a robust IVR system useful for farmers, providing them with timely and valuable agricultural information in their native languages (starting with Swahili and Kinyarwanda for East African farmers).
