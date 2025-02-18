from flask import Flask, render_template, request
import bcrypt
import random
import string
import webview
from threading import Thread

app = Flask(__name__)

def run_flask():
    app.run(debug=False, use_reloader=False)

if __name__ == "__main__":
    t = Thread(target=run_flask)
    t.start()

    webview.create_window("Password Criptatore", "http://127.0.0.1:5000")


# Funzione per criptare la password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

# Funzione per generare una password sicura
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def home():
    hashed_password = None
    generated_password = None

    if request.method == "POST":
        if "password" in request.form:
            password = request.form["password"]
            hashed_password = hash_password(password)
        if "generate" in request.form:
            length = int(request.form["length"])
            generated_password = generate_password(length)

    return render_template("index.html", hashed_password=hashed_password, generated_password=generated_password)

if __name__ == "__main__":
    app.run(debug=True)
