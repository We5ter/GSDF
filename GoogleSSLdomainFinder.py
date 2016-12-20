# -*- coding: utf-8 -*-
__author__ = 'Wester'

import requests
import re
import json
import os,cmd,sys

#文本高亮
class Color:
    def __init__(self, msg):
        self.msg = ''
        self.msg = msg
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = "\033[1m"

    def infog(self):

        print self.OKGREEN + self.msg + self.ENDC

    def info(self):
        print self.OKBLUE + self.msg + self.ENDC

    def warn(self):
        print self.WARNING + self.msg + self.ENDC

    def err(self):
        print self.FAIL + self.msg + self.ENDC


#查找域名
class Domain:
    def __init__(self,domain):
        self.domain = domain
        self.Token = 'CAA='
        self.ds = []
        self.count = 0
        self.baseUrl = 'https://www.google.com/transparencyreport/jsonp/ct/search?incl_exp=true&incl_sub=true&c=jsonp'
        self.proxies = {
            'http': 'http://127.0.0.1:8087',
            'https': 'http://127.0.0.1:8087',
        }
        requests.packages.urllib3.disable_warnings()

    def get_domain(self):
        while 1:
            r = requests.get(self.baseUrl+'&domain='+self.domain+'&token='+self.Token, proxies=self.proxies,verify=False)
            # print r.text
            pattern = re.compile(r"jsonp\((.*)\)", re.I|re.X)
            match = pattern.findall(r.text)
            obj = json.loads(match[0])
            self.ds.append(obj['results'])
            self.count = obj['numResults']
            if hasattr(a, 'nextPageToken'):
                self.Token = obj['nextPageToken']
            else:
                break

    def run(self):
        try:
            self.get_domain()
            print self.count
            print self.ds
        except:
            print 'error'


#命令行交互
class Main(cmd.Cmd):
    u'''
 GoogleSSLdomainFinder docs

 Site:https://lightrains.org
 help - 打开本帮助
 find + domain - 列举子域名
 cls - 清空屏幕

        '''
    def __init__(self):
        cmd.Cmd.__init__(self)
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.prompt = "domainFinder by Wester>>"
        self.intro = "Welcome to GoogleSSLdomainFinder wrote by Wester(site:https://lightrains.org)!\nPlease print 'help' to start,Enjoy!"
    def do_EOF(self, line):
        return True

    def do_help(self, line):
        print self.__doc__

    def do_find(self, line):
        domain = line
        d = Domain(domain)
        d.run()

    def do_cls(self, line):
        os.system("clear")



if '__main__' == __name__:
    try:
        os.system("clear")
        m = Main()
        m.cmdloop()
    except KeyboardInterrupt:
        print "Ctrl-c pressed ..."
        sys.exit(1)
    except:
        print '运行出错，请重试'
        reload(sys)
        n = Main()
        n.cmdloop()