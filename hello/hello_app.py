from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><h1><center>Mini Project SCM <h2>Marziah, Fara, Sarina, Suhaimi</center></h2></html>"


if __name__ == "__main__":
    app.run()
