#Embedded file name: ServerConfig.py

import os
ru = lambda text: text.decode('utf-8', 'ignore')
ur = lambda text: text.encode('utf-8', 'ignore')
name = 'SimpleServer.ini'
conf = os.path.realpath(os.path.join(os.path.dirname(__file__), '%s' % name))

class Sets:

    def __init__(self):
        self.LHOST = '127.0.0.53'
        self.LPORT = 8989
        self.FQUERY = ''
        self.MQUERY = ''
        self.BQUERY = ''
        self.RQUERY = ''
        self.CQUERY = ''
        self.IQUERY = ''
        self.IMETHOD = 0
        self.ILINE = 0
        self.ISPLIT = 0
        self.RPORT = 0
        self.RPATH = 0
        self.ADMODE = 1
        self.CUSHDR0 = 'X-Online-Host'
        self.VALHDR0 = '52.219.124.148'
        self.CUSHDR1 = 'Connection'
        self.VALHDR1 = 'Keep-Alive'
        self.CUSHDR2 = ''
        self.VALHDR2 = ''
        self.CUSHDR3 = ''
        self.VALHDR3 = ''
        self.KEEP = ''
        self.RHTTP = 0
        self.RHTTPS = 1
        self.SBUFF = 1024
        self.TIMEOUT = 1
        self.PHOST = ''
        self.PPORT = 0
        self.PTYPE = 0
        self.load()

    def load(self):
        try:
            for name, value in [ line.split(' = ') for line in open(conf, 'rb').read().splitlines() ]:
                self.__dict__[name] = eval(value)

        except:
            self.save()
            for name, value in [ line.split(' = ') for line in open(conf, 'rb').read().splitlines() ]:
                self.__dict__[name] = eval(value)

    def save(self):
        data = ''
        for name in self.__dict__.keys():
            line = name + ' = ' + repr(self.__dict__[name]) + '\r\n'
            data += line

        open(conf, 'wb').write(ur(data))
        del data
        #mod sane4tsu
