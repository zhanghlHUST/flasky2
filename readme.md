# flask读书笔记_chpter3
<!-- MarkdownTOC -->

- [概念剖析](#概念剖析)
	- [jinja2初试](#jinja2初试)

<!-- /MarkdownTOC -->

### 概念剖析
>* (Control View Model) 表现层、业务层与模型层分离机制，而模板用来管理表现层。
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

