from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Visitor System</h1><p>Welcome to Al Mansour City</p>"

if __name__ == "__main__":
    app.run(debug=True)
