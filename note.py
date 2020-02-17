class Note:
    
    def __init__(self, n, s):
        self._dur = n
        self._name = s
        self._dot = False
        self._hand = ''
        self._accent = False

    def __str__(self):
        tmp = "%s%s" % (self._name,self._dur)
        ret = ''
        if self._dot == True:
            tmp += '.'
        if self._accent == True:
            tmp += '->'
        return ret

    def set_value(self, ch):
        self._name = ch

    def add_duration(self, d):
        self._dur = d

    def get_full(self):
        tmp = "%s%s" % (self._name,self._dur)
        if self._dot == True:
            tmp = tmp + '.'
        if self._hand != '':
            tmp = f'{tmp}_"{self._hand}"'
        if self._accent == True:
            tmp += '->'
        return tmp

    def get_name(self):
        return self._name

    def get_duration(self):
            return (self._dur)

    def less_duration(self):
        self._dur = self._dur // 2

    def add_dot(self):
        self._dot = True

    def add_accent(self):
        self._accent = True

    def add_hand(self, h):
        self._hand = h
