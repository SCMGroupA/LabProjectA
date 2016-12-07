from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><b><center>Mini Project SCM <p>Marziah, Fara, Sarina, Suhaimi</center></b>
            <p><img src="img/robot.jpg" width="600" height="200" />
	</html>"


if __name__ == "__main__":
    app.run()
