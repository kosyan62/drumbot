class Note:
    _dur = 0
    _name = 'r'
    
    def __init__(self, n, s):
        self._dur = n
        self._name = s

    def __str__(self):
        return "%s%s" % (self._name,self._dur)

    def set_value(self, ch):
        self._name = ch

    def add_duration(self, d):
        self._dur = d

    def get_full(self):
        if self._name != ' ':
            return ("%s%s" % (self._name, self._dur))
        else:
            return ' '

    def get_name(self):
        return self._name

    def get_duration(self):
            return (self._dur)

