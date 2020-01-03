#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess


def log(filename='test.log', rex='PRETTYLOGGER'):
    # 以append形式打开(创建)文件
    file = open(filename, 'a')
    # 要执行的终端指令 -s 后面接过滤的tag
    order = 'adb logcat -s '
    # 创建管道
    pi = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
    # t用来标记输出行数，每10行刷新到文件中一次
    t = 0
    try:
        # 遍历每行
        for i in iter(pi.stdout.readline, 'b'):
            # 将得到字节转码成utf-8，然后写入文件
            # 第二个参数防止使用默认参数会报出转换异常, 'ignore'会过滤掉特殊符号
            file.write(i.decode('utf-8', 'ignore'))
            t = t+1
            # 当达到10行时，将数据刷到文件中
            if t == 10:
                t = 0
                file.flush()
    except BaseException as e:
        print(e)
    finally:
        if file.closed:
            pass
        else:
            file.close()
        pi.terminate()


log()