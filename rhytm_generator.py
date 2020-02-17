import random
from  randweight import weight
from note import Note
import notation

def get_drumbit_str():
    x = weight()
    rhytm = []
    for i in range(x):
        nt = Note(16, 'bassdrum')
        rhytm.append(nt)
    while len(rhytm) < 7:
        nt = Note(16, 'r')
        rhytm.append(nt)
    random.shuffle(rhytm)
    nt = Note(16, 'snare')
    rhytm.insert(4, nt)
    ret = notation.get_string(rhytm)
    return ret

def get_hh_str():
    if random.choice([True, False, True]):
        str ="hh8 hh <hh> hh "
    else:
        str = "hh16 hh hh hh <hh> hh hh hh "
    return str
