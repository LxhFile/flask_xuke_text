# -*- coding:utf-8 -*-
# @TIME     : 2018/10/15  20:46
# @AUTHOR   : LXH
# @FILE     : manage.py # 程序入口，安装app给manage控制程序启动

# 导入app初始化方法
from APP import create_app

# 导入运行脚本
from flask_script import Manager


# 导入环境
import os
# 'FLASK_ENV'为环境变量名，可设置,可去config文件去查找，通用环境，做修改
#  [注意：要运行一次命令]Terminal： export FLASK_ENV=default
# 设置这两个先相等，这里的FLASK_ENV也就相当于形参的作用
config_name = os.getenv('FLASK_ENV') or 'default'


app = create_app(config_name) # 获得环境变量后，在此实例化出来


manager = Manager(app) # 把app交给manager控制程序的启动


# 测试运行
@app.route('/hello/')
def hello():
    return 'ok'


if __name__ == '__main__':
    manager.run()