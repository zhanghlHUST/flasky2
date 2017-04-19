from flask import Flask
from flask import redirect
from flask import abort

app = Flask(__name__)

# 路由的基本用例
@app.route('/')
def index():
	# 重定向响应 redirect(url)
	return redirect('http://baidu.com')

# 动态路由的基本用例
@app.route('/user/<name>')
def user(name):
	if name !='zhang':
	# 处理错误的abort 函数的使用
		abort(404)
	return '<h1> Hello %s !</h1>' % name

if __name__ == '__main__':
	app.run(debug=True)