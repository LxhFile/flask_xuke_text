# -*- coding:utf-8 -*-
# @TIME     : 2018/10/15  20:18
# @AUTHOR   : LXH
# @FILE     : config.py # 通用配置文件，通用环境配置
import os

# 当前文件根目录(绝对路径)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 通用配置
class Config(object):
    # 通用配置，大写
    # 密钥 每次调用随机生成32位的密钥  , 只有用到session的时候才用启用，用session之前先要进行redis的开启
    SECRET_KEY = os.urandom(32)
    # SECRET_KEY = '123456'


    # redis保存session
    # SECRET_TYPE = 'redis'

    # 留个额外配置的封装方法
    '''
    将函数转化为静态方法，并可以在类中调用 例如：Config.方法名()
                        或者在实例中调用 例如: Config().方法名()  这个实例会被忽略，除了他它的类外
    '''

    @staticmethod
    def int_app(app):
        pass


# 环境配置（开发环境），继承通用配置
class DevelopmentConfig(Config):
    '''
        配置数据库环境
        mysql 配置
        mysql+驱动(驱动:python3的是pymysql   python2的是mysqldb) ://用户名:密码@host:port/数据库名
        数据库必须三干净的
        '''
    # 忽略警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 数据库url
    SQLALCHEMY_DATABASE_URL = None

    # 数据提交自动保存
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 配置完成后去到manage里添加extensions（插件）的db命令


# 测试环境
class TestConfig(Config):
    pass


# 发布环境
class ProductConfig(Config):
    pass


'''----------------------------------通用字典，用于找环境---------------------------'''
config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'product': ProductConfig,
    'default': DevelopmentConfig,
}
