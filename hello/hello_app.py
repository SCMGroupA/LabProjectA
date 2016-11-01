from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, we love continuous delivery a lot and we enjoyed learn SCM!..Yes best"

if __name__ == "__main__":
    app.run()
