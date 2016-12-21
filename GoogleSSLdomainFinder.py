# -*- coding: utf-8 -*-
__author__ = 'Wester'

import requests
import re
import json
import os,cmd,sys

#文本高亮
class Colored(object):
    # 显示格式: \033[显示方式;前景色;背景色m
    # 只写一个字段表示前景色,背景色默认
    RED = '\033[31m'       # 红色
    GREEN = '\033[32m'     # 绿色
    YELLOW = '\033[33m'    # 黄色
    BLUE = '\033[34m'      # 蓝色
    FUCHSIA = '\033[35m'   # 紫红色
    CYAN = '\033[36m'      # 青蓝色
    WHITE = '\033[37m'     # 白色

    #: no color
    RESET = '\033[0m'      # 终端默认颜色

    def color_str(self, color, s):
        return '{}{}{}'.format(
            getattr(self, color),
            s,
            self.RESET
        )

    def red(self, s):
        return self.color_str('RED', s)

    def green(self, s):
        return self.color_str('GREEN', s)

    def yellow(self, s):
        return self.color_str('YELLOW', s)

    def blue(self, s):
        return self.color_str('BLUE', s)

    def fuchsia(self, s):
        return self.color_str('FUCHSIA', s)

    def cyan(self, s):
        return self.color_str('CYAN', s)

    def white(self, s):
        return self.color_str('WHITE', s)

#查找域名
class Domain:
    def __init__(self,domain,Token):
        self.domain = domain
        self.Token = Token
        self.ds = []
        self.count = 0
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
        if self.count == 0:
            self.count = obj['numResults']
        if 'nextPageToken' in obj.keys():
            self.Token = obj['nextPageToken']
            self.get_domain()


    def run(self):
        try:
            c = Colored()
            print c.red('执行查询中，请稍候...')
            self.get_domain()
            print c.green('\n\n共有'+str(self.count)+'条子域名记录:\n\n')
            print '-'*70
            x = 0
            domains = []
            while (x<len(self.ds)):
                for y in self.ds[x]:
                    domains.append(y['subject'])
                x +=1
            # 去重处理
            domains = list(set(domains))
            # 按表格形式输出
            z = 0
            width = 20
            while z <(len(domains)/3+1):
                print "{} | {} | {}".format(domains[z].ljust(width),domains[z+1].ljust(width),domains[z+2].ljust(width))
                print '-'*70
                z +=3
            print '\n\n'

        except:
            print '程序部分执行出现异常'


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
        self.prompt = "domainFinder[at]Wester>>"
        self.intro = "Welcome to GoogleSSLdomainFinder wrote by Wester(site:https://lightrains.org)!\nPlease print 'help' to start,Enjoy!"
    def do_EOF(self, line):
        return True

    def do_help(self, line):
        print self.__doc__

    def do_find(self, line):
        domain = line
        d = Domain(domain,'CAA=')
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
        print '程序执行出错，请重试...'
        reload(sys)
        n = Main()
        n.cmdloop()