import requests
from modules import proxychecker

class AnonBrowser(object):

    def __init__(self):
        self.proxies = proxychecker.proxyList
        self.session = requests.session()

        self.RED = "\033[1;31m"
        self.CYAN = "\033[1;36m"
        self.GREEN = "\033[0;32m"
        self.MAGENTA = '\033[95m'
        self.OKBLUE = '\033[94m'

    def banner(self):
        print(self.CYAN+" _____ _    _    ___       ")
        print(self.CYAN+"|_   _| |  | |  /   |      ")
        print(self.CYAN+"  | | | |  | | / /| |_  __ ")
        print(self.CYAN+"  | | | |/\| |/ /_| \ \/ / ")
        print(self.CYAN+" _| |_\  /\  /\___  |>  <  ")
        print(self.CYAN+" \___/ \/  \/     |_/_/\_\ ")
        print("")
        print(self.MAGENTA + "# Author      :" + "KIZILYILDIZ✮")
        print(self.MAGENTA + "# Instagram   :" + "www.instagram.com/kiziilyildiz")
        print(self.MAGENTA + "# GitHub      :" + "www.github.com/Zeynel-Cubuk")
        print(self.MAGENTA + "# Title       :" + "iw4x.py")
        print(self.MAGENTA + "# Date        :" + "18/1/2021")
        print(self.MAGENTA + "# Version     :" + "None")
        print(self.MAGENTA+"#" * 47)

    def browser(self):
        print("\n"+self.OKBLUE+"[*] IP:" + requests.get("http://icanhazip.com/").text)

        checkList = []
        for prox in self.proxies:

            if prox not in checkList:
                ip, port = prox
                self.session.proxies = {}

                try:
                    self.session.proxies['http'] = 'http://' + str(ip) + ":" + str(port)
                    self.session.proxies['https'] = 'https://' + str(ip) + ":" + str(port)
                    self.session.get("http://icanhazip.com/")
                    print(self.GREEN+"[+] " + str(ip) + ":" + str(port))

                except:
                    print(self.RED+"[-] " + str(ip) + ":" + str(port))

                checkList.append(prox)

            else:
                continue

if __name__ == "__main__":
    ab = AnonBrowser()
    ab.banner()
    ab.browser()