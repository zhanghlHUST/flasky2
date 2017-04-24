from flask import Flask, render_template, session, url_for, redirect, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
import os

# 获取当前路径
basedir = os.path.abspath( os.path.dirname(__file__))

# 设置 flask 对象 manager, bootstrap, 及 moment 对象
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

## 设置 SQLite 数据库 URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
## SQLALCHEMY_COMMIT_ON_TEARDOWN
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
## 获取数据库对象
db = SQLAlchemy(app)
## 定义模型

# 定 Role 模型
class Role(db.Model):

    """ database table class Role """
    # 表名，一般采用 复数 形式
    __tablename__ = 'roles'
    # 类变量即数据表的字段，由 db.Column创建
    # primary_key = True 定义主键
    # unique = True 不允许出现重复的值
    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String(64), unique = True )
    
    # backref 在关系的另一个模型中，添加反向引用
    # 添加到 Role 中的 users 属性代表了关系的面向对象视角，
    # 将返回与角色相关联的用户的列表，第一个参数 用字符串表示关系另一端的模型
    # backref='role' 向User类添加了 role 属性, role_id 返回的是外键的值，
    # role返回的是模型Role的对象
    users = db.relationship('User', backref='role')

    # 返回表示模型的字符串，供调试和测试使用
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):

    """ database table class User """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(64), unique = True, index=True )
    
    # 创建外链，同时创建了关系，引用 表 roles 的 id 字段
    role_id = db.Column(db.Integer, db.ForeignKey( 'roles.id' ) )

    def __repr__(self):
        return '<User %r>' % self.username

        
# # 数据库对象的创建及初始化
# def Create_database():
#     # 创建数据库文件及表，
#     # ? 程序如何识别所有需要创建数据表的对象 ?
#     db.create_all()
#     # 插入行
#     admin_role = Role(name='Admin')
#     mod_role = Role(name='Moderator')
#     user_role = Role(name='User')
#     user_john = User( username='john', role = admin_role )
#     user_susan = User( username='susan', role = user_role )
#     user_david = User( username='david', role = user_role )

#     # 添加到会话
#     db.session.add( admin_role )
#     db.session.add( mod_role )
#     db.session.add( user_role )
#     db.session.add( user_john  )
#     db.session.add( user_susan )
#     db.session.add( user_david )

#     # db.session.add_all( [admin_role, mod_role, user_role, user_john , user_susan, user_david] )
#     # 提交到数据库
#     db.session.commit()
#     # db.session.rollback() 将添加到数据库会话中的所有对象还原到他们在数据库中的状态，相当于git中的checkout
#     # 删除数据
#     # db.session.delete(mod_role)
#     # db.session.commit()


# 创建表单对象
class NameForm(FlaskForm):
    name = StringField("What's your name", validators=[Required()] )
    submit = SubmitField('Submit')

# 设置密钥s
app.config['SECRET_KEY'] = "hard to guess string"

# 路由 index
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # 查找用户信息
        user = User.query.filter_by( username=form.name.data ).first()
        # 记录新用户
        if user is None:
            user = User( username = form.name.data)
            # add 到 session
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect( url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))



    name=None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session['name']
        if old_name is not None and old_name != form.name.data:
            # flash 推送状态信息
            flash('Looks like you have changed your name!')
        # 使用 session 保存数据
        session['name'] = form.name.data
        return redirect( url_for('index'))
    return render_template( 'index.html', form=form, name=session.get('name') )


# 动态路由 /user/<name>
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
	# manager.run()
    app.run(host='127.0.0.1',port=5000,debug=True)