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
from InstallApk import BatchInstallApk


class BatchInstalliOS:
    def __init__(self,root,device_iOS,index_iOS,DeviceManager):
        self.DeviceManager = DeviceManager
        self.device  = device_iOS
        self.root = root
        # ipa-ui
        # 选择ipa
        self.entry_default = StringVar()
        self.entry_default.set("请选择一个ipa文件")

        self.lab_device = tk.Label(self.root, text=device_iOS)
        self.lab_device.grid(row=index_iOS+1,column=1,stick='w')

        self.entry_apk = Entry(self.root, width=45, textvariable=self.entry_default)
        self.entry_apk.grid(row=index_iOS+1,column=2,stick='w')

        # 选择ipa
        self.select_ipa_button = tk.Button(self.root, text="选择ipa", command=self.thread_choose_file)
        self.select_ipa_button.grid(row=index_iOS+1, column=5, stick='w')

        # 安装ipa
        self.button_install_ipa = Button(self.root, text="安装", bg="LightSteelBlue", command=self.thread_install_ipa)
        self.button_install_ipa.grid(row=index_iOS+1,column=4,stick='w')

        # 卸载ipa
        self.button_uninstall_ipa = Button(self.root, text="卸载", command=self.thread_uninstall_ipa)
        self.button_uninstall_ipa.grid(row=index_iOS+1, column=3, stick='w')

        # 日志
        self.button_tid_syslog = Button(self.root, text="抓iOS日志", command=self.tidevice_syslog)
        self.button_tid_syslog.grid(row=index_iOS+1, column=7, stick='w')


    def destroy(self):
        self.select_ipa_button.destroy()
        self.button_install_ipa.destroy()
        self.button_uninstall_ipa.destroy()
        self.button_tid_syslog.destroy()
        # self.button_delete_GCloudlog.destroy()
        # self.button_pull_GCloudlog.destroy()
        # self.button_delete_Corelog.destroy()
        # self.button_pull_Corelog.destroy()
        self.entry_apk.destroy()
        self.lab_device.destroy()

    def tidevice_syslog(self):
        print("iOS_device",self.device)
        device_name = self.device
        platform_system = platform.system()
        Win = "Windows"
        if platform_system == Win:
            computer_save_path = self.DeviceManager.get_logcat_path() +'\\' + device_name+"\\" # 本地的路径，存在指定的文件夹再加上设备名作为区分
        else:
            computer_save_path = self.DeviceManager.get_logcat_path() +'/' + device_name+"/" # 本地的路径，存在指定的文件夹再加上设备名作为区分
        print("iOS日志保存到本地的路径：%s"%computer_save_path)

        if not os.path.exists(computer_save_path):
            os.makedirs(computer_save_path)
        logcat_name = self.set_file_name() + ".log"
        tidevice_syslog = 'tidevice --udid {0} syslog >{1}'.format(self.device, computer_save_path) + logcat_name
        print(tidevice_syslog)
        os.popen(tidevice_syslog)

    def choose_file(self):
        selectFileName = tkinter.filedialog.askopenfilename(title='选择文件')  # 选择文件
        self.entry_default.set(selectFileName)

    def set_file_name(self):#设置文件名
         now=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
         return now

    def install_ipa(self):
        # 安装ipa
        tid_install = 'tidevice --udid {0} install {1}'.format(self.device,self.entry_apk.get())
        print("installing ", tid_install)
        os.system(tid_install)

    def uninstall_ipa(self):
        # 卸载apk
        # adb_install = "adb -s " + self.device + " install -r " + self.DeviceManager.get_apk_path() + "\\" + self.entry_apk.get())
        tid_uninstall = 'tidevice --udid {0} uninstall com.tencent.itop.example'.format(self.device)
        print("uninstalling ", tid_uninstall)
        os.system(tid_uninstall)

    def thread_choose_file(self):
        t4 = threading.Thread(target=self.choose_file, )
        t4.start()

    def thread_install_ipa(self):     #用多线程来安装，不然点击安装后会卡住主线程，无法实现多apk同时安装
        t5 = threading.Thread(target=self.install_ipa, )
        t5.start()

    def thread_uninstall_ipa(self):   #用多线程来卸载，不然点击卸载后可能会卡住主线程
        t6 = threading.Thread(target=self.uninstall_ipa, )
        t6.start()