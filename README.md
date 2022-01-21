## Batch installer3.0

## 工具介绍
实现批量安装Apk的安装器（以下简称Bti），依赖Python3环境。支持Windows/Mac系统，支持批量安装不同的Apk，支持抓取Logcat实时日志、导出组件日志。因为采用了多线程，批量安装时单台设备安装的时间比手动要慢一些。

## 依赖环境
**Python3**  
**adb**

## 界面介绍


## 脚本简要介绍
+ InstallItem.py：导入tkinter模块，主要定义了一些界面的button。将安装Apk、抓实时日志、导出日志的adb命令封装成了函数等。
+ DeviceManager.py：导入tkinter模块，定义了一些界面的输入框，部分关于模拟器的button。实现adb连接、刷新adb、关闭adb、选择Apk根目录等功能。
+ Main.py：启动安装器（DeviceManager）的脚本。

## 执行
+ 执行Main.py会启动一个DeviceManager的界面，在界面操作所需的功能。
+ 执行Main.py可以选择在Pycharm里面执行，也可以在Windows系统的cmd面板（Mac系统的终端面板）通过输入命令"python Main.py"(Main.py存放的绝对路径)执行。

## 适用场景
+ 兼容性测试批量安装Apk；
+ Bti可快速抓取实时日志，导出日志，删除日志；
+ 当需要抓实时日志又需要运用adb命令在Windows系统的cmd面板（Mac系统的终端面板）处理一些其它的事情时，比如给安装在设备上的测试应用的输入框传入一串数据，不方便。运用Bti抓日志可解放出Windows系统的cmd面板（Mac系统的终端面板）。

## 其他说明
+ 使用micro或type-c数据线插入Androi设备，需要点击[刷新adb]，点击[关闭adb]或者[停止抓logcat日志]按钮之后需要重新点击2次[刷新adb]。
+ 点击卸载的button默认卸载的是packageName为xxxxx的Apk。
+ 当前已知问题：导出日志的设备有大量的组件日志时，（200M以上）此时界面会出现卡顿情况。

