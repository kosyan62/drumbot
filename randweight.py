import random

def weight():
    weight = random.randint(1, 125)
    if 0 < weight <= 7:
        return 1
    elif 7 < weight <= 28:
        return 2
    elif 28 < weight <= 63:
        return 3
    elif 63 < weight <= 98:
        return 4
    elif 98 < weight <= 119:
        return 5
    elif 119 < weight <= 126:
        return 6
    else: 
        return 7
