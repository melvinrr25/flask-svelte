import os
from flask import Flask, send_from_directory, request, jsonify
from deta import Deta
from dotenv import load_dotenv
import uuid
from flask_cors import CORS

load_dotenv()

deta = Deta(os.getenv("DETA_API_KEY"))

app = Flask(__name__, static_folder='client/dist/assets')
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/dist', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/dist/assets', path)


@app.route("/api/sessions", methods=["POST"])
def login():
    db_users = deta.Base("pet_connect__users")
    db_tokens = deta.Base("pet_connect__tokens")
    # grab request body
    data = request.json
    usename = data.get("username")
    password = data.get("password")
    
    if not usename or not password:
        return jsonify({"status": "failed", "message": "username and password are required"}), 400
    
    res = db_users.fetch({"username": usename, "password": password})
    
    if len(res.items) == 0:
        return jsonify({"status": "failed"}), 401
        
    user = res.items[0]
    token = str(uuid.uuid4())
    db_tokens.put({"token": token, "user_id": user["key"]})
    del user["password"]    
    
    return jsonify({ "token": token, "user": user })

with_debug = True if os.getenv('FLASK_DEBUG') else False
app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=with_debug)