# flask读书笔记_chapter6

<!-- MarkdownTOC -->

- [概念剖析-flask电子邮件操作](#概念剖析-flask电子邮件操作)
  - [python 的数据库支持](#python-的数据库支持)
  - [`Flask-Mail` 的电子邮件支持](#flask-mail-的电子邮件支持)
- [附录](#附录)
  - [Flask-Mail SMTP服务器的配置](#flask-mail-smtp服务器的配置)

<!-- /MarkdownTOC -->


### 概念剖析-flask电子邮件操作

#### python 的数据库支持

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

### 附录

