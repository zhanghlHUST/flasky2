from flask import Flask, render_template, session, url_for, redirect
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField("What's your name", validators=[Required()] )
    submit = SubmitField('Submit')

# 设置密钥s
app.config['SECRET_KEY'] = "hard to guess string"

@app.route('/', methods=['GET', 'POST'])
def index():
    name=None
    form = NameForm()
    if form.validate_on_submit():
        # 使用 session 保存数据
        session['name'] = form.name.data
        return redirect( url_for('index'))
    return render_template( 'index.html', form=form, name=session.get('name') )

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