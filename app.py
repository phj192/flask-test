from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return "Hello, Flask!"

"""@app.get("/home")
def home():
    return render_template("home.html", title="Flask 템플릿 연결")"""

@app.get("/hw1")
def home():
    return render_template("hw1.html", title="강의실 배정 건물 예측")

if __name__ == "__main__":
    app.run()