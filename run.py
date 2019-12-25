#!/usr/bin/env python
# -*- coding:utf-8 -*-
from config import *
from core.scheduler import Scheduler

# 是否记录日志
print = logger.info if (RUN_TYPE == 1) else print


def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()
