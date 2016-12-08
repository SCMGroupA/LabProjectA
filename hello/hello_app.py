from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Friends, here is our SCM Mini Project!"


if __name__ == "__main__":
    app.run()
