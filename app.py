import os
from flask import Flask, send_from_directory

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='client/dist/assets')

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/dist', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/dist/assets', path)


with_debug = True if os.getenv('FLASK_DEBUG') else False
app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=with_debug)