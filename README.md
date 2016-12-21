### GoogleSSLdomainFinder 使用指引

####简要介绍
GoogleSSLdomainFinder是为方便使用[谷歌透明证书查询](https://www.google.com/transparencyreport/)的python脚本(基于XX-Net的代理访问Google)，而使用谷歌透明证书查询子域名准确率较高，同时也存在漏掉部分域名的不足，因此可一定程度上协助渗透测试，此外，此项目也是 @CNSISMO 开发中的某项目模块。

####使用方法

- 首先确保电脑已经安装上python 2.7或者更高版本
- 安装[XX-Net](https://github.com/XX-net/XX-Net/wiki/%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3)
  
简要安装方法，下载https://codeload.github.com/XX-net/XX-Net/zip/3.2.7=>解压=>运行start.vbs(windows)/start(unix/linux)=>导入浏览器插件和证书=>等待xx-net扫描IP完成,大概30分钟左右

- 请保证xx-net运行在127.0.0.1:8087,可访问127.0.0.1:8085查看
- 下载[本脚本](https://github.com/We5ter/GoogleSSLdomainFinder/archive/master.zip)，解压
- 运行前请保证xx-net持续运行，进入解压后目录，运行`python GoogleSSLdomainFinder.py`

####运行效果图

- 初始状态

![1](https://github.com/We5ter/GoogleSSLdomainFinder/blob/master/example/ex1.png)

- help文档

![3](https://github.com/We5ter/GoogleSSLdomainFinder/blob/master/example/ex3.png)

- 查询示例

![2](https://github.com/We5ter/GoogleSSLdomainFinder/blob/master/example/ex2.png)

&copy;Wester 2016 持续更新中...
