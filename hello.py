from flask import Flask, render_template
from flask_script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

# 路由的基本用例
@app.route('/')
def index():
	return render_template( 'index.html' )

# 动态路由的基本用例
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

#处理 404 错误
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

#处理 500 错误
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	manager.run()