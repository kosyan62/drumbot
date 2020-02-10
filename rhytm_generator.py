import random
from  randweight import weight
from note import Note
from notation import Notation

def get_drumbit_str():
    x = weight()
    lis1 = []
    for i in range(x):
        lis1.append('bassdrum')
    while len(lis1) < 7:
        lis1.append('r')
    random.shuffle(lis1)
    lis1.insert(4, 'snare')
    i = 0
    rhytm = Notation()
    for element in lis1:
        one = Note(8, element)
        rhytm.append_note(one)
    ret = rhytm.get_string()
    del rhytm
    #ret = ret.replace('snare', '\\skip ')
    return ret

def get_hh_str():
    if random.choice([True, False, True]):
        str ="hh4 hh <hh> hh "
    else:
        str = "hh8 hh hh hh <hh> hh hh hh "
    return str
