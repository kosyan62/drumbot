import random

class Rudiments:
    _roll = "RLRL"
    _didl = ["RLRR", "RRLR", "RLLR", "RLRL", "LRLR", "LLRL", "LRRL", "LRLL"]
    _pair = "RRLLRRLL"
    _tripl = ["RRRLRRRL", "RLLLRLLL", "LLLRLLLR", "LRRRLRRR"]
    _quad = "RRRRLLLL"

    def get_random_rudim(self):
        res = [self._roll, self._pair] + self._didl +\
                [''.join(reversed(self._roll)), \
                ''.join(reversed(self._pair))]
        random.shuffle(res)
        return res
