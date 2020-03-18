import os
import sys
import time
import random
import threading
import ServerInfo
import ServerConfig
import ServerPinger
import ServerHandler
os.system('clear')
ru = lambda text: text.decode('utf-8', 'ignore')
R = '\033[31;1m'
Y = '\033[33;1m'
G = '\033[32;1m'
B = '\033[94m'
C = '\x1b[36m'
P = '\033[35;1m'
W = '\033[0m'
class Server:
    def __init__(self):
        self.long = 18
        self.sets = ServerConfig.Sets()
        self.noyes = [ru('No'), ru('Yes')]
        self.version = [ru('Default'), ru('HTTP/1.0'), ru('HTTP/1.1')]
        self.method = [ru('HEAD'),
         ru('GET'),
         ru('POST'),
         ru('DELETE'),
         ru('CONNECT'),
         ru('OPTIONS'),
         ru('TRACE'),
         ru('PUT')]
        self.line = [ru('\\r\\n'), ru('\\n')]
        self.split = [ru('Default'),
         ru('%s' % (self.line[self.sets.ILINE] * self.sets.ILINE)),
         ru('%s' % (self.line[self.sets.ILINE] * self.sets.ILINE)),
         ru('%s' % (self.line[self.sets.ILINE] * self.sets.ILINE)),
         ru('%s' % (self.line[self.sets.ILINE] * self.sets.ILINE)),
         ru('%s' % (self.line[self.sets.ILINE] * self.sets.ILINE))]
    def subs(self, data = '', cut = False):
        if data:
            data = data
        else:
            data = 'None'
        if cut:
            if len(data) > 5:
                data = '%s...' % data[:5]
        return data
    def about(self, title = ''):
        self.info = []
        self.info.append('%s %s\n' % (title, '' * (self.long - len(title) - 5)))
        return ru(''.join(self.info))
    def log(self, title = ''):
        self.info = []
        self.info.append('=[ %s ]=\n' % (title))
        self.info.append('\n\n')
        return ru(''.join(self.info))
    def log(self, title = ''):
        self.info = []
        self.info.append('    [ %s %s]\n' % (title, '' * (self.long - len(title) - 5)))
        self.info.append('\n')
        return ru(''.join(self.info))
    def show(self):
        sys.stderr.write(self.about(R+'##################################'))
        sys.stderr.write(self.about(P+'#========= MUHAMMAD AMIN =======#'))
        sys.stderr.write(self.about(B+'#================================#'))
        sys.stderr.write(self.about(G+'#= HOST:PORT > [127.0.0.1:8080] =#'))
        sys.stderr.write(self.about(B+'#======= [START INJECT!!] =======#'))
        sys.stderr.write(self.about(P+'#= Hubungkan Aplikasi VPN Anda! =#'))
        sys.stderr.write(self.about(R+'##################################'))
        time.sleep(2)
    def run(self):
        ServerHandler.LogWindow(True)
        ServerHandler.HTTPProxyService().serve_forever()
    def log(self, text):
        sys.stderr.write(text)
    def pinger(self):
        while 1:
            time.sleep(random.randint(30, 300))
            ServerPinger.Pinger().check()
if __name__ == '__main__':
    Server().show()
    services = [threading.Thread(target=Server().run, args=()), threading.Thread(target=Server().pinger, args=())]
    for serving in services:
        serving.start()