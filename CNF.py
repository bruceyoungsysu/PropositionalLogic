from propositional_logic import *

class problems:
    def __init__(self):
        self.kb = []
        self.a = []


def elmnt_bid(self, sym):
    if sym.type != "bid":
        sym1, sym2 = sym.params[0], sym.params[1]
        if sym1.type != 'atom':
            pass

    return [pl_imply(sym1, sym2), pl_imply(sym2, sym1)]


def elmnt_imply(self, sym):
    if sym.type != "":
        pass

def elmnt_neg(self, sym):
    pass

def distr_and(self, sym):
    pass

def to_symbols(self, sym):
    # call above functions
    pass
