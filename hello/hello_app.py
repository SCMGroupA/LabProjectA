from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return ""<html>
<head></head>
<body>
	<p><u>Mini Project Software Configuration Management MCS1044</u></p>
	<p><i><ul>Group Members:</i>
		<li>Marziah Abdul Wahab KCS15001 </li>
		<li>Nor Faradilla Mohamed Idris KCS15002 </li>
		<li>Sarina Abu Bakar KCS15004 </li>
		<li>Suhaimi Saad KCS15007 </li>
	</ul>
	</p>
</body>
</html>""


if __name__ == "__main__":
    app.run()
