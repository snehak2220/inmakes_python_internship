from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello world </h1>"
@app.route(('/new'))
def new():
    return "<h1>This is new page</h1>"
app.run()

