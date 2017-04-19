from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

# 路由的基本用例
@app.route('/')
def index():
	return '<h1> Hello world !</h1>'

# 动态路由的基本用例
@app.route('/user/<name>')
def user(name):
	return '<h1> Hello %s !</h1>' % name

if __name__ == '__main__':
	manager.run()