import os
import signal
import subprocess
import pytest


# 设置record_vedio函数的执行级别，此为模块级别；autouse=True 会自动调用
@pytest.fixture(scope='module', autouse=True)
def record_vedio():
    cmd = "scrcpy --record file.mp4"
    # subprocess 是python的一个特性:条用命令行 subprocess.Popen() 打开一个需要录屏的管道
    # shell=True ： 命令自动切割  会自动识别运行，不加的话需要手动切割
    # stdout：标准输出管道   正常运动后的结果会放到stdout管道
    # stderr： 错误输出管道  运行报错后将会把错误信息放到stderr管道  （这样不管是执行正确或错误都会打印）
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    # 相当于retur，但是不同与return的是，在yield后的代码也会执行
    yield
    # signal.CTRL_C_EVENT 模仿ctrl+c的动作
    os.kill(p.pid, signal.CTRL_C_EVENT)
