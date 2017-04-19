from flask import Flask
from flask import make_response

app = Flask(__name__)

# 路由的基本用例
@app.route('/')
def index():
	# 相应 Response 对象的基本使用
	response = make_response( '<h1> This file carries with a cookie !</h1>' )
	response.set_cookie('answer','42')
	return response

# 动态路由的基本用例
@app.route('/user/<name>')
def user(name):
	return '<h1> Hello %s !</h1>' % name

if __name__ == '__main__':
	app.run(debug=True)