# -*- coding:utf-8 -*-
# @TIME     : 2018/10/15  20:38
# @AUTHOR   : LXH
# @FILE     : extensions.py # 插件文件

'''
===================================导入插件==============================================
'''
from flask_bootstrap import Bootstrap
# from flask_session import Session # 这个不能瞎配,配上就会报 secret_key 错误

from flask_moment import Moment # 时间模块


'''
====================================实例化对象===========================================
'''
bootstrap = Bootstrap()
# session = Session()
moment = Moment()


'''
====================================封装扩展方法=========================================
'''

def config_extensions(app):
    bootstrap.init_app(app)
    # session.init_app(app) # 这个不能瞎配
    moment.init_app(app)
    pass
