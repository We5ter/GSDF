## GoogleSSLdomainFinder

![GitHub issues](https://img.shields.io/github/issues/We5ter/GSDF.svg)
![GitHub forks](https://img.shields.io/github/forks/We5ter/GSDF.svg)
![GitHub stars](https://img.shields.io/github/stars/We5ter/GSDF.svg)

**README.md in [English 英文](https://github.com/We5ter/GSDF/blob/master/README.md)**

#### 简要介绍

**GoogleSSLdomainFinder**是为方便使用<a href="https://transparencyreport.google.com/https/certificates" target="_blank">谷歌透明证书查询</a>的python脚本(基于XX-Net访问Google)，而使用谷歌透明证书查询子域名准确率较高，但结果集较小。

<hr>

#### 更迭记录

- 2016.12.21 增加文件记录功能
- 2016.12.22 增加api库
- 2017.01.05 完成api库，使用方法：
  <pre><code>from GSDFA import GoogleSSLdomainFinder
  do = GoogleSSLdomainFinder('mi.com')
  do.list()  #输出为列表
  </code></pre>
  
- 2017.09.16 更新至v1.1版本

<hr>

#### 使用方法

- 首先确保电脑已经安装上python 2.7或者更高版本

- 确保访问google,安装[XX-Net](https://github.com/XX-net/XX-Net/wiki/%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3)(如已安装，可忽略本步骤，简要安装过程如下)<br>
<pre><code>下载https://codeload.github.com/XX-net/XX-Net/zip/3.2.7=>解压=>运行start.vbs(windows)/start(unix/linux)=>导入浏览器插件和证书=>等待xx-net扫描IP完成,大概30分钟左右
</code></pre>
**注意：**

如果你使用Shadowsocks访问Google，可替换脚本proxies为：
```
 self.proxies = {
            'http': 'http://127.0.0.1:1087',
            'https': 'http://127.0.0.1:1087',
            }
```

- 运行XX-Net,请保证xx-net运行在127.0.0.1:8087(默认),可访问127.0.0.1:8085查看

- 下载[本脚本](https://github.com/We5ter/GoogleSSLdomainFinder/archive/master.zip)，解压并进入解压后的目录

- 运行`python GSDFT.py`，即Terminal version，运行中请保证xx-net持续运行；

- 输出结果以表格形式展示在终端，同时写入txt文件

### 演示视频

![demo](https://github.com/We5ter/GSDF/blob/master/demo.gif)


<hr>

&copy;Sixtant Security Lab 2016-2017
