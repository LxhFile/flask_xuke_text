# -*- coding:utf-8 -*-
# @TIME     : 2018/10/16  23:14
# @AUTHOR   : LXH
# @FILE     : f_wtf.py # flask-wtf
from flask import Blueprint, render_template

# 导入表基类
from APP.form.f_wtf_ import NameForm

f_wft = Blueprint('f_wtf',__name__)


@f_wft.route('/wtf/', methods = ['POST','GET'])
def wtf():
    # 创建表单对象
    form = NameForm()
    # 渲染时候分配到模板文件
    return render_template('f_wtf.html', form=form)