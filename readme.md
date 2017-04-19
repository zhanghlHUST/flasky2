# flask读书笔记_chpter2
<!-- MarkdownTOC -->

- [环境设置](#环境设置)
	- [第一个完整程序](#第一个完整程序)
	- [上下文对象和url_map](#上下文对象和urlmap)
	- [响应对象 Response 的使用](#响应对象-response-的使用)

<!-- /MarkdownTOC -->

> 本书没有细致的讲解设计的逻辑与规则，所以本书的学习重点在于熟悉 flask 处理的基本方式，决定跟着书中的程序敲一遍

### 环境设置
>* 工作目录：`E:\study\evernote\material\flasky2`
>* 创建本地仓库：`git init`
>* 添加 git忽略规则 `.gitignore` 
>* 添加笔记文件 `readme.md`
>* 创建虚拟环境：`virtualenv venv`,`>venv\scripts\activate`, 向 `.gitignore` 添加 `venv` 
>* 安装 flask：`pip install flask` , 向 `.gitignore` 添加 python 的忽略项 `*.py[cod] *.so *.egg *.egg-info dist build`

#### 第一个完整程序

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1> Hello World !</h1>'
# 路由的基本使用
@app.route('/user/<name>')
def user(name):
	return '<h1> Hello %s !</h1>' % name
# 动态路由的基本实现
if __name__ == '__main__':
	app.run(debug=True)
``` 

>* 添加到本地仓库, `git add .`, `git commit -m "2a, basic use of route"`

#### 上下文对象和url_map
``` python
from flask import Flask
from flask import request

app = Flask(__name__)

# 路由的基本用例
@app.route('/')
def index():
	# return '<h1> Hello World !</h1>'
	# request 请求上下文的使用
	# use_agent = request.headers.get('User-Agent')
	# return '<h1> Your brower is %s !</h1>' % use_agent
	# url_map 的信息
	return '<p> url_map is %s !</h1>' % app.url_map


# 动态路由的基本用例
@app.route('/user/<name>')
def user(name):
	return '<h1> Hello %s !</h1>' % name

if __name__ == '__main__':
	app.run(debug=True)
```

>* 添加到本地仓库, `git add .`, `git commit -m "2b, request and url_map"`

#### 响应对象 Response 的使用

``` python
from flask import Flask
from flask import make_response

app = Flask(__name__)

# 路由的基本用例
@app.route('/')
def index():
	# 相应 Response 对象的基本使用
	response = make_response( '<h1> This file carries with a cookie !</h1>' )
	response.set_cookie('answer','42')
	return response

# 动态路由的基本用例
@app.route('/user/<name>')
def user(name):
	return '<h1> Hello %s !</h1>' % name

if __name__ == '__main__':
	app.run(debug=True)
```

>* Chrome 浏览器查看 cookie 点击 url 左侧的感叹号
>* 添加到本地仓库, `git add .`, `git commit -m "2c, response object"`