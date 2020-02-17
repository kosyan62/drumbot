import note
import random

class Notation:

    def __init__(self):
        self._list = []
        self._len = 0

    def __str__(self):
        str = "Notes list: "
        for s in self._list:
            print(s.get_full())
            str += s.get_full() + ' '
        return str

    def __len__(self):
        return self._len

    def append(self, n):
        self._list.append(n)
        self._len += 1;

    def insert(self, note, place):
        self._list.insert(note, place)
        self._len += 1

    def _make_dots(self):
        for i in range(self._len - 1):
            cur = self._list[i]
            nxt = self._list[i + 1]
            if nxt.get_name() == 'r' and cur.get_duration() * 2 == nxt.get_duration():
                cur.add_dot()
                self._list.remove(nxt)
                self._len -= 1
                self._make_dots()
                break
        
    
    def _make_clear(self):    
        for i in range(self._len - 1):
            cur = self._list[i]
            nxt = self._list[i + 1]
            if nxt.get_name() == 'r' and cur.get_duration() == nxt.get_duration():
                cur.less_duration()
                self._list.remove(nxt)
                self._len -= 1
                self._make_clear()
                break
        self._make_dots()
                
    def get_string(self):
        self._make_clear()
        str = ' '
        for element in self._list:
            str = str + element.get_full()
            str += ' '
        return str

    def shuffle(self):
        random.shuffle(self._list)

    def add_accent(self, i):
        print(i)
        self._list[i - 1].add_accent()
