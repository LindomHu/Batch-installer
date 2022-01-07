#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time
# @Author  : Huix
# @File
# @Software: PyCharm


# -*- coding: utf-8 -*-
import os
import tkinter as tk
from tkinter import *  # 导入 Tkinter 库
import multiprocessing
import threading
from InstallItem import InstallItem


class DeviceManager():

    def __init__(self):
        try:
            # cmd = 'adb connect 127.0.0.1:7555'  # 木木模拟器比较常用，所以写在程序里
            cmd = 'adb connect 127.0.0.1:5555'  # 腾讯手游模拟器比较常用，所以写在程序里
            os.system(cmd)
        except EXCEPTION as e:
            print(e)

        self.root = Tk()
        self.root.geometry('1200x450')
        self.root.title("DeviceManager")
        self.log_path=StringVar()
        self.log_path.set("F:\\DeviceManager\\GCloudLogs")
        self.logcat_path=StringVar()
        self.logcat_path.set("F:\\DeviceManager\\LogcatLogs")
        self.apk_path = StringVar()
        self.apk_path.set("F:\\")
        #连接模拟器
        self.init_port =IntVar()

        #nox模拟器  62001  第二个开始 62025+index
        self.init_port.set(5555)
        self.increase_num = IntVar()
        self.increase_num.set(1)

        self.apk_name = StringVar()
        self.apk_name.set("请输入apk完整包名")
        self.select_device_list =[]
        self.device_list = self.get_device_list()
        self.cb_list =[]
        self.pool = multiprocessing.Pool(processes=6)
        self.button_list=[]
        self.button_delete_log_list=[]
        self.button_pull_log_list=[]
        self.button_logcat_log_list=[]
        self.install_item_list=[]


    def get_log_path(self):#得到log存放路径
        return self.log_path.get()

    def get_logcat_path(self):#得到log存放路径
        return self.logcat_path.get()

    def get_apk_path(self):#得到apk更目录路径
        return self.apk_path



    def draw_log_path(self):
        label_log=tk.Label(self.root, text="GCloud日志保存路径:")
        label_log.grid(row=0,column=1,sticky='w')

        entry_log_path = Entry(self.root, width=50, textvariable=self.log_path)
        entry_log_path.grid(row=0,column=2,sticky='w')

        # print(entry_log_path)
        button_open_log = Button(self.root, text="打开", command=lambda: self.open_file(entry_log_path.get()))
        button_open_log.grid(row=0 ,column=4)

        label_logcat=tk.Label(self.root, text="Logcat日志保存路径:")
        label_logcat.grid(row=1,column=1,sticky='w')

        entry_logcat_path = Entry(self.root, width=50, textvariable=self.logcat_path)
        entry_logcat_path.grid(row=1,column=2,sticky='w')

        button_open_logcat_path = Button(self.root, text="打开", command=lambda: self.open_file(entry_logcat_path.get()))
        button_open_logcat_path.grid(row=1 ,column=4)

        #刷新adb
        button_refresh = Button(self.root,text="刷新adb",bg="LightSteelBlue",command=lambda:self.refresh_adb())
        button_refresh.grid(row=0,column=8)
        #关闭adb
        button_close_adb = Button(self.root,text="关闭adb",command=self.close_adb)
        button_close_adb.grid(row=0,column=9)
        #连接模拟器
        button_connect_device = Button(self.root, text="连接模拟器", command=self.start_connect_device_thread)
        button_connect_device.grid(row=1, column=12)

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


    def refresh_adb(self):
        print("刷新adb")
        try:
            cmd1 = 'adb devices'
            # cmd2 = 'adb connect 127.0.0.1:5555'  #解决如果先运行工具（脚本），再启动腾讯手游助手，刷新 adb 手游助手刷不出来的问题
            os.popen(cmd1)
            # os.popen(cmd2)
        except EXCEPTION as e:
            print(e)

        old_device_list =self.device_list
        new_device_list =self.get_device_list()
        #old-new 的差集用old_new表示
        old_new  = set(old_device_list)-set(new_device_list)
        print("old-new:",list(old_new))
        for item in self.install_item_list:
            if item.device in list(old_new):
                item.destroy()

        #new-old 的差集用new_old表示
        new_old = set(new_device_list)-set(old_device_list)
        start_draw_index =  len(set(old_device_list)&set(new_device_list))
        self.draw_installer_item(list(new_old),start_draw_index)
        self.device_list=new_device_list

    def connect_device(self,index):
        try:
            port =self.init_port.get()+index
            print(port)
            cmd = 'adb connect 127.0.0.1:'+str(port)
            print(cmd)
            os.system(cmd)
        except:
            print("连接第%d个模拟器有问题" % index)

    def start_connect_device_thread(self):
        print(self.increase_num.get())
        for i in range(self.increase_num.get()):
            t= threading.Thread(target=self.connect_device,args=(i,))
            t.start()


    def draw_apk_path(self):
        label_apk_path = tk.Label(self.root, text="APK根目录:")
        label_apk_path.grid(row=2, column=1, sticky='w')

        entry_apk_path = Entry(self.root, width=50, textvariable=self.apk_path)
        entry_apk_path.grid(row=2, column=2, sticky='w')

        button_open_apkPath = Button(self.root, text="打开", command=lambda : self.open_file(entry_apk_path.get()))
        button_open_apkPath.grid(row=2, column=4)




    def draw_installer_item(self,device_list,old_device_num=0):
        for index,device in enumerate(device_list):
            start_row=index+old_device_num+2
            install_item=InstallItem(self.root,device,start_row,self)
            self.install_item_list.append(install_item)
            self.root.grid_columnconfigure((0,3,5), minsize=20)

    def mainloop(self):
        self.draw_log_path()
        self.draw_device_connect()
        self.draw_apk_path()
        self.draw_installer_item(self.device_list)
        self.root.mainloop()

    def get_device_list(self):#得到设备列表
        os.system("adb devices")
        res = os.popen("adb devices").readlines()
        device_list = [sub.split('\t')[0] for sub in res[1:-1]]
       # device_list = [sub for sub in res[1:-1]]
        return device_list

    def open_file(self,path):#打开文件
        os.system("explorer "+path)



# if __name__=='__main__':
#     multiprocessing.freeze_support()#不加这句打包成exe后会出现死循环
#     apkInstaller= DeviceManager()
#     apkInstaller.mainloop()