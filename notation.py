import note

class Notation:
    _list = []

    def append_note(self, n):
        self._list.append(n)
    def insert_note(self, a, b):
        _list.insert(a, b)
    
    def _make_clear(self):    
        for i in range(0, 8, 2):
            if self._list[i + 1].get_name() == 'r' and self._list[i].get_duration() == 8:
                self._list[i+1].set_value(' ')
                self._list[i].add_duration(4)
        
    def get_string(self):
        self._make_clear()
        str = ' '
        for element in self._list:
            str = str + element.get_full()
            str += ' '
        return str
    def get_len(self):
        return len(self._list)

    def __del__(self):
        self._list.clear()
