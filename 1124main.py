from flask import Flask
from resources.user import Users,User
from flask_restful import Api


app= Flask(__name__)
api=Api(app)
api.add_resource(Users,"/users")
api.add_resource(User,"/user/<userid>")

@app.route("/")
def hello():
    return "hello world"

@app.route("/test")
def test():
    return "test"

@app.route("/heyhey/<userid>")
def heyhey(userid):
    return "hey hey {}".format(userid)

@app.route("/123")
def hi():
    return "Hi"

if __name__ == "__main__":
    app.debug=True
    app.run(debug=True,host="0.0.0.0",port=5049)