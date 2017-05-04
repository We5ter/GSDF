# GoogleSSLdomainFinder Api Version
# -*- coding: utf-8 -*-
__author__ = 'Wester'

import requests
import re
import json
import sys

#查找域名
class GoogleSSLdomainFinder:
    def __init__(self,domain):
        self.domain = domain
        self.Token ='CAA='
        self.ds = []
        self.baseUrl = 'https://www.google.com/transparencyreport/jsonp/ct/search?incl_exp=true&incl_sub=true&c=jsonp'
        self.proxies = {
            'http': 'http://127.0.0.1:8087',
            'https': 'http://127.0.0.1:8087',
        }
        requests.packages.urllib3.disable_warnings()

    def get_domain(self):
        r = requests.get(self.baseUrl+'&domain='+self.domain+'&token='+self.Token, proxies=self.proxies,verify=False)
        # print r.text
        pattern = re.compile(r"jsonp\((.*)\)", re.I|re.X)
        match = pattern.findall(r.text)
        obj = json.loads(match[0])
        self.ds.append(obj['results'])
        if 'nextPageToken' in obj.keys():
            self.Token = obj['nextPageToken']
            self.get_domain()

    def list(self):
        try:
            self.get_domain()
            x = 0
            domains = []
            while (x<len(self.ds)):
                for y in self.ds[x]:
                    domains.append(y['subject'])
                x +=1
            # 去重处理
            domains = list(set(domains))
        except:
            domains = []
        return domains



