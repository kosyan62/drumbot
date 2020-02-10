class Paradidl:
    _roll = "RLRL"
    _didl = ["RLRR", "RRLR", "RLLR", "RLRL"]
    _pair = "RRLL"
    _tripl = ["RRRL", "RLLL", "LLLR", "LRRR"]
    _quad = "RRRR"

    def get_val(self, str, opt = 0):
        if str == "roll":
            return self._roll * 2
        if str == "didl":
            return self.get_full_rev(self._didl[opt % 4])
        if str == "pair":
            return (self._pair * 2)
        if str == "tripl":
            return (self._tripl[opt % 4] * 2)
        if str == "quad":
            return _quad * 2

    def get_full_rev(self, str):
        fin = ''
        for i in str:
            if i == 'R':
                fin += 'L'
            else:
                fin += 'R'
        return str + fin
