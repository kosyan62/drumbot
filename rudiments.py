class Rudiments:
    _roll = "RLRL"
    _didl = ["RLRR", "RRLR", "RLLR", "RLRL"]
    _pair = "RRLL"
    _tripl = ["RRRL", "RLLL", "LLLR", "LRRR"]
    _quad = "RRRR"

    def get_val_full(self, str, opt = 0):
        if str == "roll":
            return self._roll * 2
        elif str == "didl":
            return self.get_full_rev(self._didl[opt % 4])
        elif str == "pair":
            return (self._pair * 2)
        elif str == "tripl":
            return (self._tripl[opt % 4] * 2)
        elif str == "quad":
            return _quad * 2
    def get_val_half(self, rud, half, opt = 0):
        res = self.get_val_full(rud, opt)
        print(res)
        for i in range (7):
            if i < 4:
                left = res[i]
            else:
                right = res[i]
        print(left + right)
        if half == "left":
            return left
        else:
            return right

    def get_full_rev(self, str):
        fin = ''
        for i in str:
            if i == 'R':
                fin += 'L'
            else:
                fin += 'R'
        return str + fin
