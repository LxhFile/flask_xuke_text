# -*- coding:utf-8 -*-
# @TIME     : 2018/10/15  19:47
# @AUTHOR   : LXH
# @FILE     : __init__.py.py # 创建app方法

from flask import Flask
from .config import config  # 导入文件，不是导入类
# from APP.config import Config # 存放有 密钥，不需要单独使用，选择环境时候就会携带
from .extensions import config_extensions # 第三方插件方法
from .views import config_blueprint # 蓝本


def create_app(config_name):
    # 实例化一个app对象
    app = Flask(__name__)

    app.config.from_object(config.get(config_name)) # 传入名字，选择环境与通用配置

    config.get(config_name).int_app(app) # 静态方法的安装,加载额外配置

    config_extensions(app) # 加载扩展

    config_blueprint(app) # 激活蓝本

    # 返回加载好的app对象
    return app