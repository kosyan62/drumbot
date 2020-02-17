import note
import random

def make_dots(nots):
    for i in range(len(nots) - 1):
        cur = nots[i]
        nxt = nots[i + 1]
        if nxt.get_name() == 'r' and cur.get_duration() * 2 == nxt.get_duration():
            cur.add_dot()
            nots.remove(nxt)
            make_dots(nots)
            break
    

def make_clear(nots):    
    for i in range(len(nots) - 1):
        cur = nots[i]
        nxt = nots[i + 1]
        if nxt.get_name() == 'r' and cur.get_duration() == nxt.get_duration():
            cur.less_duration()
            nots.remove(nxt)
            make_clear(nots)
            break
    make_dots(nots)
            
def get_string(nots):
    make_clear(nots)
    str = ' '
    for element in nots:
        str = str + element.get_full()
        str += ' '
    return str

def add_accent(mlist, i):
    mlist[i - 1].add_accent()
