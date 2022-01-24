## Batch installer3.0

## 工具介绍
批量安装器是用Python语言编写的，实现批量安装Apk的安装器。主要对adb连接、adb安装、adb logcat、adb导出日志等命令封装成了Python函数，并做了界面，将函数实现的功能渲染在界面。支持Windows/Mac系统，因为采用了多线程，支持批量安装不同的Apk、附带支持抓取Logcat实时日志，支持导出组件日志，文本传输。

## 依赖环境
**Python3**  
**adb**

## 界面介绍
暂无。

## 脚本简要介绍
+ InstallApk.py：导入tkinter模块，主要定义了一些界面的button。将安装Apk、抓实时日志、导出日志的adb命令封装成了函数等。
+ DeviceManager.py：导入tkinter模块，定义了一些界面的输入框，部分关于模拟器的button。实现adb连接、刷新adb、关闭adb、选择Apk根目录等功能。
+ BatchInstaller.py：启动安装器（DeviceManager）的脚本。

## 执行
+ 执行BatchInstaller.py会启动一个DeviceManager的界面，在界面操作所需的功能。
+ 执行BatchInstaller.py可以选择在Pycharm里面执行，也可以在Windows系统的cmd面板（Mac系统的终端面板）,终端进到Batch-Installer目录，通过键入命令"python BatchInstaller.py"执行。
+ Windows系统已打出exe包，如果是启动exe运行，无Python环境也可以运行。

## 适用场景
+ 兼容性测试时批量安装Apk或某些需要频繁安装测试包的场景；
+ 可快速抓取实时日志，导出日志，删除日志；
+ 抓日志可解放出Windows系统的cmd的Dos面板。（Mac系统的终端面板）比如在抓Logcat日志的同时，又需要给安装在设备上的测试包的输入框传入一串数据，不方便处理。运用批量安装器抓日志可一边抓日志，同时在面板上传数据给测试包的输入框。


## 其他说明
+ 当连接新设备（插入设备）后，需要重新点击【刷新adb】，如果刷不出来新连接的设备到界面上，需要再点一次；
+ 点击卸载demo的按钮默认卸载的是指定的测试包（apk）；
+ 当前已知问题：导出日志的设备有大量的组件日志时，（100M左右）此时点击【导出日志】界面会出现卡顿情况，最终可以导出成功。


