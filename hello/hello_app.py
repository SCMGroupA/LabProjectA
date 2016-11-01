from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, WE love continuous delivery a lot and WE enjoyed learn SCM!..Yes best"

if __name__ == "__main__":
    app.run()
