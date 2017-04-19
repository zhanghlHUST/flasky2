# flask读书笔记_1
<!-- MarkdownTOC -->

- [环境设置](#环境设置)
	- [第一个完整程序](#第一个完整程序)

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