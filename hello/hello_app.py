from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return ""<html>
<head></head>
<body>
	<p><u>Mini Project Software Configuration Management MCS1044</u></p>
	<p><i>Group Members:</i></p>
		<p>Marziah Abdul Wahab KCS15001 </p>
		<p>Nor Faradilla Mohamed Idris KCS15002 </p>
		<p>Sarina Abu Bakar KCS15004 </p>
		<p>Suhaimi Saad KCS15007 </p>
</body>
</html>""


if __name__ == "__main__":
    app.run()
