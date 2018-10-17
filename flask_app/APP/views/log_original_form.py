# -*- coding:utf-8 -*-
# @TIME     : 2018/10/16  20:41
# @AUTHOR   : LXH
# @FILE     : log_original_form.py # 原生表单
from flask import Blueprint, render_template, request
# from __future__ import print_function # 这是使用python新功能的包

o_form = Blueprint('o_form', __name__)


# @o_form.route('/form/<username>/', methods=['POST', 'GET'])
# def form(username):
#     if request.method == 'POST':
#         pass
#     return render_template('original_form.html', username=username)

@o_form.route('/form/',methods=['POST', 'GET'])
def form():
    username = 'god'
    if request.method == 'POST':
        username = request.form['username']
        return render_template('original_form.html',username = username)

    return render_template('original_form.html',username = username)
