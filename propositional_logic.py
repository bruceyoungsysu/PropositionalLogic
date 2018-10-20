
class symbol:

    def __init__(self):
        self.type = "atom"
        self.value = None
        self.params = []
        self.name = ""

    def assign(self, dic, model):
        if self.name in dic.keys():
            self.value = dic[self.name] & model
        elif self.params:
            for p in self.params:
                p.assign(dic, model)
        self.update()
        return self

    def update(self):
        pass


class pl_not(symbol):

    def __init__(self, sym):
        symbol.__init__(self)
        self.type = "not"
        self.params = [sym]

    def update(self):
        self.value = not self.params[0].value


class pl_and(symbol):

    def __init__(self, sym1,sym2):
        symbol.__init__(self)
        self.type = "and"
        self.params = [sym1, sym2]

    def update(self):
        self.value = self.params[0].value and self.params[1].value


class pl_or(symbol):

    def __init__(self, sym1, sym2):
        symbol.__init__(self)
        self.type = "or"
        self.params = [sym1, sym2]

    def update(self):
        self.value = self.params[0].value or self.params[1].value


class pl_imply(symbol):

    def __init__(self, sym1, sym2):
        symbol.__init__(self)
        self.type = "imply"
        self.params = [sym1, sym2]

    def update(self):
        if self.params[0].value and not self.params[1].value:
            self.value = False
        else:
            self.value = True


class pl_bid(symbol):

    def __init__(self, sym1, sym2):
        symbol.__init__(self)
        self.type = "bid"
        self.params = [sym1, sym2]

    def update(self):
        if bool(self.params[0].value) == bool(self.params[1].value):
            self.value = True
        else:
            self.value = False


def same(s1, s2):
    # assert whether two symbols are the same
    if s1.type != s2.type:
        return False
    if s1.value != s2.value:
        return False
    p1 = sorted(s1.params)
    p1_l = len(p1)
    p2 = sorted(s2.params)
    p2_l = len(p2)
    if p1_l == p2_l == 0:
        return True
    if p1_l != p2_l:
        return False
    for i in range(len(p1_l)):
        if not same(p1[i], p2[i]):
            return False
    return True


def compose(symbols):
    # compose the symbols to a symbol
    pass


def symbols(s1):
    # return all the symbols in a nested symbol
    # symbs should be a list to hold symbols in recursions
    symbs = []
    if s1.params == []:
        return symbs
    for ele in s1.params:
        if (ele.params == []) or (ele.type == "not") :  # should note the symbols with type not could be a atomic element
            symbs.append(ele)
        else:
            symbs += symbols(ele)
    return symbs


def operators(s1):  # should not include not?
    # return all the operators in a nested symbol
    oprts = [].append(s1.type)
    if not s1.params:
        return oprts
    for ele in s1.params:
        if ele.params:
            oprts.append(ele.type)
            oprts += operators(ele)
    return oprts


if __name__ == "__main__":
    p = symbol()
    p.value = False
    print(p.type)
    np = pl_not(p)
    np.update()
    print(np.value)