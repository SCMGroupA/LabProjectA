from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """"<html>
<head></head>
<body><p><b>Hello World!</b></p></body>
</html>"""


if __name__ == "__main__":
    app.run()
