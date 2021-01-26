# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Handsome_Author   : Rui
# @Time     : 2020/4/30 11:46
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 设置数据库的连接地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:root:200810@127.0.0.1:3306/test23'
# 设置是否跟踪数据库变化，开启非常影响性能，不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建数据连接
db = SQLAlchemy(app)


# 映射关系 类>表 属性>字段 对象>记录
class User(db.Model):
    __tablename__ = 't_user'  # 设置表名，表名默认为类名小写
    id = db.Column(db.Integer, primary_key=True)  # 标识为主键
    name = db.Column(db.String(40), unique=True, nullable=False)  # 标识唯一且不能为空值


# @app.route('/')
# def index():
#     # 删除所有继承db.Model的表
#     db.drop_all()
#
#     # 创建所有继承db.Model的表
#     db.create_all()
#
#     # 创建对象（模型）
#     user1 = User(name='zs')
#
#     # 将对象添加到会话（事物）中
#     db.session.add(user1)
#
#     # 提交会话（事物），必须提交，否则数据库不会变化
#     db.session.commit()
#     return 'index'

import time


@app.route('/')
def index():
    time.sleep(3)
    return 'Hello!'

if __name__ == '__main__':
    app.run(threaded=True)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080, debug=True)

