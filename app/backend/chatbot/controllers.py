from flask import Blueprint, render_template, render_template, request, jsonify, session
import google.generativeai as ai
import os
from dotenv import load_dotenv

load_dotenv()

index_blueprint = Blueprint('index', __name__)

API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError("API key is missing. Please add it to the .env file.")

ai.configure(api_key=API_KEY)

message_count = 0

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
def index():
    return render_template('index.html', name="Bot")

@index_blueprint.route('/get', methods=['POST'])
def chat():
    
    if 'message_count' not in session:
        session['message_count'] = 0
    
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "Désolé, je n'ai pas compris votre message."})

    model = ai.GenerativeModel("gemini-pro")
    chat = model.start_chat()

    session['message_count'] += 1
    print(session['message_count'])
    if session['message_count'] >= 3 :
        session['message_count'] = 0
        bot_message = "Ce chatbot est une démo. Merci de l'avoir utilisé !"
    else:
        response = chat.send_message(user_message)
        bot_message = response.text

    return jsonify({"response": bot_message})