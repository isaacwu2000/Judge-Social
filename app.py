from model import *
from flask import Flask, render_template, request, jsonify, Response

#print(judgement("User: How are you today? You: I'm doing alright. Just finished prepping a con speech for the upcoming bill on renewable energy incentives. Honestly, trying to wade through all the economic jargon is a bit of a headache. How about you? What's keeping you busy?"))

app = Flask(__name__)

# Rendering index.html
@app.route("/")
def home():
    return render_template("index.html")

# Dealing w/ cors issues
@app.before_request
def handle_options_request():
    if request.method == 'OPTIONS':
        response = Response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
        return response, 200
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    return response


@app.route('/conversation', methods=['POST'])
def conversation_response(): 
    content = request.json
    conversation_text = content.get('conversation', '')
    response = conversation(conversation_text)
    return jsonify({'response': response})

@app.route('/judgement', methods=['POST'])
def conversation_judgement(): 
    content = request.json
    full_conversation_text = content.get('conversation', '')
    print(full_conversation_text)
    response = judgement(full_conversation_text)
    return jsonify({'response': response})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000, debug=True)
