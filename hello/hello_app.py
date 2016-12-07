from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><b>Marziah, Fara, Sarina, Suhaimi</b></html>"


if __name__ == "__main__":
    app.run()
