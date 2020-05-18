from flask import  Flask


app = Flask(__name__)

@app.route("/<user_name>")
def hello(user_name):
    return "<h1>hello, %s!</h1>"%user_name

if __name__ == "__main__":
    app.run()

