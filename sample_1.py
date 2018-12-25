from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    str = "Hello world!"
    return str + str + str

@app.route("/greet/")
def greet_none():
    return "Hello!"

@app.route("/greet/<your_name>")
def greet(your_name):
    return "Hello! " + your_name

if __name__ == "__main__":
    app.run(debug = True)
