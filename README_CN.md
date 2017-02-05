## GoogleSSLdomainFinder 使用指引

**仓库名已缩短为GSDF,原链接https://github.com/We5ter/GoogleSSLdomainFinder 会自动重定向到现在的链接**

####简要介绍
GoogleSSLdomainFinder是为方便使用<a href="https://www.google.com/transparencyreport/" target="_blank">谷歌透明证书查询</a>的python脚本(基于XX-Net访问Google)，而使用谷歌透明证书查询子域名准确率较高，但是也存在部分子域名被漏掉的不足，可在一定程度上协助渗透测试，此外，此项目也是 @CNSISMO 开发中的某项目模块。

<hr>

####更迭记录

- 2016.12.21 增加文件记录功能
- 2016.12.22 增加api库
- 2017.01.05 完成api库，使用方法：
  <pre><code>from GSDFA import GoogleSSLdomainFinder
  do = GoogleSSLdomainFinder('mi.com')
  do.list()  #输出为列表
  </code></pre>
  
<hr>

####使用方法

- 首先确保电脑已经安装上python 2.7或者更高版本

- 确保访问google,安装[XX-Net](https://github.com/XX-net/XX-Net/wiki/%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3)(如已安装，可忽略本步骤，简要安装过程如下)<br>
<pre><code>下载https://codeload.github.com/XX-net/XX-Net/zip/3.2.7=>解压=>运行start.vbs(windows)/start(unix/linux)=>导入浏览器插件和证书=>等待xx-net扫描IP完成,大概30分钟左右
</code></pre>
**注：如果你使用Shadowsocks等方式访问Google，可暂时去掉脚本66行的proxies=proxies,之后的更新会提供是否选择XX-Net代理**

- 运行XX-Net,请保证xx-net运行在127.0.0.1:8087(默认),可访问127.0.0.1:8085查看

- 下载[本脚本](https://github.com/We5ter/GoogleSSLdomainFinder/archive/master.zip)，解压并进入解压后的目录

- 运行`python GSDFT.py`，即Terminal version，运行中请保证xx-net持续运行；

- 输出结果以表格形式展示在终端，同时写入txt文件

####Terminal version运行效果图

- 初始状态

<img src="https://github.com/We5ter/GoogleSSLdomainFinder/blob/master/example/ex1.png" width="500px">

- help文档

<img src="https://github.com/We5ter/GSDF/blob/master/example/Screen%20Shot%202017-01-09%20at%207.13.57%20PM.png" width="500px">

- 查询示例

<img src="https://github.com/We5ter/GSDF/blob/master/example/Screen%20Shot%202017-01-09%20at%207.14.27%20PM.png" width="500px">


<hr>

####维护信息
- &copy;2016 Wester@CNSISMO
- 作者blog:<a href="https://lightrains.org" target="_blank">https://lightrains.org</a>
