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

if __name__ == '__main__':
	manager.run()