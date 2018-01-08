## GoogleSSLdomainFinder

![GitHub issues](https://img.shields.io/github/issues/We5ter/GSDF.svg)
![GitHub forks](https://img.shields.io/github/forks/We5ter/GSDF.svg)
![GitHub stars](https://img.shields.io/github/stars/We5ter/GSDF.svg)

**README.md in [English 英文](https://github.com/We5ter/GSDF/blob/master/README.md)**

#### 简要介绍

**GoogleSSLdomainFinder**是为方便使用<a href="https://transparencyreport.google.com/https/certificates" target="_blank">谷歌透明证书查询</a>的python脚本，而使用谷歌透明证书查询子域名准确率较高，但覆盖面不足。

<hr>

#### 更迭记录

- 2016.12.21 增加文件记录功能
- 2016.12.22 增加api库
- 2017.01.05 完成api库，使用方法：
  <pre><code>from GSDFA import GoogleSSLdomainFinder
  do = GoogleSSLdomainFinder('mi.com')
  do.list()  #输出为字典
  </code></pre>
  
- 2017.09.16 更新至v1.1版本
- 2018.01.07 更新至v2.0版本 （新功能：标记证书已经过期的域名）

<hr>

#### 使用方法

- 首先确保电脑已经安装上python 2.7或者更高版本
- 如果你使用Shadowsocks访问Google，可取消以下几行的注释为并在requests中添加`proxies=self.proxies`：

```
 self.proxies = {
            'http': 'http://127.0.0.1:1087',
            'https': 'http://127.0.0.1:1087',
            }
```

- 下载[本脚本](https://github.com/We5ter/GSDF/archive/master.zip)，解压并进入解压后的目录

- 运行`python GSDFT.py -h`，即Terminal version；

- 输出结果以表格形式展示在终端，同时写入txt文件

### 演示视频

![demo](https://github.com/We5ter/GSDF/blob/master/demo.gif)


<hr>

&copy;Sixtant Security Lab 2016-2017
