# GoogleSSLdomainFinder

![GitHub issues](https://img.shields.io/github/issues/We5ter/GSDF.svg)
![GitHub forks](https://img.shields.io/github/forks/We5ter/GSDF.svg)
![GitHub stars](https://img.shields.io/github/stars/We5ter/GSDF.svg)
![GitHub contributors](https://img.shields.io/github/contributors/We5ter/GSDF.svg)
[![Python 2.7](https://img.shields.io/badge/python-2.x-yellow.svg)](https://www.python.org/) 

**README.md in [Chinese 中文](https://github.com/We5ter/GSDF/blob/master/README_CN.md)**

***

### Project Description

**GoogleSSLdomainFinder** is a domain searcher based on https://transparencyreport.google.com/https/certificates.
### Change records

- 2016.12.21 Increase the file record function
- 2016.12.22 Add the api library
- 2017.01.05 complete api library, usage:
```
from GSDFA import GoogleSSLdomainFinder
domain = GoogleSSLdomainFinder('chaitin.cn','show')
print domain.list() # output as a dict
```

- 2017.09.16 update to v1.1
- **2018.01.07 update to v2.0 (New feature:Identifies the subdomain which has expired)**

### Using Instructions

- First make sure the computer is already installed on **Python 2.x(Advice is 2.7)**;
- If you use the Shadowsocks to access Google, please cancel the following lines comments and add `proxies=self.proxies` to requests
```
self.proxies = {
            'http': 'http://127.0.0.1:1087',
            'https': 'http://127.0.0.1:1087',
            }
```
- Download this script, extract and enter the extracted directory;

- Run  `python GSDFT.py -h`, this is Terminal version;

- The output is displayed in tabular form on the terminal, the results is also written in txt file.

<hr>

### Demo video

![demo](https://github.com/We5ter/GSDF/blob/master/demo.gif)

&copy;Sixtant Security Lab 2016-2017
