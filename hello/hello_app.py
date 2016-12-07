from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><b><center>Mini Project SCM <p>Marziah, Fara, Sarina, Suhaimi</center></b></html>"


if __name__ == "__main__":
    app.run()
