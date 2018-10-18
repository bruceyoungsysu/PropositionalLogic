
class symbol:

    def __init__(self):
        self.type = "atom"
        self.value = None
        self.params = []
        self.name = ""

    def assign(self,dic):
        for k in dic.keys:
            if k == self.name:
                self.value = dic[k]
            elif self.params:
                for p in self.params:
                    p.assign(dic)
                self.update()
        return self

    def update(self):
        pass


def pl_not(sym:symbol):
    new_sym = symbol()
    new_sym.value = not sym.value
    new_sym.type = "not"
    new_sym.params = sym
    return new_sym


def pl_and(sym1:symbol, sym2:symbol):
    new_sym = symbol()
    new_sym.value = sym1.value and sym2.value
    new_sym.type = "and"
    new_sym.params = [sym1,sym2]
    return new_sym


def pl_or(sym1:symbol, sym2:symbol):
    new_sym = symbol()
    new_sym.value = sym1.value or sym2.value
    new_sym.type = "or"
    new_sym.params = [sym1, sym2]
    return new_sym


def pl_imply(sym1:symbol,sym2:symbol):
    new_sym = symbol()
    if sym1.value == True and sym2.value == False:
        new_sym.value = False
    else:
        new_sym.value = True
    new_sym.type = "imply"
    new_sym.params = [sym1, sym2]
    return new_sym


def pl_bid(sym1:symbol, sym2:symbol):
    # biconditional
    new_sym = symbol()
    if sym1.value == sym2.value:
        new_sym.value = True
    else:
        new_sym.value = False
    new_sym.type = 'bid'
    new_sym.params = [sym1, sym2]
    return new_sym


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


def compliment(sym):
    # find the compliment of sym
    comp = symbol()
    if sym.type != "not" or sym.params == [] or sym.params[0].type != "atom":
        return None
    return sym.params[0]


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
