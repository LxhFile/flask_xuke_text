# -*- coding:utf-8 -*-
# @TIME     : 2018/10/15  20:54
# @AUTHOR   : LXH
# @FILE     : __init__.py.py # 创建各种蓝本的地方

# 导入蓝本
from .user_ import user
from .moment_time import moment
from .log_original_form import o_form
from .f_wtf import f_wft


# 装蓝本的元组
BASE_BLUEPRINT = (
    (user,'/user'),
    (moment,'/moment'),
    (o_form,'/o_form'),
    (f_wft,'/f_wtf'),

)

# 循环便利存放蓝本的元组
def config_blueprint(app):
    for blueprint_name,url_prefix in BASE_BLUEPRINT:
        app.register_blueprint(blueprint=blueprint_name, url_prefix=url_prefix)
    pass