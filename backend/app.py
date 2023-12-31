from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import openai
import dotenv
from dotenv import load_dotenv, find_dotenv
from gevent.pywsgi import WSGIServer

# DOTENV
load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPEN_AI_KEY")


# FLASK
app = Flask(__name__)
CORS(app)


@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    message = data['message']
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=3000,
        temperature=0.9,
    )
    print(response.choices[0].text)
    return jsonify({
        "message": response.choices[0].text
    }), 201


if __name__ == '__main__':
    app.run(debug=True)