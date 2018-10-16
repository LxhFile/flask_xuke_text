# -*- coding:utf-8 -*-
# @TIME     : 2018/10/16  11:43
# @AUTHOR   : LXH
# @FILE     : moment_time.py

from flask import Blueprint, render_template
from datetime import datetime


moment = Blueprint('moment',__name__)


# 测试时间模块
@moment.route('/timies/')
def timeies():
    current_time = datetime.utcnow() # utc世界标准时间
    return render_template('moment.html',current_time=current_time)

@moment.route('/bootstrap_time/')
def add_time():
    pass
