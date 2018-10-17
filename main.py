from flask import Flask, request
from caesar import rotate_string

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
                font: 16px arial black;
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
      <!-- create your form here -->
       <form method="POST">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="0" />
            <br />
            <textarea name="text">{0}</textarea>
            <br />
            <input type="submit" value = "Submit Query" />
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    newtext = ''
    for char in text:
        newtext += rotate_string(char, rot)
    return form.format(newtext)


app.run()
