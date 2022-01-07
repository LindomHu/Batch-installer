#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time
# @Author  : Huix
# @File
# @Software: PyCharm


# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *  # 导入 Tkinter 库
import os
import time
import threading

class InstallItem:

    def __init__(self,root,device,index,DeviceManager):
        self.DeviceManager = DeviceManager
        self.device  = device
        self.entry_default = StringVar()
        self.entry_default.set("请输入apk完整包名")

        self.root=root
        self.lab_device = tk.Label(self.root, text=device)
        self.lab_device.grid(row=index+1,column=1,stick='w')

        self.entry_apk = Entry(self.root, width=65, textvariable=self.entry_default)
        self.entry_apk.grid(row=index+1,column=2,stick='w')

        self.button_install = Button(self.root, text="安装",command=self.thread_install_apk)
        self.button_install.grid(row=index+1,column=4,stick='w')

        self.button_delete_log = Button(self.root,text="删GCloud日志",command=self.delete_log)
        self.button_delete_log.grid(row=index+1,column=7,stick='w')

        self.button_pull_log = Button(self.root,text="拉GCloud日志",command=self.pull_log)
        self.button_pull_log.grid(row=index+1,column=8,stick='w')

        self.button_logcat_c = Button(self.root,text="删logcat缓存日志",command=self.logcat_c)
        self.button_logcat_c.grid(row=index+1,column=9,stick='w')

        self.button_logcat_log = Button(self.root,text="抓logcat日志",command=self.logcat_log)
        self.button_logcat_log.grid(row=index+1,column=10,stick='w')


    def destroy(self):
        self.button_install.destroy()
        self.button_delete_log.destroy()
        self.button_pull_log.destroy()
        self.button_logcat_c.destroy()
        self.button_logcat_log.destroy()
        self.entry_apk.destroy()
        self.lab_device.destroy()



    def delete_log(self):
        print("device",self.device)
        # if "emulator" in self.device or "127.0.0.1" in self.device:#如果是模拟器
        device_log_path = "sdcard/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloud"
        # else:# 如果是手机
        #     device_log_path = "/storage/emulated/0/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloud"
        if ':' in self.device:
            device_name = self.device.replace(':', '-')  # 这里用来处理模拟器多开，冒号在路径名中无法使用，所以替换一下
        else:
            device_name = self.device

        cmd_delete = 'adb -s {0} shell rm -rf {1}'.format(self.device, device_log_path)
        print(cmd_delete)
        os.system(cmd_delete)


    def pull_log(self):
        print("device",self.device)
        # if "emulator" in self.device or "127.0.0.1" in self.device:#如果是模拟器
        device_log_path = "sdcard/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloud"
        # else:# 如果是手机
        #     device_log_path = "/storage/emulated/0/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloud"
        if ':' in self.device:
            device_name = self.device.replace(':', '-')  # 这里用来处理模拟器多开，冒号在路径名中无法使用，所以替换一下
        else:
            device_name = self.device
        computer_copy_path = self.DeviceManager.get_log_path() +'\\' + device_name+"\\" # 本地的路径，存在指定的文件夹再加上设备名作为区分
        print("\033[1;32;40mGCloud日志拉取到本地的路径：%s\033[0m"%computer_copy_path)

        if not os.path.exists(computer_copy_path):
            os.makedirs(computer_copy_path)
        # print(self.DeviceManager.get_log_path())
        cmd_pull = 'adb -s {0} pull {1} {2}'.format(self.device, device_log_path, computer_copy_path)
        # print(cmd)
        os.system(cmd_pull)

    def logcat_c(self):
        print("device",self.device)
        if ':' in self.device:
            device_name = self.device.replace(':', '-')  # 这里用来处理模拟器多开，冒号在路径名中无法使用，所以替换一下
        else:
            device_name = self.device


        cmd_logcat_c = 'adb -s {0} logcat -c'.format(self.device)
        print(cmd_logcat_c)
        os.popen(cmd_logcat_c)

    def logcat_log(self):
        print("device",self.device)
        if ':' in self.device:
            device_name = self.device.replace(':', '-')  # 这里用来处理模拟器多开，冒号在路径名中无法使用，所以替换一下
        else:
            device_name = self.device
        computer_save_path = self.DeviceManager.get_logcat_path() +'\\' + device_name# 本地的路径，存在指定的文件夹再加上设备名作为区分
        print("\033[1;32;40mlogcat日志保存到本地的路径：%s\033[0m"%computer_save_path)

        if not os.path.exists(computer_save_path):
            os.makedirs(computer_save_path)
        logcat_name = self.set_file_name() + ".log"
        cmd_logcat = 'adb -s {0} logcat -v time >{1}\\' .format(self.device, computer_save_path) + logcat_name
        print(cmd_logcat)
        os.popen(cmd_logcat)


    def set_file_name(self):#设置文件名
         now=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
         return now

    def install_apk(self):
        # 安装游戏
        # print(self.entry_apk.get())
        # cmd_install = "adb -s " + self.device + " install -r " + self.DeviceManager.get_apk_path() + "\\" + self.entry_apk.get())
        cmd_install = "adb -s {0} install -r {1}\\{2}".format(self.device,self.DeviceManager.apk_path.get(),self.entry_apk.get())
        print("installing ", cmd_install)
        os.system(cmd_install)

    def thread_install_apk(self):#用多线程来安装，不然点击安装后会卡住主线程，无法实现多apk同时安装
        t = threading.Thread(target=self.install_apk, )
        t.start()