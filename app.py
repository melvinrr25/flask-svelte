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
    # db_users = deta.Base("pet_connect__users")
    db_tokens = deta.Base("pet_connect__tokens")
    db_user_accounts = deta.Base("pet_connect__user_accounts")
    # grab request body
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"status": "failed", "message": "username and password are required"}), 400
    
    res = db_user_accounts.fetch({"username": username, "password": password})
    
    if len(res.items) == 0:
        return jsonify({"status": "failed"}), 401
        
    user = res.items[0]
    token = str(uuid.uuid4())
    db_tokens.put({"token": token, "user_id": user["key"]})
    del user["password"]
    return jsonify({ "token": token, "user": user })
    
@app.route("/api/follow", methods=["POST"])
def follow():
    db_follows = deta.Base("pet_connect__follows")
    # grab request body
    data = request.json
    follower = data.get("followerId") # the person following
    followee = data.get("followeeId") # the person being followed
    
    db_follows.put({ "followerId": follower, "followeeId": followee })
    
    return jsonify({ "result": "ok" })

@app.route("/api/follows/<follower_id>", methods=["GET"])
def get_follow(follower_id):
    db_follows = deta.Base("pet_connect__follows")
    followees = db_follows.fetch({"followerId": follower_id})
    
    return jsonify({ "followees": followees.items })
    
@app.route("/api/users/<account_id>", methods=["POST"])
def user_account_update(account_id):
    db_user_accounts = deta.Base("pet_connect__user_accounts")
    
    # grab request body
    data = request.json
    
    # find existing user account 
    existing_account = db_user_accounts.get(account_id)
    
    petName = data.get("petName")
    petPhotoUrl = data.get("petPhotoUrl")
    ownerName = data.get("ownerName")
    ownerPhotoUrl = data.get("ownerPhotoUrl")
    data = {
        "petName": petName,
        "petPhotoUrl": petPhotoUrl,
        "ownerName": ownerName,
        "ownerPhotoUrl": ownerPhotoUrl,
    }
    # merge existing account with new data
    data = {**existing_account, **data}
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

@app.route("/api/posts", methods=["GET"])
def user_get_posts():
    args = request.args
    last = args.get("last")
    db_user_posts = deta.Base("pet_connect__user_posts")
    db_user_accounts = deta.Base("pet_connect__user_accounts")
    res = db_user_posts.fetch({}, limit=10, last=last)
    
    result = []
    for item in res.items:
        item["user"] = db_user_accounts.get(item["user_id"])
        result.append(item)
    
    return jsonify({ "posts": result })

@app.route("/api/users", methods=["GET"])
def user_get_list():
    args = request.args
    last = args.get("last")
    nameArg = args.get("username")
 
    db_user_accounts = deta.Base("pet_connect__user_accounts")
    if nameArg:
        res = db_user_accounts.fetch({"username?contains": nameArg}, limit=5)
    else:
        res = db_user_accounts.fetch({}, limit=5)
    
    return jsonify({ "users": res.items })

with_debug = True if os.getenv('FLASK_DEBUG') else False
app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=with_debug)