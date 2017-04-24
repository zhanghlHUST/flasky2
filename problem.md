<!-- MarkdownTOC -->

- [问题及资源汇总](#问题及资源汇总)
	- [问题汇总](#问题汇总)
		- [Flask中模板的执行机制](#flask中模板的执行机制)
			- [block块的多次设置（层叠）执行机制](#block块的多次设置（层叠）执行机制)
		- [JinJa2中变量的传入机制是什么？](#jinja2中变量的传入机制是什么？)
		- [Flask_wtf 中表单相关问题](#flaskwtf-中表单相关问题)
			- [`get`与`post`的区别](#get与post的区别)
			- [表单数据怎样提交到程序？](#表单数据怎样提交到程序？)
			- [执行方式](#执行方式)
		- [`Flask-SQKAlchemy`在执行`create_all\(\)` 自动创建对应的表，如何识别所有需要建表的对象](#flask-sqkalchemy在执行createall-自动创建对应的表，如何识别所有需要建表的对象)
	- [资源汇总](#资源汇总)

<!-- /MarkdownTOC -->
# 问题及资源汇总

## 问题汇总

### Flask中模板的执行机制

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

## 资源汇总

[思诚之道](http://www.bjhee.com/jinja2-context.html)  
[flask 扩展文档汇总](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-sqlalchemy.html)  

