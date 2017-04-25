<!-- MarkdownTOC -->

- [问题及资源汇总](#问题及资源汇总)
	- [问题汇总](#问题汇总)
		- [Flask中模板的执行机制](#flask中模板的执行机制)
			- [Flask 上下文的概念](#flask-上下文的概念)
			- [FLask 扩展对象](#flask-扩展对象)
			- [block块的多次设置（层叠）执行机制](#block块的多次设置（层叠）执行机制)
		- [JinJa2中变量的传入机制是什么？](#jinja2中变量的传入机制是什么？)
		- [Flask_wtf 中表单相关问题](#flaskwtf-中表单相关问题)
			- [`get`与`post`的区别](#get与post的区别)
			- [表单数据怎样提交到程序？](#表单数据怎样提交到程序？)
			- [执行方式](#执行方式)
		- [`Flask-SQKAlchemy`在执行`create_all\(\)` 自动创建对应的表，如何识别所有需要建表的对象](#flask-sqkalchemy在执行createall-自动创建对应的表，如何识别所有需要建表的对象)
		- [shell 与 manage 的执行方式有何区别](#shell-与-manage-的执行方式有何区别)
		- [shell 执行方式的目的是？](#shell-执行方式的目的是？)
		- [数据库修改框架`migrate`的使用](#数据库修改框架migrate的使用)
		- [python 发邮件联系](#python-发邮件联系)
			- [邮件发送任务队列 `Celery`](#邮件发送任务队列-celery)
		- [python 并发](#python-并发)
			- [基本的程序结构](#基本的程序结构)
			- [函数返回线程对象解释](#函数返回线程对象解释)
	- [资源汇总](#资源汇总)

<!-- /MarkdownTOC -->
# 问题及资源汇总

## 问题汇总

### Flask中模板的执行机制

#### Flask 上下文的概念

```python
def send_async_email(app, msg):
    # flsk 上下文的概念
    with app.app_context():
        mail.send(msg)
```

#### FLask 扩展对象

```python
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
```

#### block块的多次设置（层叠）执行机制

> * 在子模块中对父模块的块进行修* 覆盖了父木块的定义？  
> * 假设父木块中存在 `block_A` 包含 `block_B` 是否一定需要先对 `block_B` 进行替换再替换 `block_A`？  
> * 假设父木块中存在 `block_A` 包含 `block_B`，子模块文件对`block_B`进行修改，那么程序如何确保子模块的替换在父模块前？  
>    是否类似于层叠样式表中的，上层定义覆盖下层的机制  

### JinJa2中变量的传入机制是什么？
 
>* render_template("template.html",var=val) 关键字参数的方式传入   
>* Page 31, flask - Moment 部分 `为了处理时间戳，Flask-Moment 向模板开放了 moment 类 `， 以什么样的机制？  
>    猜想是通过 `hello.py` 中的 `moment = Moment(app) ` 语句，并且 `manager`和`bootstrap`都是通过这种机制  

### Flask_wtf 中表单相关问题
#### `get`与`post`的区别
#### 表单数据怎样提交到程序？
#### 执行方式
[flask-wtf速成教程](http://flask123.sinaapp.com/article/60/)

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    name=None
	在 post 和 get 时创建的对象有何区别？
    form = NameForm()
	创建时，自动传入 request 作为参数吗？
	那么，当一个页面有多个表格怎么区分？
    if form.validate_on_submit():
      name = form.name.data
      form.name.data = ''
    return render_template( 'index.html', form=form, name=name )
```

### `Flask-SQKAlchemy`在执行`create_all()` 自动创建对应的表，如何识别所有需要建表的对象

### shell 与 manage 的执行方式有何区别

[网站后端.Flask.五脏俱全的flask-script扩展](http://www.th7.cn/Program/Python/201606/886039.shtml)
> runserver  1.runserver,主要运行Flask内置的Web服务器,可通过python manager.py runserver -h设置内置web开发服务器的命令行参数> 
> shell  1.shell,主要用于基于上下文在ipython(如果安装ipython,可通过Shell(use_ipython=False)或--no-ipython禁用)/python shell中调试程序实例中的对象

### shell 执行方式的目的是？

### 数据库修改框架`migrate`的使用
[Flask 数据库迁移与部署的一些经验](http://www.jianshu.com/p/032723bb9b05)

### python 发邮件联系
[python邮件总结](https://my.oschina.net/jhao104/blog/613774)

#### 邮件发送任务队列 `Celery`

### python 并发
#### 基本的程序结构
#### 函数返回线程对象解释

```python
def send_mail( to, subject, template, **kwargs):
    msg = Message( app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject, sender = app.config['MAIL_USERNAME'], recipients=[to] )
    msg.body = render_template( template + '.txt', **kwargs )
    msg.html = render_template( template + '.html', **kwargs )
    # 创建发邮件线程
    thr = Thread( target=send_async_email, args=[app,msg] )
    thr.start()
    # 为什么返回线程对象
    return thr
```

## 资源汇总

[思诚之道](http://www.bjhee.com/jinja2-context.html)  
[flask 扩展文档汇总](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-sqlalchemy.html)  

