#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time
# @Author  : Huix
# @File
# @Software: PyCharm


# -*- coding: utf-8 -*-
import tkinter as tk
from threading import Thread
from tkinter import *  # 导入 Tkinter 库
import tkinter.filedialog
import os
import time
import threading
import platform




class InstallItem:
    def __init__(self,root,device,index,DeviceManager):
        self.DeviceManager = DeviceManager
        self.device  = device
        self.root = root
        # 选择Apk
        self.entry_default = StringVar()
        self.entry_default.set("请选择一个Apk文件")

        self.lab_device = tk.Label(self.root, text=device)
        self.lab_device.grid(row=index+1,column=1,stick='w')

        self.entry_apk = Entry(self.root, width=45, textvariable=self.entry_default)
        self.entry_apk.grid(row=index+1,column=2,stick='w')

        self.select_apk_button = tk.Button(self.root, text ="选择Apk", command = self.thread_choose_file)
        self.select_apk_button.grid(row=index+1,column=5,stick='w')

        # 安装
        self.button_install = Button(self.root, text="安装", bg="LightSteelBlue", command=self.thread_install_apk)
        self.button_install.grid(row=index+1,column=4,stick='w')

        # 卸载
        self.button_uninstall = Button(self.root, text="卸载", command=self.thread_uninstall_apk)
        self.button_uninstall.grid(row=index+1, column=3, stick='w')

        # 日志
        self.button_logcat_c = Button(self.root,text="删logcat日志",command=self.logcat_c)
        self.button_logcat_c.grid(row=index+1,column=7,stick='w')

        self.button_logcat_log = Button(self.root,text="抓logcat日志",bg="LightSteelBlue", command=self.logcat_log)
        self.button_logcat_log.grid(row=index+1,column=8,stick='w')

        self.button_delete_GCloudlog = Button(self.root,text="删GCloud日志",command=self.delete_GCloudlog)
        self.button_delete_GCloudlog.grid(row=index+1,column=9,stick='w')

        self.button_pull_GCloudlog = Button(self.root,text="拉GCloud日志",bg="LightSteelBlue", command=self.pull_GCloudlog)
        self.button_pull_GCloudlog.grid(row=index+1,column=10,stick='w')

        self.button_delete_Corelog = Button(self.root, text="删GCloudCore日志", command=self.delete_Corelog)
        self.button_delete_Corelog.grid(row=index+1, column=11, stick='w')

        self.button_pull_Corelog = Button(self.root, text="拉GCloudCore日志", bg="LightSteelBlue", command=self.pull_Corelog)
        self.button_pull_Corelog.grid(row=index+1, column=12, stick='w')

        # 安装ipa
        self.button_install_ipa = Button(self.root, text="安装ipa", bg="LightSteelBlue", command=self.thread_install_ipa)
        self.button_install_ipa.grid(row=index + 1, column=4, stick='w')

        # 卸载ipa
        self.button_uninstall_ipa = Button(self.root, text="卸载ipa", command=self.thread_uninstall_ipa)
        self.button_uninstall_ipa.grid(row=index + 1, column=3, stick='w')

        # 日志
        self.button_syslog = Button(self.root, text="抓iOS日志", command=self.logcat_c)
        self.button_syslog.grid(row=index + 1, column=7, stick='w')

    def destroy(self):
        self.select_apk_button.destroy()
        self.button_install.destroy()
        self.button_uninstall.destroy()
        self.button_logcat_c.destroy()
        self.button_logcat_log.destroy()
        self.button_delete_GCloudlog.destroy()
        self.button_pull_GCloudlog.destroy()
        self.button_delete_Corelog.destroy()
        self.button_pull_Corelog.destroy()
        self.button_install_ipa.destroy()
        self.button_uninstall_ipa.destroy()
        self.button_syslog.destroy()
        self.entry_apk.destroy()
        self.lab_device.destroy()


    def delete_GCloudlog(self):
        print("device",self.device)
        # if "emulator" in self.device or "127.0.0.1" in self.device:#如果是模拟器
        device_log_path = "sdcard/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloud"
        # else:# 如果是手机
        #     device_log_path = "/storage/emulated/0/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloud"
        if ':' in self.device:
            device_name = self.device.replace(':', '-')  # 这里用来处理模拟器多开，冒号在路径名中无法使用，所以替换一下
        else:
            device_name = self.device

        adb_delete = 'adb -s {0} shell rm -rf {1}'.format(self.device, device_log_path)
        print(adb_delete)
        os.system(adb_delete)


    def pull_GCloudlog(self):
        print("device",self.device)
        # if "emulator" in self.device or "127.0.0.1" in self.device:#如果是模拟器
        device_log_path = "sdcard/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloud"
        # else:# 如果是手机
        #     device_log_path = "/storage/emulated/0/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloud"
        if ':' in self.device:
            device_name = self.device.replace(':', '-')  # 这里用来处理模拟器多开，冒号在路径名中无法使用，所以替换一下
        else:
            device_name = self.device

        platform_system = platform.system()
        Win = "Windows"
        if platform_system == Win:
            computer_copy_path = self.DeviceManager.get_GCloudlog_path() +'\\' + device_name+"\\" # 本地的路径，存在指定的文件夹再加上设备名作为区分
        else:
            computer_copy_path = self.DeviceManager.get_GCloudlog_path() +'/' + device_name+"/" # 本地的路径，存在指定的文件夹再加上设备名作为区分
        print("GCloud日志拉取到本地的路径：%s"%computer_copy_path)

        if not os.path.exists(computer_copy_path):
            os.makedirs(computer_copy_path)
        adb_pull = 'adb -s {0} pull {1} {2}'.format(self.device, device_log_path, computer_copy_path)
        os.system(adb_pull)


    def delete_Corelog(self):
        print("device",self.device)
        # if "emulator" in self.device or "127.0.0.1" in self.device:#如果是模拟器
        device_Corelog_path = "sdcard/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloudCore"
        # else:# 如果是手机
        #     device_log_path = "/storage/emulated/0/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloud"
        if ':' in self.device:
            device_name = self.device.replace(':', '-')  # 这里用来处理模拟器多开，冒号在路径名中无法使用，所以替换一下
        else:
            device_name = self.device

        adb_delete2 = 'adb -s {0} shell rm -rf {1}'.format(self.device, device_Corelog_path)
        print(adb_delete2)
        os.system(adb_delete2)


    def pull_Corelog(self):
        print("device",self.device)
        # if "emulator" in self.device or "127.0.0.1" in self.device:#如果是模拟器
        device_Corelog_path = "sdcard/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloudCore"
        # else:# 如果是手机
        #     device_log_path = "/storage/emulated/0/Android/data/com.tencent.itop.example/cache/GCloudSDKLog/GCloud"
        if ':' in self.device:
            device_name = self.device.replace(':', '-')  # 这里用来处理模拟器多开，冒号在路径名中无法使用，所以替换一下
        else:
            device_name = self.device

        platform_system = platform.system()
        Win = "Windows"
        if platform_system == Win:
            computer_copy_path = self.DeviceManager.get_Corelog_path() +'\\' + device_name+"\\" # 本地的路径，存在指定的文件夹再加上设备名作为区分
        else:
            computer_copy_path = self.DeviceManager.get_Corelog_path() +'/' + device_name+"/" # 本地的路径，存在指定的文件夹再加上设备名作为区分
        print("GCloudCore日志拉取到本地的路径：%s"%computer_copy_path)

        if not os.path.exists(computer_copy_path):
            os.makedirs(computer_copy_path)

        adb_pull = 'adb -s {0} pull {1} {2}'.format(self.device, device_Corelog_path, computer_copy_path)
        os.system(adb_pull)

    def logcat_c(self):
        print("device",self.device)
        if ':' in self.device:
            device_name = self.device.replace(':', '-')  # 这里用来处理模拟器多开，冒号在路径名中无法使用，所以替换一下
        else:
            device_name = self.device


        adb_logcat_c = 'adb -s {0} logcat -c'.format(self.device)
        print(adb_logcat_c)
        os.popen(adb_logcat_c)

    def logcat_log(self):
        print("device",self.device)
        if ':' in self.device:
            device_name = self.device.replace(':', '-')  # 这里用来处理模拟器多开，冒号在路径名中无法使用，所以替换一下
        else:
            device_name = self.device

        platform_system = platform.system()
        Win = "Windows"
        if platform_system == Win:
            computer_save_path = self.DeviceManager.get_logcat_path() +'\\' + device_name+"\\" # 本地的路径，存在指定的文件夹再加上设备名作为区分
        else:
            computer_save_path = self.DeviceManager.get_logcat_path() +'/' + device_name+"/" # 本地的路径，存在指定的文件夹再加上设备名作为区分
        print("logcat日志保存到本地的路径：%s"%computer_save_path)

        if not os.path.exists(computer_save_path):
            os.makedirs(computer_save_path)
        logcat_name = self.set_file_name() + ".log"
        adb_logcat = 'adb -s {0} logcat -v time >{1}' .format(self.device, computer_save_path) + logcat_name
        print(adb_logcat)
        os.popen(adb_logcat)

    def choose_file(self):
        selectFileName = tkinter.filedialog.askopenfilename(title='选择文件')  # 选择文件
        self.entry_default.set(selectFileName)

    def set_file_name(self):#设置文件名
         now=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
         return now

    def install_apk(self):
        # 安装Apk
        # print(self.entry_apk.get())
        # 通过选择Apk根目录来安装
        # adb_install = "adb -s {0} install -r {1}/{2}".format(self.device,self.DeviceManager.apk_path.get(),self.entry_apk.get())
        # 选择Apk文件安装
        adb_install = 'adb -s {0} install -r "{1}"'.format(self.device,self.entry_apk.get())
        print("installing ", adb_install)
        os.system(adb_install)

    def uninstall_apk(self):
        # 卸载apk
        # adb_install = "adb -s " + self.device + " install -r " + self.DeviceManager.get_apk_path() + "\\" + self.entry_apk.get())
        adb_uninstall = "adb -s {0} uninstall com.tencent.itop.example".format(self.device)
        print("uninstalling ", adb_uninstall)
        os.system(adb_uninstall)

    def install_ipa(self):
        # 安装ipa
        tid_install = "tidevice --udid $UDID install {0}".format(self.entry_apk.get())
        print("installing ", tid_install)
        os.system(tid_install)

    def uninstall_ipa(self):
        # 卸载apk
        # adb_install = "adb -s " + self.device + " install -r " + self.DeviceManager.get_apk_path() + "\\" + self.entry_apk.get())
        tid_uninstall = "tidevice uninstall com.tencent.itop.example"
        print("uninstalling ", tid_uninstall)
        os.system(tid_uninstall)

    def thread_choose_file(self):
        t = threading.Thread(target=self.choose_file, )
        t.start()

    def thread_install_apk(self):     #用多线程来安装，不然点击安装后会卡住主线程，无法实现多apk同时安装
        t2 = threading.Thread(target=self.install_apk, )
        t2.start()

    def thread_uninstall_apk(self):   #用多线程来卸载，不然点击卸载后可能会卡住主线程
        t3 = threading.Thread(target=self.uninstall_apk, )
        t3.start()

    def thread_install_ipa(self):  # 用多线程来安装，不然点击安装后会卡住主线程，无法实现多apk同时安装
        print("多线程安装ipa")
        t5 = threading.Thread(target=self.install_ipa, )
        t5.start()

    def thread_uninstall_ipa(self):  # 用多线程来卸载，不然点击卸载后可能会卡住主线程
        print("多线程卸载ipa")
        t6 = threading.Thread(target=self.uninstall_ipa, )
        t6.start()