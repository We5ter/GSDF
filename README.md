# GoogleSSLdomainFinder

![GitHub issues](https://img.shields.io/github/issues/We5ter/GSDF.svg)
![GitHub forks](https://img.shields.io/github/forks/We5ter/GSDF.svg)
![GitHub stars](https://img.shields.io/github/stars/We5ter/GSDF.svg)
![GitHub contributors](https://img.shields.io/github/contributors/We5ter/GSDF.svg)
[![Python 2.x](https://img.shields.io/badge/python-2.x-yellow.svg)](https://www.python.org/) 

**README.md in [Chinese 中文](https://github.com/We5ter/GSDF/blob/master/README_CN.md)**

***

### Project Description

**GoogleSSLdomainFinder** is a domain scanner based on https://transparencyreport.google.com/https/certificates.
### Change records

- 2016.12.21 Increase the file record function
- 2016.12.22 Add the api library
- 2017.01.05 complete api library, usage:
```
from GSDFA import GoogleSSLdomainFinder
domain = GoogleSSLdomainFinder ('chaitin.cn')
domain.list () # output as a dict
```

- 2017.09.16 update to v1.1
- 2018.1.7 update to v2.0(The original api was closed,so I rewrite this script again)

### Using Instructions

- First make sure the computer is already installed on python 2.7 or later;
- If you use the Shadowsocks to access Google, please cancel the following lines comments and add `proxies=self.proxies` to requests
```
self.proxies = {
            'http': 'http://127.0.0.1:1087',
            'https': 'http://127.0.0.1:1087',
            }
```

- Run  `python GSDFT.py -h`, this is Terminal version;

- The output is displayed in tabular form on the terminal, the results is also written in txt file.

<hr>

### Demo video

![demo](https://github.com/We5ter/GSDF/blob/master/demo.gif)

&copy;Sixtant Security Lab 2016-2017
