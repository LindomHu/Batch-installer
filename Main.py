#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time
# @Author  : Huix
# @File
# @Software: PyCharm

import multiprocessing
from DeviceManager import DeviceManager

# Main.py   启动工具入口脚本



if __name__ == "__main__":
    multiprocessing.freeze_support()#不加这句打包成exe后会出现死循环
    apkInstaller= DeviceManager()
    apkInstaller.mainloop()