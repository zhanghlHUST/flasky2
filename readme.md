# flask读书笔记_chapter6

<!-- MarkdownTOC -->

- [概念剖析-flask电子邮件操作](#概念剖析-flask电子邮件操作)
  - [python 的邮件支持](#python-的邮件支持)
  - [`Flask-Mail` 的电子邮件支持](#flask-mail-的电子邮件支持)
  - [Flask-Mail SMTP服务器的配置](#flask-mail-smtp服务器的配置)
  - [126邮箱的配置](#126邮箱的配置)
  - [模板渲染邮件](#模板渲染邮件)
- [附录](#附录)
  - [cmd环境变量的设置](#cmd环境变量的设置)

<!-- /MarkdownTOC -->


### 概念剖析-flask电子邮件操作

#### python 的邮件支持

>* python 标准库中的 `smtplib` 包可以用于发送电子邮件
>* `Flask-Mail` 扩展包装了 `smtplib`


#### `Flask-Mail` 的电子邮件支持

* 安装 `pip install flask-mail` 

> 若不配置服务器，`Flask-Mail` 会连接 `localhost` 上的端口 25，发送邮件

#### Flask-Mail SMTP服务器的配置
|配置|默认值|说明
|---|---|---
|`MAIL_SERVER`|`localhost`|电子邮件主机名或IP地址
|`MAIL_PORT`| 25 | 电子邮件服务器端口
|`MAIL_USE_TLS`|`False`| 启用传输层安全协议（Transport Layer Security）
|`MAIL_USE_SSL`|`False`| 启用安全套接层（Secure Sockets Layer）
|`MAIL_USERNAME`|`None`| 邮件账户的账户名
|`MAIL_PASSWORD`|`None`| 邮件账户的密码

#### 126邮箱的配置
[Flask-mail测试和遇到的问题](http://www.jianshu.com/p/ab0f062da743)   
[聊聊HTTPS和SSL/TLS协议](http://www.techug.com/post/https-ssl-tls.html)

126邮箱的服务器主机名`smtp.126.com`，非SSL端口号`25`，SSL端口号 `465`，使用前需要配置`客户端授权密码`

```python
from flask_mail import Mail, Message
...
# 设置邮件
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_126_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_126_PASSWORD')
# 导入邮件
mail = Mail(app)
...
# 路由 /mail>
@app.route('/mail')
def mail_test():
    msg = Message('test subject', sender='发件人@126.com', recipients=['收件人列表@hust.edu.cn'])
    msg.body = 'test body'
    msg.html = '<b>HTML</b> body'
    mail.send(msg)
    return '<h1> hava send the message </h1>'
```
> `git add. git commit -m "flask mail demo"`,`git tag 6a`

#### 模板渲染邮件

`hello.py` 文件中

```python

from flask_mail import Mail, Message
...
# 设置邮件
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_126_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_126_PASSWORD')
# 设置管理员邮箱
app.config['FLASK_ADMIN'] = os.environ.get('FLASK_ADMIN')
# 设置 邮件主题前缀
app.config['FLASK_MAIL_SUBJECT_PREFIX'] = '[Flask]'
# 设置 发件人名称，此处126邮箱要求发件人名称与账户名一致，此处设置无效
app.config['FLASK_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'
# 导入邮件
mail = Mail(app)
...
# 发件函数
def send_mail( to, subject, template, **kwargs):
    msg = Message( app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject, sender = app.config['MAIL_USERNAME'], recipients=[to] )
    # jinja2 同样能够渲染 txt 文件
    msg.body = render_template( template + '.txt', **kwargs )
    # jinja2 渲染 html 文件
    msg.html = render_template( template + '.html', **kwargs )
    mail.send(msg)
...
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
            # 发现新用户，邮件通知管理员
            if app.config['FLASK_ADMIN']:
                send_mail(app.config['FLASK_ADMIN'], 'New User', 'mail/new_user', user=user )
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect( url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))
```

> 设置管理员邮箱环境变量，`set FLASK_ADMIN=xxx@xx.com`

模板文件：`'$templates/mail/new_user.txt`'：`User {{ user.username }} has joined.`
模板文件：`'$templates/mail/new_user.html`'：`User <b>{{ user.username }}</b> has joined.`

> `git add. git commit -m "flask mail with template"`,`git tag 6b`

### 附录
#### cmd环境变量的设置
[cmd命令集-SET(显示、设置或删除 cmd.exe 环境变量](http://blog.itpub.net/637736/viewspace-310181)  
[python环境变量操作](http://aurorawu.lofter.com/post/18f005_6fd653)
