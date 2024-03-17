from flask import Flask
test=Flask(__name__)

@test.route('/profile/<int:id>')
def home(id):
    return "<h1>This profile is for %d </h1>" % id
test.run(debug=True)


