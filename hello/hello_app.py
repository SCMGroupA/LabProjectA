from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, I love continuous delivery a lot and I enjoyed learn SCM!.. make changes..tambahan tambahan tambahan code"

if __name__ == "__main__":
    app.run()
