## Batch installer3.0

## 工具介绍
实现批量安装Apk的安装器（简称Bti），依赖Python3环境。可支持批量安装不同的Apk，支持抓取Logcat实时日志、导出Cloud/GCloudCore日志。因为采用了多线程，批量安装时单台设备安装的时间手动要慢一些。

## 依赖环境
**Python3**  
**adb**

## 界面介绍

![avatar](https://github.com/LindomHu/Python-Study_90/blob/ce1d18d88ee94a2e2b66795106ce184d0621c9cc/OldBoyStudy/16415386396895.png?raw=true)


## 脚本简要介绍
+ InstallItem.py：导入tkinter模块，主要定义了一些界面的button。将安装Apk、抓实时日志、导出日志的adb命令封装成了函数等。
+ DeviceManager.py：导入tkinter模块，定义了一些界面的输入框，部分关于模拟器的button。实现adb连接、刷新adb、关闭adb、选择Apk根目录等功能。
+ Main.py：启动安装器（DeviceManager）的脚本。

## 执行
+ 执行Main.py会启动一个DeviceManager的界面，在界面操作所需的功能。
+ 执行Main.py可以选择在Pycharm里面执行，也可以在Windows系统的dos面板（Mac系统的终端面板）通过输入命令"python Main.py"(Main.py存放的绝对路径)执行。

## 适用场景
+ 兼容性测试批量安装Apk
+ 可快速抓取实时日志，导出日志，删除日志。

## 其他说明
+ 使用micro或type-c数据线插入Androi设备，需要点击[刷新adb]，点击[关闭adb]/[停止抓logcat日志]之后需要重新点击2次[刷新adb]。
+ 点击卸载的button默认卸载的是packageName为com.tencent.itop.example的Apk。
+ 当前已知问题：导出日志的设备有大量的GCloud/GCloudCore日志时，（200M以上）此时导出GCloud/GCoudCore日志界面会出现卡顿情况。

