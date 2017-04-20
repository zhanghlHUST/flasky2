# flask读书笔记_chpter3
<!-- MarkdownTOC -->

- [概念剖析](#概念剖析)
	- [jinja2初试](#jinja2初试)
	- [jinjia2 传入复杂变量](#jinjia2-传入复杂变量)
	- [常用过滤器](#常用过滤器)

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

