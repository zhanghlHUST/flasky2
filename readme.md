# flask读书笔记_chpter5
[flask-SQLAlchemy数据库操作](http://wengmengkai.blog.51cto.com/9016647/1865244)
<!-- MarkdownTOC -->

- [概念剖析-flask数据库操作](#概念剖析-flask数据库操作)
  - [数据库分类](#数据库分类)
  - [python数据库框架](#python数据库框架)
  - [使用 `Flask-SQLAlchemy` 管理数据库](#使用-flask-sqlalchemy-管理数据库)
    - [设置 SQLlite 数据库的链接](#设置-sqllite-数据库的链接)
    - [定义模型](#定义模型)
    - [创建模型之间的关系](#创建模型之间的关系)
    - [数据库操作](#数据库操作)
    - [数据库的查询`query`对象](#数据库的查询query对象)
    - [视图函数中调用数据库](#视图函数中调用数据库)
- [附录](#附录)
  - [常用的SQLAlchemy 的列类型](#常用的sqlalchemy-的列类型)
  - [常用的 SQLAlchemy 的列选项](#常用的-sqlalchemy-的列选项)
  - [常用的 SQLAlchemy 的关系选项](#常用的-sqlalchemy-的关系选项)
  - [常用的 SQLAlchemy 查询过滤器](#常用的-sqlalchemy-查询过滤器)
    - [常用的 query 对象的操作](#常用的-query-对象的操作)

<!-- /MarkdownTOC -->


### 概念剖析-flask数据库操作

#### 数据库分类
>* `SQL数据库`基于关系模型，用表来模拟不同的实体，列定义代表所属实体的数据属性，每个表有个特殊的列称为 **主键**，其值是各行的唯一标识符，不能重复，表中还有 **外键**，引用同一表或不同表的主键，这种联系称为 **关系**。 **特点**：支持联结操作，数据存储高效，数据一致性好，避免重复，但是设计比较复杂。**常见**：MySQL, Oracal, SQLite
>* `NoSQL数据库` 使用 **集合** 代替表，使用 **文档** 代替记录，**特点**数据重复查询效率高，一致性差。**常见**：MongoDB

```python
SQL数据库

#       表 roles               表 users                   
#  ------------------      ------------------            
#    id : 主键              id : 主键
#    name                   username 
#                           password
#                           role_id : 外键
#  ------------------      ------------------ 

NoSQL 数据库

#                users
#          -----------------
#          id
#          username
#          password
#          role: 有大量重复
#          ------------------
```

#### python数据库框架
>* **数据引擎的Python包** 大多数的数据库引擎都有对应的Python包。
>* **数据库抽象层** 如`SQLAlchemy` 和`MongoEngine` 通过 `ORM(Object-Relational Mapper)`或者`ODM(Object-Document Mapper)` 将处理表、文档或查询语言等数据库实体操作转换成为高层的Python对象的操作，极大地提升开发效率。
>* **数据库框架评价指标**：易用性，性能，可移植性。Flask集成度。本书使用的是 Flask-SQLAlchemy

#### 使用 `Flask-SQLAlchemy` 管理数据库

>* 安装 `pip install flask-sqlalchemy`
>* 通过URL指定数据库

| 数据库引擎 | URL
|---|---
| MYSQL | mysql://uername:password@hostname/database
| SQLite(Unix) | sqlite:///absolute/path/to/database
| SQLite(Win) | sqlite:///c:/absolute/path/to/database

##### 设置 SQLlite 数据库的链接

`hello.py` 文件, 设置`app.config['SQLALCHEMY_DATABASE_URI']`,`app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']`

```python
## 设置 SQLite 数据库 URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
## 每次请求提交后，自动提交数据库的修改
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
## 获取数据库对象
db = SQLAlchemy(app)
```

##### 定义模型

> **模型**表示程序使用的持久化实体，在 `ORM` 中，模型一般是一个 Python 类，类的属性对应数据表中的列，类的操作会在底层自动转换成为对应的数据库操作。

`hello.py` 中，定义 Role 和 User 模型

```python
# 定 Role 模型
class Role(db.Model):

    """ database table class Role """
    # 表名，一般采用 复数 形式
    __tablename__ = 'roles'
    # 类变量即数据表的字段，由 db.Column创建
    # primary_key = True 定义主键
    # unique = True 不允许出现重复的值
    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String(64), unique = True )
    
    # 返回表示模型的字符串，供调试和测试使用
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):

    """ database table class User """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(64), unique = True, index=True )
    
    def __repr__(self):
        return '<User %r>' % self.username
```

##### 创建模型之间的关系

`hello.py` 文件中，User中定义外键 `role_id` 的同时定义了关系，可以在关系的另一端`Role`中定义关系，添加反向引用。

```python
class User(db.Model):
...    
# 创建外链，同时创建了关系，引用 表 roles 的 id 字段
    role_id = db.Column(db.Integer, db.ForeignKey( 'roles.id' ) )
...

class Role(db.Model):
... 
# backref 在关系的另一个模型中，添加反向引用
# 添加到 Role 中的 users 属性代表了关系的面向对象视角，
# 将返回与角色相关联的用户的列表，第一个参数 用字符串表示关系另一端的模型
# backref='role' 向User类添加了 role 属性, role_id 返回的是外键的值，
# role返回的是模型Role的对象
    users = db.relationship('User', backref='role')
...
```

##### 数据库操作
与`git`的操作十分相似  

* **创建数据表**  `db.create_all() ` 创建`sqlite`数据库文件`data.sqlite`，改动模型后，更新数据库时只能删除旧表 `db.drop_all()`，然后重新 `db.create_all() ` 创建，但是会导致原有数据的丢失。
* **插入记录** 只需要调用模型的关键字参数形式的构造函数，如 `admin_role = Role(name='Admin)'`，主键 `id` 由 `Flask-SQLAlchemy` 管理，不需要明确设置
* **同步模型改动到数据库** 使用 `db.session` 数据库事务对象管理对数据库的改动，如添加记录到数据库 `db.session.add(admin_role)`
* **提交操作** `db.session.commit()`
* **修改记录** 首先修改模型对象属性值，然后 `db.session.add(), db.session.commit() `
* **删除记录** 首先`db.session.delete( model obj)` 然后提交到仓库 `db.session.commit()`

`hello.py`文件添加

```python
# 数据库对象的创建及初始化
def Create_database():
    # 创建数据库文件及表，
    # ? 程序如何识别所有需要创建数据表的对象 ?
    db.create_all()
    # 插入行
    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_john = User( username='john', role = admin_role )
    user_susan = User( username='susan', role = user_role )
    user_david = User( username='david', role = user_role )

    # 添加到会话
    db.session.add( admin_role )
    db.session.add( mod_role )
    db.session.add( user_role )
    db.session.add( user_john  )
    db.session.add( user_susan )
    db.session.add( user_david )

    # db.session.add_all( [admin_role, mod_role, user_role, user_john , user_susan, user_david] )
    # 提交到数据库
    db.session.commit()
    # db.session.rollback() 将添加到数据库会话中的所有对象还原到他们在数据库中的状态，相当于git中的checkout
    # 删除数据
    # db.session.delete(mod_role)
    # db.session.commit()
```

##### 数据库的查询`query`对象
[SQLALchemy-查询篇](http://lib.csdn.net/article/python/1453)  
[Python SQLAlchemy基本操作和常用技巧](http://www.jb51.net/article/49789.htm)  

> `Flask-SQLAlchemy` 为每个模型类都提供一个`query`对象，
> 而 **过滤器** 在 `query` 上调用，返回更加精确的 `query` 对象 ，过滤器返回 `query` 对象

> **利用关系创建的模型对象1* * `User.query.filter_by(role=user_role).all()`，role是**关系**添加的模型对象，`str( User.query.filter_by(role=user_role))` 查询ORM自动生成的查询语句
> **利用关系创建的模型对象2** `user_role.users` 默认情况下返回的是`query`对象的查询结果，设置 `lazy = dynamic` 可以得到查询对象

cmd 中 shell 方式执行查找：

```shell
>>> python hello.py shell
>>> from hello import db, Role, User
>>> User.query.all()
[<User 'john'>, <User 'susan'>, <User 'david'>]

```

`git add. git commit -m "sqlalchemy first demo"`

##### 视图函数中调用数据库

`hello.py`文件

```python
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
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect( url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))
```


### 附录
#### 常用的SQLAlchemy 的列类型

|类型名称 |python类型 |描述
|---|---|---
|Integer  |int  |常规整形，通常为32位
|SmallInteger  |int  |短整形，通常为16位
|BigInteger  |int或long  |精度不受限整形
|Float  |float  |浮点数
|Numeric  |decimal.Decimal  |定点数
|String  |str  |可变长度字符串
|Text  |str  |可变长度字符串，适合大量文本
|Unicode  |unicode  |可变长度Unicode字符串
|Boolean  |bool  |布尔型
|Date  |datetime.date  |日期类型
|Time  |datetime.time  |时间类型
|Interval  |datetime.timedelta  |时间间隔
|Enum  |str  |字符列表
|PickleType  |任意Python对象  |自动Pickle序列化
|LargeBinary  |str  |二进

#### 常用的 SQLAlchemy 的列选项

|可选参数 |描述
|---|---
|primary_key|如果设置为True，则为该列表的主键
|unique|如果设置为True，该列不允许相同值
|index|如果设置为True，为该列创建索引，查询效率会更高
|nullable|如果设置为True，该列允许为空。如果设置为False，该列不允许空值
|default|定义该列的默认值

#### 常用的 SQLAlchemy 的关系选项

|选项名|说明
|---|---
|backref |在关系的另一个模型中添加反向引用
|primaryjoin |明确指定另个模型之间使用的关系的联结条件
|lazy |指定如何加载相关记录，可选项有 select( 首次访问按需加载 )，immediate( 源对象加载后立即加载 )，joined( 加载记录且使用联结 )，subquery( 立即加载，使用子查询 )，noload( 永不加载 )，dynamic( 不加载记录，提供加载记录的查询 )
|uselist |默认为真，对应一对多，返回列表，若为 `False` 对应一对一，返回标量值
|order_by |关系中记录的排序方式
|secondary |指定 `多对多` 关系中关系表的名字
|secondaryjoin |指定 `多对多` 关系中 `二级联结` 条件

#### 常用的 SQLAlchemy 查询过滤器
[在 Flask 中使用 SQLAlchemy](http://docs.jinkan.org/docs/flask/patterns/sqlalchemy.html)

|过滤器|说明
|---|---
|`filter()`| 将过滤器添加到原查询上，返回新查询    
|`filter_by()`| 将等值过滤器添加到原查询上，返回新查询  
|`limit()`| 使用指定的值限制返回的结果数量，返回新查询  
|`offset()`| 偏移原查询的结果，返回新查询  
|`oredr_by()`| 采用指定条件对原查询的结果排序，返回新查询
|`group_by`|采用指定条件对原查询结果进行分组，返回新查询    

##### 常用的 query 对象的操作

|操作|说明
|---|---
|`all()`| 列表形式返回所有查询结果
|`first()`| 返回查询结果的第一个，如果没有返回`None`
|`first_or_404()`| 返回查询结果的第一个，如果没有终止请求，返回404
|`get()`| 返回主键对应的行，如果没有返回 `None`
|`get_or_404()`| 返回主键对应的行，如果没有，终止请求，返回404
|`count()`| 返回查询结果的数量
|`paginate()`| paginate (为书或者手稿标页数)，返回一个`paginate`对象，包含指定范围的结果