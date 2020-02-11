class Note:
    
    def __init__(self, n, s):
        self._dur = n
        self._name = s
        self._dot = False

    def __str__(self):
        tmp = "%s%s" % (self._name,self._dur)
        ret = ''
        if self._dot == True:
            ret = tmp + '.'
        return ret

    def set_value(self, ch):
        self._name = ch

    def add_duration(self, d):
        self._dur = d

    def get_full(self):
        tmp = "%s%s" % (self._name,self._dur)
        ret = ''
        if self._dot == True:
            tmp = tmp + '.'
        return tmp

    def get_name(self):
        return self._name

    def get_duration(self):
            return (self._dur)

    def less_duration(self):
        self._dur = self._dur // 2

    def add_dot(self):
        self._dot = True
