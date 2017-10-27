# GoogleSSLdomainFinder

![GitHub issues](https://img.shields.io/github/issues/We5ter/GSDF.svg)
![GitHub forks](https://img.shields.io/github/forks/We5ter/GSDF.svg)
![GitHub stars](https://img.shields.io/github/stars/We5ter/GSDF.svg)
![GitHub contributors](https://img.shields.io/github/contributors/We5ter/GSDF.svg)
[![Python 2.x](https://img.shields.io/badge/python-2.x-yellow.svg)](https://www.python.org/) 

**README.md in [Chinese 中文](https://github.com/We5ter/GSDF/blob/master/README_CN.md)**

***

### Project Description

**GoogleSSLdomainFinder** is a domain scanner based on https://transparencyreport.google.com/https/certificates (use XX-Net to access Google).

### Change records

- 2016.12.21 Increase the file record function
- 2016.12.22 Add the api library
- 2017.01.05 complete api library, usage:
```
from GSDFA import GoogleSSLdomainFinder
do = GoogleSSLdomainFinder ('mi.com')
do.list () # output as a list
```

- 2017.09.16 update to v1.1

### Using Instructions

- First make sure the computer is already installed on python 2.7 or later;

- Make sure that you can visit google, install XX-Net (if installed, you can ignore this step, a brief installation process is as follows)

```
Download https://codeload.github.com/XX-net/XX-Net/zip/3.2.7=> Unzip => Run start.vbs (windows) / start (unix / linux) => Import the browser plug-in and Certificate => Waiting for xx-net scan IP to complete, about 30 minutes
```

**Note**

If you use the Shadowsocks to access Google, please replace proxies port to
```
self.proxies = {
            'http': 'http://127.0.0.1:1087',
            'https': 'http://127.0.0.1:1087',
            }
```


- Run XX-Net, please ensure that xx-net running in 127.0.0.1:8087 (default), you can access 127.0.0.1:8085 view it;

- Download this script, unzip it and go to the unpacked directory;

- Run  `python GSDFT.py`, this is Terminal version, please ensure that running xx-net continuous operation;

- The output is displayed in tabular form on the terminal, the results is also written in txt file.

<hr>

### Demo video

![demo](https://github.com/We5ter/GSDF/blob/master/demo.gif)

&copy;Sixtant Security Lab 2016-2017
