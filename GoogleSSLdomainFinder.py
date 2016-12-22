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
        sys.setdefaultencoding('utf-8')
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


    def run(self):
        try:
            c = Colored()
            print c.green('\n查询中，结果集可能较大，导致耗时较长，请耐心等待...')
            self.get_domain()
            x = 0
            domains = []
            while (x<len(self.ds)):
                for y in self.ds[x]:
                    domains.append(y['subject'])
                x +=1
            # 去重处理
            domains = list(set(domains))

            # 按表格形式输出结果
            z = 0
            width = 20
            if len(domains)>2:
                print c.green('\n\n共有'+str(len(domains))+'条子域名记录:\n\n')
                print '-'*(width*3+10)
                while z <(len(domains)):
                    if (len(domains) - z) == 1:
                        print "{} |".format(c.fuchsia("{}")).format(domains[z].ljust(width))
                    elif (len(domains) - z) == 2:
                        print "{} | {} |".format(c.fuchsia("{}"), c.cyan("{}")).format(domains[z].ljust(width),
                                                                         domains[z + 1].ljust(width))
                    else:
                        print "{} | {} | {}".format(c.fuchsia("{}"), c.cyan("{}"),
                                                   c.yellow("{}")).format(domains[z].ljust(width),
                                                                         domains[z + 1].ljust(width),
                                                                         domains[z + 2].ljust(width))


                    print '-'*(width*3+10)
                    z +=3
                print '\n\n'
            else:
                if not (len(domains) ==0):
                    print c.green('\n\n共有'+str(len(domains))+'条子域名记录:\n\n')
                    print '-'*(width+5)
                    while z <(len(domains)):
                        print "{0}".format(c.fuchsia("{}")).format(domains[z].ljust(width))
                        print '-'*(width+5)
                        z +=1
                    print '\n\n'
                else:
                    print c.red('未查询到子域名记录，请稍后重试...')

            # 根据操作系统不同将查询记录写入文件
            if os.path.exists('log') == False:
                os.mkdir('log')
            if(os.name == 'posix'):
                with open(os.getcwd()+"/log/"+self.domain+'.txt', 'wb') as f:
                    for i in domains:
                        f.write(i+'\r\n')
                        f.flush()
                f.close()
            else:
                with open(os.getcwd()+"\\log\\"+self.domain+'.txt', 'wb') as f:
                    for i in domains:
                        f.write(i+'\r\n')
                        f.flush()
                f.close()

        except KeyboardInterrupt:
            print "检测到Ctrl-c按键，正在退出"
            sys.exit(1)
        except:
            print c.red('您所查询域名结果较多，耗时过长，可能已经断开连接')

#命令行交互
class Main(cmd.Cmd):
    u'''╭╮　　　　　　　╭╮　　
　││　　　　　　　││　　
╭┴┴———————┴┴╮
│　　　　　　　　　　　│　　　
│　　　　　　　　　　　│　　　
│　●　　　　　　　●　│
│○　　╰┬┬┬╯　　○│
│　　　　╰—╯　　　　│　
╰——┬Ｏ———Ｏ┬——╯
　 　╭╮　　　　╭╮　　　　
　 　╰┴————┴╯
 GoogleSSLdomainFinder  帮助文档

 author:Wester
 blog:https://lightrains.org

 help - 打开本帮助
 find + domain - 列举子域名 example:find mi.com 域名可使用www.mi.com或者mi.com,无需添加http或者https
 cls - 清空屏幕
 exit - 退出程序
        '''
    def __init__(self):
        cmd.Cmd.__init__(self)
        co = Colored()
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.prompt = co.green("domainFinder[at]Wester =>")
        self.intro = "\nWelcome to "+co.fuchsia("GoogleSSLdomainFinder")+" wrote by Wester("+co.yellow("blog:https://lightrains.org")+")!\n\nPlease print "+co.red('help')+" to start,Enjoy!\n\n"
    def do_EOF(self, line):
        return True

    def do_help(self, line):
        print self.__doc__

    def do_find(self, line):
        co = Colored()
        domain = line
        if domain =='':
            print co.red('请输入域名')
        elif not re.search(r"^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$", domain):
            print co.red('你输入的'+domain+'不符合规范')
        else:
            d = Domain(domain,'CAA=')
            d.run()

    def do_cls(self, line):
        os.system("clear")

    def do_exit(self,line):
        sys.exit(-1)



if '__main__' == __name__:
    try:
        os.system("clear")
        m = Main()
        m.cmdloop()
    except KeyboardInterrupt:
        print "检测到Ctrl-c按键,正在退出"
        sys.exit(1)
    except:
        exit()
