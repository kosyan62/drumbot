import random
from  randweight import weight

def get_drumbit_str():
    x = weight()
    list = []
    for i in range(x):
        list.append('bassdrum')
    while len(list) < 7:
        list.append('r')
    random.shuffle(list)
    list.insert(4, 'snare')
    i = 0
    for i in range(0, 8, 2):
        if list[i + 1] == 'r':
            list[i] += '4'
        else:
            list[i] += '8'
    i = 0
    for i in list:
        if i == 'r':
            list.remove(i)
    str = ' '
    for element in list:
        str = str + element
        str += ' '
    return str

def get_hh_str():
    if random.choice([True, False, True]):
        str ="hh4 hh hh hh"
    else:
        str = "hh8 hh hh hh hh hh hh hh"
    return str
