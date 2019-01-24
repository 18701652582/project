# _*_ coding: utf-8 _*_
import logging
import os.path
import time


class Logger(object):
    def __init__(self, logger):
        '''''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        #log文件夹名称 如201901240948
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        #系统当前时间目录 如2019-01-24
        directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs 保存日志
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/' + directory_time + '\\'

        #判断当前系统日期的文件夹目录是否存在
        try:
            if not os.path.exists(log_path):
                os.makedirs(log_path)
                print("log目录新建成功：%s" % log_path)
            else:
                print("log目录已存在！！！")
        except BaseException as msg:
            print("新建log目录失败：%s" % msg)
        # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger