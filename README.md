### 程序使用介绍

调用了 [Remove.bg](https://www.remove.bg/api) 的 API 接口，用 Python 的 PIL 包处理，只需要简单敲几下键盘，就可以随意批量更换照片的背景色（常见的白、蓝、红三种颜色），然后秒换背景出图。

不仅是证件照，只要是有清晰前景的人或物品都可以抠。

操作效果如下：


![mark](http://media.makcyun.top/win/20190724/DLa5GBHwfuzL.gif)

http://media.makcyun.top/win/20190724/DLa5GBHwfuzL.gif

具体实现很简单，第一步输入 API，第二步输入图片所在文件夹，接着程序就会先抠图，生成带透明背景的 PNG 格式图形。

接下来第三步利用 PIL 库来设置图片的背景颜色，键入一个字母就可以秒生成对应的背景色证件照。

- b：blue 蓝色
- r：red 红色
- w：white 白色

这样就做成了一个简单的证件照更换工具，更换证件照背景色的整个过程，一分钟就可以完成。拿去开个淘宝店感觉应该没太大问题，专注处理证件照，定价 2 元，哈哈哈。

### FAQ

#### 关于 API

需要自行邮箱注册个账号才能获取，每个账号每月可以抠 50 张标清照片，要想抠更多或者高清图片，需要付费。提供个批量生成邮箱账号的方法：

[一元 100 个网易邮箱](http://baidca.com/item-35.html)



#### 关于无法抠图

弹框选择文件夹时只需要选择到文件夹所在位置即可，不需要进到文件夹内部：

![](http://media.makcyun.top/FvBEHtoojt03PA4esIVbDW39Zwa9)



最后欢迎关注我的公众号，Python 爬虫、数据分析、佳软神器应有尽有：

![](http://media.makcyun.top/FjTddugyNsm2rsuinVtuUPSRRwaU)
