# GoogleSSLdomainFinder Api Version
# -*- coding: utf-8 -*-
__author__ = 'Wester'

import requests
import re
import json
import os,cmd,sys
import argparse
import time,datetime
from tqdm import tqdm

sess = requests.Session()

#domainfinde function
class GoogleSSLdomainFinder:
    def __init__(self,search_domain,show_expired):
        self.search_domain = search_domain
        self.show_expired = show_expired
        self.domains = {}
        self.page_token = ''
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"}
        self.indexUrl = 'https://transparencyreport.google.com/transparencyreport/api/v3/httpsreport/ct/certsearch?include_subdomains=true'
        self.nextUrl = 'https://transparencyreport.google.com/transparencyreport/api/v3/httpsreport/ct/certsearch/page?p='
        #self.proxies = {
        #    'http': 'http://127.0.0.1:1087',
        #    'https': 'http://127.0.0.1:1087',
        #}
        requests.packages.urllib3.disable_warnings()

    def get_domain(self):
        if self.page_token != '':
            req = sess.get(self.nextUrl+self.page_token,headers=self.headers,verify=False)
        else:
            if self.show_expired == 'show':
                req = sess.get(self.indexUrl+'&domain='+self.search_domain+'&include_expired=true',headers=self.headers,verify=False)
            else:
                req = sess.get(self.indexUrl+'&domain='+self.search_domain,headers=self.headers,verify=False)
        rep = (req.text).encode('utf-8').lstrip(")]}'")
        rep = re.sub(r'\[\[\"https\.ct\.cdsr\"\,','[',rep)
        rep = rep.replace('\n','').replace('\\','')
        rep = rep[:-1]
        rep = json.loads(rep)              
        for y in rep[0]:
            if not self.domains.has_key(y[1]):
                self.domains[y[1]] = {}
                self.domains[y[1]]['expired_time'] = int((str(y[4]))[:-3])
                self.domains[y[1]]['is_expired'] = 0
            else:
                if self.domains[y[1]]['expired_time'] < int((str(y[4]))[:-3]):
                    self.domains[y[1]]['expired_time'] = int((str(y[4]))[:-3])
                    now = time.time()
                    if now >int((str(y[4]))[:-3]):
                        self.domains[y[1]]['is_expired'] = 1
                    else:
                        self.domains[y[1]]['is_expired'] = 0
                else:
                    continue
        if rep[2][1] != None:
            self.page_token = rep[2][1]
            self.get_domain()

    def list(self):
        try:
           self.get_domain()
           return self.domains
        except:
            self.domains = {}
            return self.domains
