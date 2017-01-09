# GoogleSSLdomainFinder Terminal Version
# -*- coding: utf-8 -*-
__author__ = 'Wester'

import requests
import re
import json
import os,cmd,sys

#text highlight
class Colored(object):
    RED = '\033[31m'       
    GREEN = '\033[32m'     
    YELLOW = '\033[33m'    
    BLUE = '\033[34m'      
    FUCHSIA = '\033[35m'   
    CYAN = '\033[36m'      
    WHITE = '\033[37m'     

    #: no color
    RESET = '\033[0m'      

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

#domainfinde function
class Domain:
    def __init__(self,domain,Token):
        self.domain = domain
        self.Token = Token
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
            print c.green('\nProcessing...,The result may be numerous.so please wait for a while.')
            self.get_domain()
            x = 0
            domains = []
            while (x<len(self.ds)):
                for y in self.ds[x]:
                    domains.append(y['subject'])
                x +=1
            # Remove duplicates
            domains = list(set(domains))

            # Output the results in a table
            z = 0
            width = 20
            if len(domains)>2:
                print c.green('\n\nAha,I have found '+str(len(domains))+' subdomains:\n\n')
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
                    print c.green('\n\nAha,I have found '+str(len(domains))+' subdomains:\n\n')
                    print '-'*(width+5)
                    while z <(len(domains)):
                        print "{0}".format(c.fuchsia("{}")).format(domains[z].ljust(width))
                        print '-'*(width+5)
                        z +=1
                    print '\n\n'
                else:
                    print c.red('unfortunately,I can not find subdomains for your conditions...')

            # write into txt file
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
            print "Ctrl-c Pressed，exit..."
            sys.exit(1)
        except:
            print c.red('Sorry,timeout or network is not smooth')

#terminal
class Main(cmd.Cmd):
    '''
 GoogleSSLdomainFinder  docs

 author:Wester
 blog:https://lightrains.org

 help - open this help

 find + domain - list subdomains,example command:find mi.com;domain format:www.mi.com or mi.com;don't need to add http/https
 
 cls - clear screen

 exit - exit program

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
            print co.red('please input domain')
        elif not re.search(r"^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$", domain):
            print co.red(''+domain+'is illegal')
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
        print "Ctrl-c pressed,exit..."
        sys.exit(1)
    except:
        exit()
