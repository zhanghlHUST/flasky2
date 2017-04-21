# flask读书笔记_chpter4



### 概念剖析-flask表单对象

>* `request.form` 能够获取 POST 请求中提交的表单对象，但是需要很多重复的操作，如：生成表单的HTML代码和验证提交的表单数据。
>* `Flask-WTF` 扩展能够方便的处理表单，`pip install flask-wtf`

#### 跨站请求伪造保护
>* `Flask-WTF`，需要程序设置一个密钥，`Flask-WTF`利用密钥生成加密令牌，再利用令牌验证请求中表单数据的真伪。
>* `app.config` 字典能用来存储框架、扩展和程序本身的配置变量。 
>* `app.config['SECRET_KEY'] = 'scret word'` 设置通用密钥，可在 FLask 和多个第三方库中使用。
>* 为了增强安全性，密钥不应该直接输入代码，而要保存在环境变量中。

```python
  app = FLask(__name__)
  app.config['SECRET_KEY'] = "hard to guess string"
```

#### 表单类
[廖雪峰-Python教程-使用元类](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000)
>* `flask-web` 中的每个表单都由继承自 `Form` 的一个类表示，这个类定义表单中一组字段，每个字段都用对象表示。类似于ORM的技术
>* 每个字段都可附属一个或多个验证函数，验证用户输入是否符合要求

`hello.py` 文件:
```python
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
  name = StringField("What's your name", validators=[Required()] )
  submit = SubmitField('Submit')
# ---------------------------------------------------- #
# ---------------------------------------------------- #
# 路由的 GET 和 POST 的区别是什么，及执行过程？
@app.route('/', methods=['GET', 'POST'])
def index():
    name=None
    form = NameForm()
    if form.validate_on_submit():
      name = form.name.data
      form.name.data = ''
    return render_template( 'index.html', form=form, name=name )
```

`index.html` 文件：

```python
{% extends "base.html" %}
<!-- 导入 wtf.html --> 
{% import "bootstrap/wtf.html" as wtf %}
{% block title %} Flasky - index {% endblock %}
{% block page_content %}
  <div class="page-header">
     <h1> Hello {% if name %} {{name}} {% else %} Stranger{% endif %} !</h1>
  </div>
  <!-- 表单渲染成 html -->
  {{ wtf.quick_form(form) }}
{% endblock %}
```
>* `git add. `, `git commit -m "flask-wtf first demo "`, `git tag 4a`
