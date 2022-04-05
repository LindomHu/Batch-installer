#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time
# @Author  : Huix
# @File
# @Software: PyCharm


import os
import tkinter as tk
from tkinter import *  # 导入 Tkinter 库
from tkinter.filedialog import askdirectory
import multiprocessing
import threading
import platform
import getpass
from InstallApk import InstallApk
# from adbutils import devices


class DeviceManager():

    def __init__(self):
        try:
            cmd = 'adb connect 127.0.0.1:5555'  # 腾讯手游模拟器比较常用，所以写在程序里
            os.system(cmd)
        except EXCEPTION as e:
            print(e)

        self.root = Tk()
        self.root.geometry('1615x420')
        self.root.title("DeviceManager")
        self.user = getpass.getuser()
        platform_system = platform.system()
        if platform_system == "Windows":
            self.win_logcat_path = ("D:\\DeviceManager\\LogcatLog")
            self.logcat_path = StringVar()
            self.logcat_path.set(self.win_logcat_path)

            self.win_GCloudlog_path = ("D:\\DeviceManager\\GCloudSDKLog")
            self.GCloudlog_path=StringVar()
            self.GCloudlog_path.set(self.win_GCloudlog_path)

            self.win_Corelog_path = ("D:\\DeviceManager\\GCloudSDKLog")
            self.Corelog_path = StringVar()
            self.Corelog_path.set(self.win_Corelog_path)

            self.win_GVoicelog_path = ("D:\\DeviceManager\\GCloudSDKLog")
            self.GVoicelog_path = StringVar()
            self.GVoicelog_path.set(self.win_GVoicelog_path)

        else:
            self.mac_logcat_path = ("/Users/" + self.user + "/Downloads/LogcatLog")
            self.logcat_path = StringVar()
            self.logcat_path.set(self.mac_logcat_path)

            self.mac_GCloudlog_path = ("/Users/" + self.user + "/Downloads/GCloudSDKLog")
            self.GCloudlog_path=StringVar()
            self.GCloudlog_path.set(self.mac_GCloudlog_path)

            self.mac_Corelog_path = ("/Users/" + self.user + "/Downloads/GCloudSDKLog")
            self.Corelog_path = StringVar()
            self.Corelog_path.set(self.mac_Corelog_path)

            self.mac_GVoicelog_path = ("/Users/" + self.user + "/Downloads/GCloudSDKLog")
            self.GVoicelog_path = StringVar()
            self.GVoicelog_path.set(self.mac_GVoicelog_path)

        #连接模拟器
        self.init_port =IntVar()

        #手游助手模拟器  5555  第二个开始 5555+index
        self.init_port.set(5555)

        self.increase_num = IntVar()
        self.increase_num.set(1)
        self.apk_name = StringVar()
        self.apk_name.set("请选择一个Apk或输入apk完整路径")
        self.select_device_list =[]
        self.device_list = self.get_device_list()
        self.cb_list =[]
        self.pool = multiprocessing.Pool(processes=6)
        self.button_list=[]
        self.button_logcat_c_list = []
        self.button_logcat_log_list = []
        self.button_delete_GCloudlog_list=[]
        self.button_pull_GCloudlog_list=[]
        self.button_delete_Corelog_list = []
        self.button_pull_Corelog_list = []
        self.button_delete_GVoicelog_list = []
        self.button_pull_GVoicelog_list = []
        self.install_item_list = []
        self.uninstall_item_list = []

    def get_logcat_path(self):	#得到log存放路径
        return self.logcat_path.get()

    def get_GCloudlog_path(self):	#得到log存放路径
        return self.GCloudlog_path.get()

    def get_Corelog_path(self):	 #得到log存放路径
        return self.Corelog_path.get()

    def get_GVoicelog_path(self):	#得到log存放路径
        return self.GVoicelog_path.get()

    # def get_apk_path(self):	#得到apk更目录路径
    #     return self.apk_path

    def item_device_return(self):	#得到log存放路径
        self.device_list = StringVar()
        return self.device_list.get()

    def draw_log_path(self):
        label_logcat=tk.Label(self.root, text="Logcat日志保存外层路径:")
        label_logcat.grid(row=0,column=1,sticky='w')

        entry_logcat_path = Entry(self.root, width=45, textvariable=self.logcat_path)
        entry_logcat_path.grid(row=0,column=2,sticky='w')

        button_open_logcat_path = Button(self.root, text="打开", command=lambda: self.open_file(entry_logcat_path.get()))
        button_open_logcat_path.grid(row=0 ,column=4)

        label_log1 = tk.Label(self.root, text="GCloud日志保存外层路径:")
        label_log1.grid(row=1, column=1, sticky='w')

        entry_log_path1 = Entry(self.root, width=45, textvariable=self.GCloudlog_path)
        entry_log_path1.grid(row=1, column=2, sticky='w')

        button_open_log1 = Button(self.root, text="打开", command=lambda: self.open_file(entry_log_path1.get()))
        button_open_log1.grid(row=1, column=4)

        label_log2 = tk.Label(self.root, text="GCloudCore日志保存外层路径:")
        label_log2.grid(row=2, column=1, sticky='w')

        entry_log_path2 = Entry(self.root, width=45, textvariable=self.Corelog_path)
        entry_log_path2.grid(row=2, column=2, sticky='w')

        button_open_log2 = Button(self.root, text="打开", command=lambda: self.open_file(entry_log_path2.get()))
        button_open_log2.grid(row=2, column=4)

        label_log3 = tk.Label(self.root, text="GVoice日志保存外层路径:")
        label_log3.grid(row=3, column=1, sticky='w')

        entry_log_path3 = Entry(self.root, width=45, textvariable=self.GVoicelog_path)
        entry_log_path3.grid(row=3, column=2, sticky='w')

        button_open_log3 = Button(self.root, text="打开", command=lambda: self.open_file(entry_log_path3.get()))
        button_open_log3.grid(row=3, column=4)

        # 刷新adb
        button_refresh = Button(self.root, text="刷新adb", bg="LightSteelBlue", command=lambda: self.refresh_adb())
        button_refresh.grid(row=0, column=7)
        # 关闭adb
        button_close_adb = Button(self.root, text="关闭adb", bg="DarkGray",command=self.close_adb)
        button_close_adb.grid(row=0, column=9)

        # 连接模拟器
        button_connect_device = Button(self.root, text="连接模拟器", command=self.start_connect_device_thread)
        button_connect_device.grid(row=0, column=10)

        # 连接云真机
        button_connect_device = Button(self.root, text="连接云真机", command=self.start_connect_cloud_device_thread)
        button_connect_device.grid(row=0, column=11)

        # 过关闭adb停止抓logcat日志
        button_close_adb = Button(self.root, text="停止抓logcat日志", bg="DarkGray",command=self.close_adb)
        button_close_adb.grid(row=0, column=12)

    def draw_device_connect(self):
        label_device_start_port = tk.Label(self.root,text="起始端口:")
        label_device_start_port.grid(row=1,column=7,sticky='w')

        entry_device_start_port = Entry(self.root, width=5, textvariable=self.init_port)
        entry_device_start_port.grid(row=1,column=8,sticky='w')

        label_device_num = tk.Label(self.root, text="连接数量:")#模拟器多开时想要连接的数量
        label_device_num.grid(row=1, column=9, sticky='w')

        entry_device_num = Entry(self.root, width=5, textvariable=self.increase_num)
        entry_device_num.grid(row=1, column=10, sticky='w')



    def close_adb(self):
        print("关闭 adb")
        try:
            cmd = 'adb kill-server'
            os.system(cmd)
        except EXCEPTION as e:
            print(e)


    def refresh_adb(self, start_row=0):
        print("刷新adb")
        try:
            # cmd_kill_adb = 'adb kill-server'
            cmd_start_adb = 'adb start-server'
            cmd1 = 'adb devices'
            # cmd2 = 'adb connect 127.0.0.1:5555'  #解决如果先运行工具（脚本），再启动腾讯手游助手，刷新 adb 手游助手刷不出来的问题
            # os.popen(cmd_kill_adb)
            os.popen(cmd_start_adb)
            os.popen(cmd1)
        
            # os.popen(cmd2)
        except EXCEPTION as e:
            print(e)
     
        
        old_device_list = self.device_list   # 原来连接的设备
        new_device_list = self.get_device_list()  # ==>adb device
        #old-new 的差集用old_new表示
        old_new  = set(old_device_list)-set(new_device_list)
        for item in  (self.install_item_list):
            if item.device in list(old_new):
                item.destroy()

        #new-old 的差集用new_old表示
        new_old = set(new_device_list)-set(old_device_list)         # 原来的设备 a  新插入一台b   ==b
        start_draw_index =  len(set(old_device_list)&set(new_device_list))  # a—>len
        old_new_jiao = set(old_device_list)&set(new_device_list)
        cur_device = list(old_new_jiao) + list(new_old)
        # cur_device = list(reversed(cur_device1))
        result = set(new_device_list).issubset(set(cur_device))
        if result == True:
            for item1 in  (self.install_item_list):
                if item1.device in list(cur_device):
                    item1.destroy()
        self.draw_installer_item(cur_device,start_draw_index+1)    # ((b),1)
        self.device_list=new_device_list

    def connect_device(self,index):
        try:
            port =self.init_port.get()+index
            print(port)
            cmd = 'adb connect 127.0.0.1:'+ str(port)
            print(cmd)
            os.system(cmd)
        except:
            print("连接第%d个模拟器有问题" % index+1)

    def connect_cloud_device(self,index):
        try:
            port =self.init_port.get()+index
            print(port)
            cmd = 'adb connect 119.29.201.189:'+ str(port)
            print(cmd)
            os.system(cmd)
        except:
            print("连接第%d个云真机有问题" % index+1)

    def start_connect_device_thread(self):
        for i in range(self.increase_num.get()):
            t= threading.Thread(target=self.connect_device,args=(i,))
            t.start()

    def start_connect_cloud_device_thread(self):
        for i in range(self.increase_num.get()):
            t= threading.Thread(target=self.connect_cloud_device,args=(i,))
            t.start()

    # 选择Apk根目录
    # def draw_apk_path(self):
    #     def selectPath():
    #         path_ = askdirectory()
    #         path.set(path_)
    #     path = StringVar()
    #     self.apk_path = path
    #     self.apk_path = StringVar()
    #     self.apk_path.set("D:\\")
    #     label_apk_path = tk.Label(self.root, text="APK根目录:")
    #     label_apk_path.grid(row=3, column=1, sticky='w')
    #
    #     entry_apk_path = Entry(self.root, width=45, textvariable=self.apk_path)
    #     entry_apk_path.grid(row=3, column=2, sticky='w')
    #
    #     button_select_apkPath = Button(self.root, text="选择", command=selectPath)
    #     button_select_apkPath.grid(row=3, column=4)

    def get_device_list(*args, **kwargs):  #得到设备列表
        os.system("adb devices")
        res = os.popen("adb devices").readlines()
        device_list = [sub.split('\t')[0] for sub in res[1:-1]]
       # device_list = [sub for sub in res[1:-1]]
        return device_list

    def draw_installer_item(self,device_list,old_device_num=0):
        for index, device in enumerate(device_list):
            start_row=index + old_device_num + 2
            install_item=InstallApk(self.root,device,start_row,self)
            self.install_item_list.append(install_item)
            self.root.grid_columnconfigure((0,3,5), minsize=20)

    def draw_label_text(self):
        label_text1 = tk.Label(self.root, text="提示：点击[关闭adb]/[停止抓logcat日志]之后需要重新点击2次[刷新adb]",
                              foreground="Yellow",background="Gray",)
        label_text1.place(x=772,y=62)
        label_text2 = tk.Label(self.root, text="已知问题：点击[刷新adb]会偶现卡顿现象，导出的日志达到100M左右会卡顿",
                              foreground="Yellow",background="Gray",)
        label_text2.place(x=772,y=85.5)

    def mainloop(self):
        self.draw_log_path()
        self.draw_device_connect()
        # self.draw_apk_path()
        self.draw_installer_item(self.device_list)
        self.draw_label_text()
        self.root.mainloop()

    def open_file(self,path):  #打开文件
        print("path:",path)
        os.system("explorer "+path)
