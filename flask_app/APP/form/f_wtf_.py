# -*- coding:utf-8 -*-
# @TIME     : 2018/10/16  23:16
# @AUTHOR   : LXH
# @FILE     : f_wtf_.py # flask-wtf

# 导入表基
from flask_wtf import FlaskForm

# 导入相关字段
from wtforms import StringField, SubmitField

# 导入相关验证类
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField(label='username', validators=[DataRequired()])
    submit = SubmitField(label='log in')