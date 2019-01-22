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
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label for="first-name">Rotate By:</label>
            <input id="rot" type="text" name="rot" value="0" />
            <input id="textarea" name="text">
            <input type="submit" value="Submit Query" />
            <textarea>
                {0}
            </textarea>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]
    encrypted_text = rotate_string(text, rot)
    return form.format(encrypted_text)

app.run()