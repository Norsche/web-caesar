from flask import Flask, request, redirect
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label for="first-name">Rotate By:</label>
            <input id="rot" type="text" name="rot" value="0" />
            <input textarea name="text">
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    rot = str(request.form["rot"])
    text = str(request.form["text"])
    encrypted_text = str(rotate_string(text, rot))
    return "<h1>"+encrypted_text+"</h1>"

app.run()