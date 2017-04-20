# flask读书笔记_chpter3
<!-- MarkdownTOC -->

- [概念剖析](#概念剖析)
  - [jinja2初试](#jinja2初试)
  - [jinjia2 传入复杂变量](#jinjia2-传入复杂变量)
  - [常用过滤器](#常用过滤器)
  - [模板中的 block 和继承机制](#模板中的-block-和继承机制)
- [使用 Flask-Bootstrap 集成 Twitter Bootstrap](#使用-flask-bootstrap-集成-twitter-bootstrap)
  - [安装flask-bootstrap](#安装flask-bootstrap)
  - [初试flask-bootstrap](#初试flask-bootstrap)
  - [FLask-Boostarp基模板定义的块](#flask-boostarp基模板定义的块)
  - [自定义错误处理模块](#自定义错误处理模块)
  - [创建url的辅助函数](#创建url的辅助函数)
  - [静态文件](#静态文件)

<!-- /MarkdownTOC -->

### 概念剖析
>* (Model View Control) 表现层、业务层与模型层分离机制，而模板用来管理表现层。
>* 模板是一个包含相应文本的文件，其中的动态部分用占位量表示，占位量的具体值只有在请求上下文中才知道。使用真实值替换相应字符。

#### jinja2初试

* 创建模板文件夹`templates`,创建模板文件`index.html`,`user.html`
* `index.html` 输入 `<h1> hello world!</h1>`
* `index.html` 输入 `<h1> hello {{ name }}!</h1>`
* `hello.py` 文件

```python
from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

# 路由的基本用例
@app.route('/')
def index():
	return render_template( 'index.html' )

# 动态路由的基本用例
@app.route('/user/<name>')
def user(name):
	## 使用 jinja2 模板引擎，传入键值对，关键字参数
	return render_template('user.html', name=name)

if __name__ == '__main__':
	manager.run()
```
* 提交到仓库`git add hello.py, readme.md templates`,`git commit -m "jinja2 first demo"`
* 创建标签 `git tag 3a`

#### jinjia2 传入复杂变量

[Flask中Jinja2模板引擎详解(一)–控制语句和表达式](http://www.bjhee.com/jinja2-statement.html)

```python
@app.route('/hello/<name>')
def hello(name=None):
    if name == 'world':
        name = '<em>World</em>'
    return render_template('hello-1.html', name=name, digits=[1,2,3,4,5],
                           users=[{'name':'John'},
                                  {'name':'Tom', 'hidden':True},
                                  {'name':'Lisa'},
                                  {'name':'Bob'}])
```

模板示例：
```html
<dl>
{% for user in users if not user.hidden %}
  {% if loop.first %}
    <div>User List:</div>
    <dd>Deep: {{ loop.depth }}</dd>
    {% continue %}
  {% endif %}
  <div class="{{ loop.cycle('odd', 'even') }}">
  <dt>User No {{ loop.index }}:</dt>
  <dd>{{ user.name }}</dd>
  </div>
  {% if loop.last %}
    <div>Total Users: {{ loop.length }}</div>
  {% endif %}
{% else %}
  <li>No users found</li>
{% endfor %}
</dl>
```

#### 常用过滤器

|过滤器名|说明
|---|---
|safe|渲染时不转义
|capitalize|首字母大写
|lower|转换小写
|upper|转换大写
|title|每个单词的首字母大写
|trim|删除首尾空格
|striptags|删除所有的HTML标签

> 模板语法 {{ name|capitalize }}
> `git commit -m "jinja2 filter"`, `git tag 3b` 

#### 模板中的 block 和继承机制

base.html 文件

```html
<html>
<head>
    {% block head %}
	<title>{% block title %} {% endblock %}</title>
    {% endblock %}
    <style>
      h1{
      	background: black;
      	color: white;
      	text-align: center;
      	font-size: 200% ;
      	padding: 20px;
      	margin: 5px
      }
    </style>
</head>
<body>
   {% block body %}
   {% endblock %}
</body>
</html>
``` 

user.html 文件

```html
{% extends "base.html" %}
<!-- title 嵌套在内层，先对title模块进行衍生 -->
{% block title %} Index {% endblock %}

<!-- super() 调用父文件的定义 -->
{% block head %}
  {{ super() }}
{% endblock %}

{% block body %}
  <h1> Hello {{ name|capitalize }} ! </h1>
{% endblock %}
```
> `git add. `, `git commit -m "Jinja2 block and inhert"`  
> `git tag 3c`

### 使用 Flask-Bootstrap 集成 Twitter Bootstrap
[Bootstrap中文教程](http://www.runoob.com/bootstrap/bootstrap-glyphicons.html)

> Bootstrap 是一个用于快速开发 Web 应用程序和网站的前端框架。Bootstrap 是基于 HTML、CSS、JAVASCRIPT 的。

#### 安装flask-bootstrap

`pip install flask-bootstrap`

> 初始化 Flask-Bootstrap之后，就可以在程序中使用一个包含所有Bootstrap文件的基模板，这个模板采用Jinja2的模板继承机制，让程序扩展一个具有基本页面结构的基模板
> [Bootstrap入门教程](http://www.cnblogs.com/ventlam/archive/2012/05/28/2520703.html)

```python
from flask.ext.bootstrap import Bootstrap
# ...
bootstrap = Bootstrap( app )
```
采用Bootstrap的 `user.html`

#### 初试flask-bootstrap

```html
{% extends "bootstrap/base.html" %}
<!-- 页面标题 -->
{% block title %} Flasky {% endblock %}
{% block navbar %}
<!-- 导航栏 -->
<!-- navbar-inverse 颜色反色即黑色 -->
<nav class="navbar navbar-inverse" role="navigation">
    <div class="container-fluid">
    <!-- 首个导航标签字体稍大 -->
    <div class="navbar-header">
        <a class="navbar-brand" href="/">Flasky</a>
    </div>
    <!-- 其余导航标签 -->
    <div>
        <ul class="nav navbar-nav">
            <li class="active"><a href="/user/zhanghl">zhanghl</a></li>
            <li class="active"><a href="/user/zhanglm">zhanglm</a></li>
        </ul>
    </div>
    </div>
</nav>
{% endblock %}

<!-- 正文 -->
{% block content %}
<div class="container">
	<div class="page-header">
		<h1> Hello, {{name}}</h1>
	</div>
</div>
{% endblock %}
```

> `git add. `, `git commit -m "Jinja2 bootstrap first demo"`  
> `git tag 3d`

#### FLask-Boostarp基模板定义的块

|block名|说明
|---|---
|doc| 整个 html 文档
|html_attribs|`<html>` 标签属性
|html|`<html>` 标签中的内容
|head|`<head>` 标签中的内容
|title|`<title>` 标签中的内容
|metas|一组 `<meta>` 标签 
|styles|层叠样式表定义
|body_attribs|`<body>`标签的属性
|body|`<body>` 标签的内容
|navbar|用户定义的导航条
|`<content>`|用户定义的页面内用
|scripts|文档底部的 JavaScripts 声明

示例：

```html
    <!-- scripts 块示例 -->
    {% block scripts %}
         {{ super() }}
        <script type="text/javascript" src="my-script.js"></script>>
    {% endblock %}
    
    <!-- styles 块示例 -->
    {% block styles %}
        {{ super() }}
        <style type="text/css" src="my-style.css"> </style>
    {% endblock %}
```
> `git add .` , `git commit -m "usual blocks in flask-bootstrap"`

#### 自定义错误处理模块

```python
# 处理错误码的路由
#处理 404 错误
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
```

自定义错误页面：

```html
{% extends "base.html" %}
{% block title %} Flasky - page not found {% endblock %}
{% block page_content %}
  <div class="page-header">
     <h1> Not Found !</h1>
  </div>
{% endblock %}
```
> `git add .` , `git commit -m "user define error page "`
> `git tag 3e`

#### 创建url的辅助函数
`url_for('视图函数名', 动态路由的关键字参数, 额外参数，_external=True)`，`url_for('user', name='John', page2, _external=True ) 返回 http://localhost:5000/user/John?page=2`

#### 静态文件
>* 大多数 web 程序中还会使用静态文件，如 图片，JavaScript 源码文件 和 CSS 
>* 静态文件对应 `url_map` 中的 `/static/<filename>`, 存放在 static 文件夹下

在 `base.html` 中加入 ：

```html
    {% block head%}
        {{ super() }}
        <!-- 对于大多数浏览器，包括 chrome firefox -->
        <link rel="icon" href="{{ url_for('static', filename='favicon.ico' )}}" type="image/x-icon">
        <!-- 对于 I E -->
        <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico' )}}" type="image/x-icon">
    {% endblock %}
```
创建 `static` 文件夹加入 `favicon.ico` 文件

> `git add .` , `git commit -m "use static file create icon "`
> `git tag 3f`
