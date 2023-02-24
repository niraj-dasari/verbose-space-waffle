from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world to bot"

@app.route("/get_text")
def get_text():
    request_data =  request.args.get('data')
    print(request_data)
    return request_data