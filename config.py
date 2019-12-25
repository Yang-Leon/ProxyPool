#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import os
from logging.handlers import RotatingFileHandler

# 文件路径参数配置
# 当前路径
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# 日志文件路径
LOG_PATH = os.path.join(BASE_DIR, 'log.txt')

# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'http://www.baidu.com'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10

# 运行类别：0：本地调试、不记录日志，1：服务器运行、记录日志
RUN_TYPE = 1


# 配置日志模块
def get_logger():
    logger = logging.getLogger('proxy_pool')
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s - %(levelname)-8s: %(message)s")

    # 保留两天的日志(线程安全)
    # tfd = logging.handlers.TimedRotatingFileHandler(filename=LOG_PATH, when='midnight', interval=1,
    #                                                         backupCount=2, encoding='utf-8')

    # 保留两份300M的日志(线程安全)
    rfd = logging.handlers.RotatingFileHandler(filename=LOG_PATH, mode='a', maxBytes=300 * 1024 * 1024,
                                               backupCount=2, encoding='utf-8')

    # 保留两份300M的日志(线程,进程安全)
    # rfd = ConcurrentRotatingFileHandler(filename=LOG_PATH, mode='a', maxBytes=300 * 1024 * 1024,
    #                                     backupCount=2, encoding='utf-8')

    rfd.setFormatter(fmt)
    logger.addHandler(rfd)

    return logger


logger = get_logger()
