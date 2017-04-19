from flask import Flask
from flask import request

app = Flask(__name__)

# 路由的基本用例
@app.route('/')
def index():
	# return '<h1> Hello World !</h1>'
	# request 请求上下文的使用
	# use_agent = request.headers.get('User-Agent')
	# return '<h1> Your brower is %s !</h1>' % use_agent
	# url_map 的信息
	return '<p> url_map is %s !</h1>' % app.url_map


# 动态路由的基本用例
@app.route('/user/<name>')
def user(name):
	return '<h1> Hello %s !</h1>' % name

if __name__ == '__main__':
	app.run(debug=True)