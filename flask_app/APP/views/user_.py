# -*- coding:utf-8 -*-
# @TIME     : 2018/10/15  23:04
# @AUTHOR   : LXH
# @FILE     : user_.py

from flask import Blueprint


user = Blueprint('user',__name__)

@user.route('/hello_flask/')
def hello_flask():
    return 'hello flask'