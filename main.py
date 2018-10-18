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
                background-color: #C1E7EA;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 20px arial black;
                border-radius: 10px;

            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            h1 {{
                    padding: 10vh 0 0 0;
                    font-family: arial;
                    text-align: center;
                    color: #FA8072;
            }}
            p {{
                    font-family: verdana;
                    text-align: center;
                    color: blue;
            }}
            input[type=submit] {{
                    background-color: magenta;
                    border: double;
                    padding: 10px 22px;
            }}
        </style>
    </head>
    <body>

      <!-- create your form here -->
        <h1>Web Caesar </h1>
        <p>Enter a script and the number of letters to rotate the message.</p>
        <p>Test: Rotate by 13 and agian by 13 will return the original.</p>
        
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

# create your encryption here

def encrypt():
    msg = request.form['text']
    rot = int(request.form['rot'])
    newmsg = ''
    for char in msg:
        newmsg += rotate_string(char, rot)
    return form.format(newmsg)
    

app.run()
