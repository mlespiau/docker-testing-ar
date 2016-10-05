from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Las manos de todos los testers arriba y arriba!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
