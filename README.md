
## Batch installer

## 工具介绍
实现批量安装Apk的安装器（简称Bti），依赖Python3环境。可支持批量安装不同的Apk，支持抓取Logcat实时日志、导出Cloud/GCloudCore日志。因为采用了多线程，批量安装时单台设备安装的时间手动要慢一些。
### 批量安装不同的Apk说明
1. 当所要安装的不同Apk在同一个根目录下时：选择该根目录，批量安装即可；
2. 当所要安装的不同ApK不在同一个根目录时：需要手动分别选择（或填入）各个Apk的根目录逐台依次安装。

## 界面介绍

![avatar](https://github.com/LindomHu/Python-Study_90/blob/ce1d18d88ee94a2e2b66795106ce184d0621c9cc/OldBoyStudy/16415386396895.png?raw=true)

“请输入apk完整包名”输入框：输入apk包名（名字）。

## 脚本简要介绍
1. InstallItem.py：导入tkinter模块，主要定义了一些界面的button。将安装Apk、抓实时日志、导出日志的adb命令封装成了函数等。
2. DeviceManager.py：导入tkinter模块，定义了一些界面的输入框，部分关于模拟器的button。实现adb连接、刷新adb、关闭adb、选择Apk根目录等功能。
3. Main.py：启动安装器（DeviceManager）的脚本。

## 执行
执行Main.py会启动一个DeviceManager的界面，在界面操作所需的功能。

## 其他说明
1. 由于Mac系统和Windows系统的电脑磁盘有差异，且Mac系统上需要将日志保存到Users/用户名/目录下，所以在Mac上使用时需要手动填入日志保存路径。
2. 卸载的button卸载的是packageName为com.tencent.itop.example的Apk。
