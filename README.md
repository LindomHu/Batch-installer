
## Batch installer

## 工具介绍
实现批量安装Apk的安装器，依赖Python3。可支持批量安装不同的Apk，Logcat日志抓取、GCloud日志导出。因为采用了多线程，单台设备安装币手动要慢一些。

## 界面介绍

![avatar](https://github.com/LindomHu/Python-Study_90/blob/ce1d18d88ee94a2e2b66795106ce184d0621c9cc/OldBoyStudy/16415386396895.png?raw=true)

“请输入apk完整包名”输入的路径不需要带上Apk的根目录，例如apk包在F:\Apk\test.apk路径下，则输入框输入Apk\test.apk。

## 脚本简要介绍
1. InstallItem.py：导入tkinter模块，主要定义了一些界面的button。将安装Apk、导出日志以及抓日志的adb命令封装成函数等。
2. DeviceManager.py：导入tkinter模块，定义了一些界面的输入框，部分关于模拟器的button。实现adb连接、刷新adb、关闭adb的功能。
3. Main.py：启动安装器（DeviceManager）的脚本。

## 执行
执行Main.py会启动一个DeviceManager的界面，在界面操作所需的功能。
