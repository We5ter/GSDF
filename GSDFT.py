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
        self.domains = []
        self.flag = 0 
        self.length = 0
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"}
        self.baseUrl = 'https://www.google.com/transparencyreport/jsonp/ct/search?incl_exp=true&incl_sub=true&c=jsonp'
        self.proxies = {
            'http': 'http://127.0.0.1:1087',
            'https': 'http://127.0.0.1:1087',
        }
        requests.packages.urllib3.disable_warnings()

    def get_domain(self):
        r = requests.get(self.baseUrl+'&domain='+self.domain+'&token='+self.Token,headers=self.headers,proxies=self.proxies,verify=False)
        # print r.text
        pattern = re.compile(r"jsonp\((.*)\)", re.I|re.X)
        match = pattern.findall(r.text)
        obj = json.loads(match[0])
        try:
            if self.flag < 20:
                self.process(obj['results'])
                self.flag += 1
            else:
                if self.flag == 20:
                    print "\nOh no,too much subdomains,please give me more patience!"
                    self.flag +=1
                else:
                    pass
        except:
            print "something went wrong"
        self.ds.append(obj['results'])
        if 'nextPageToken' in obj.keys():
            self.Token = obj['nextPageToken']
            self.get_domain()
        else:
            c = Colored()
            print c.green("\nAll done,here are subdomains for "+ self.domain + "\n")

    def run(self):
        try:
            c = Colored()
            print c.yellow('Processing...,The result may be numerous.so please wait for a while.')
            self.get_domain()  
            x = 0
            while (x<len(self.ds)):
                for y in self.ds[x]:
                    self.domains.append(y['subject'])
                x +=1
            # Remove duplicates
            self.domains = list(set(self.domains))   
            #print self.domains
            for y in self.domains:
                print y
            print c.cyan("\nHere are "+str(len(self.domains))+" subdomains for "+self.domain +"\n")
            self.log()
            print c.cyan("subdomains has been saved in directory ./"+self.domain+".txt\n")
        except KeyboardInterrupt:
            print "Ctrl-c Pressed，exit..."
            sys.exit(1)
        except:
            print c.red('Sorry,timeout or network is not smooth')
            
    def process(self,data):
        self.length = self.length + len(data)
        #print self.length
        print  "["+(self.length//4) * "-" +">" + (50 - self.length//4) * " " + "] " + str(self.length)+"/all done"

    def log(self):
        # write into txt file
        if os.path.exists('log') == False:
            os.mkdir('log')
        if(os.name == 'posix'):
            with open(os.getcwd()+"/log/"+self.domain+'.txt', 'wb') as f:
                for i in self.domains:
                    f.write(i+'\r\n')
                    f.flush()
            f.close()
        else:
            with open(os.getcwd()+"\\log\\"+self.domain+'.txt', 'wb') as f:
                for i in self.domains:
                    f.write(i+'\r\n')
                    f.flush()
            f.close()

#terminal
class Main(cmd.Cmd):
    '''
    `______`````______`````_____`````______``
    /\``___\```/\``___\```/\``__-.``/\``___\`
    \`\`\__`\``\`\___``\``\`\`\/\`\`\`\``__\`
    `\`\_____\``\/\_____\``\`\____-``\`\_\```
    ``\/_____/```\/_____/```\/____/```\/_/```
    `````````````````````````````````````````

    Author:Wester@Sixtant Security Lab

    How to use:

    [find + domain] - list subdomains

    (example command:find mi.com and you don't need to add http/https)

    [cls] - clear screen

    [help] - open this help

    [exit] - exit program
    '''
    def __init__(self):
        cmd.Cmd.__init__(self)
        co = Colored()
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.prompt = co.green("domainfinder =>")
        self.intro = "Welcome to "+co.fuchsia("GoogleSSLdomainFinder")+"!Please print "+co.red('help')+" to get help,Enjoy!\n"
    
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
            print co.red(''+domain+' is illegal')
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
