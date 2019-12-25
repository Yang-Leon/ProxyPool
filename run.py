#!/usr/bin/env python
# -*- coding:utf-8 -*-
from core.scheduler import Scheduler


def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()
