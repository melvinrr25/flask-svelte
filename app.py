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
    db_user_accounts = deta.Base("pet_connect__user_accounts")
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
    print(">>>>>>>>>>>", user["key"])
    print(db_user_accounts.fetch({"user_id": user["key"]}).items)
    account = db_user_accounts.fetch({"user_id": user["key"]}).items[0]
    user["account"] = account
    
    return jsonify({ "token": token, "user": user })
    
@app.route("/api/users/<user_id>/accounts/<account_id>", methods=["POST"])
def user_account_update(user_id, account_id ):
    db_user_accounts = deta.Base("pet_connect__user_accounts")
    
    # grab request body
    data = request.json
    
    petName = data.get("petName")
    petPhotoUrl = data.get("petPhotoUrl")
    ownerName = data.get("ownerName")
    ownerPhotoUrl = data.get("ownerPhotoUrl")
    data = {
        "petName": petName,
        "petPhotoUrl": petPhotoUrl,
        "ownerName": ownerName,
        "ownerPhotoUrl": ownerPhotoUrl,
        "user_id": user_id,
    }
    res = db_user_accounts.put(data, account_id)
    print(res)
    return jsonify({ "result": "ok" })

@app.route("/api/users/<user_id>/posts", methods=["POST"])
def user_posts(user_id):
    db_user_posts = deta.Base("pet_connect__user_posts")
    
    # grab request body
    data = request.json
    
    title = data.get("title")
    content = data.get("content")
    photoUrl = data.get("photoUrl")
    
    data = {
       "title": title,
        "content": content,
        "photoUrl": photoUrl,
        "user_id": user_id,
    }
    res = db_user_posts.put(data)
    print(res)
    return jsonify({ "result": "ok" })

@app.route("/api/users/<user_id>/posts", methods=["GET"])
def user_get_posts(user_id):
    db_user_posts = deta.Base("pet_connect__user_posts")
    res = db_user_posts.fetch({"user_id": user_id})
    return jsonify({ "posts": res.items })

with_debug = True if os.getenv('FLASK_DEBUG') else False
app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=with_debug)