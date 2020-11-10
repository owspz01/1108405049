from flask import Flask

app = Flask(__name__)
@app.route('/<int:userid>')
def a(userid):
    return 'userid = {}'.format(userid)

@app.route('/test')
def test():
    return 'hello world555'

if __name__=='__main__':
    appdebug=True
    app.run("127.0.0.1",port=5000)