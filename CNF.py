from propositional_logic import *


class problems:
    def __init__(self):
        self.kb = []
        self.a = {}
        self.chars = []
        self.qs = []
        self.a_r = {}
        self.name = ""

    def init_models(self):
        for i in range(len(self.chars)):
            globals()[self.chars[i]] = symbol()
            globals()[self.chars[i]].name = self.chars[i]
            globals()["n" + self.chars[i]] = pl_not(globals()[self.chars[i]])
            if self.chars[i] in self.qs:
                self.a[self.chars[i]] = globals()[self.chars[i]]
                self.a_r[self.chars[i]] = {globals()["n" + self.chars[i]]}


class problem1(problems):
    def __init__(self):
        problems.__init__(self)
        self.name = "problem1"
        self.chars = ["P", "Q"]
        self.qs = ["Q"]
        self.init_models()
        self.kb = [pl_imply(P,Q),P]

        self.kb_r = [{P}, {pl_not(P), Q}, {pl_not(Q)}]


class problem2(problems):
    def __init__(self):
        problems.__init__(self)
        self.name = "problem2"
        self.chars = ["p11","p12", "p21", "p31", "p22", "b11", "b21"]
        self.qs = ["p21"]
        self.init_models()
        self.kb = [pl_not(p11), pl_bid(b11, pl_or(p12, p21)), pl_bid(b21, pl_or(p11, pl_or(p22, p31))), pl_not(b11),
                   b21]

        self.kb_r = [{np11}, {nb11, p12, p21}, {np12, b11}, {pl_not(p21), b11}, {pl_not(b21), p11, p22, p31},
                     {np11, b21}, {pl_not(p22), b21}, {pl_not(p31), b21}, {nb11}, {b21}, {pl_not(p12)}]


class problem3(problems):
    def __init__(self):
        problems.__init__(self)
        self.name = "problem3"
        self.chars = ["mythical", "mortal", "mammal", "horned", "magical"]
        self.qs = ["mythical", "magical", "horned"]
        self.init_models()
        immortal = pl_not(mortal)
        self.kb = [pl_imply(mythical, immortal), pl_imply(pl_not(mythical), pl_and(mortal, mammal)),
                   pl_imply(pl_or(immortal, mammal), horned), pl_imply(horned, magical)]

        self.kb_r = [{nmythical,immortal}, {mythical,mortal}, {mythical, mammal}, {mortal, horned},
                                          {nmammal, horned}, {nhorned, magical}]


class problem4a(problems):
    def __init__(self):
        problems.__init__(self)
        self.name = "problem4_a"
        self.chars = ["A", "B", "C"]
        self.qs = self.chars
        self.init_models()
        self.kb = [pl_bid(A, pl_and(C,A)), pl_bid(B,pl_not(C)), pl_bid(C, pl_or(B, pl_not(A)))]

        self.kb_r = [{nA, nC, A}, {nA, A}, {nA, C}, {C, B}, {nC, nB},
                     {nB, C}, {C, A}, {nC, B, nA}]


class problem4b(problems):
    def __init__(self):
        problems.__init__(self)
        self.name = "problem4_b"
        self.chars = ["A", "B", "C"]
        self.qs = self.chars
        self.init_models()
        self.kb = [pl_bid(A, pl_not(C)), pl_bid(B, pl_and(A,C)), pl_bid(C,B)]

        self.kb_r = [{nA, nC}, {C,A}, {nB, A}, {nB, C}, {nA, nC, B}, {nC, B}, {C, nB}]


class problem5(problems):
    def __init__(self):
        problems.__init__(self)
        self.name = "problem5"
        self.chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        self.qs = self.chars
        self.init_models()
        self.kb = [pl_bid(A, pl_and(H, I)), pl_bid(B, pl_and(A, L)), pl_bid(C, pl_and(B, G)), pl_bid(D, pl_and(E, L)),
                   pl_bid(E, pl_and(C, H)), pl_bid(F, pl_and(D, I)), pl_bid(G, pl_and(pl_not(E), pl_not(J))),
                   pl_bid(pl_or(F, K), pl_not(H)), pl_bid(pl_or(G, K), pl_not(I)), pl_bid(pl_or(A, C), pl_not(J)),
                   pl_bid(pl_or(D, F), pl_not(K)),
                   pl_bid(pl_or(B, J), pl_not(L))]

        self.kb_r = [{nA, H}, {nA,I}, {nH,nI,A}, {nB,A}, {nB,L}, {nA,nL,B}, {nC,B}, {nC,G},{nB,nG,C}, {nD,E}, {nD,L}, {nE,nL,D}, {nE,C},
                        {nE,H}, {nC,nH,E}, {nF,D}, {nF,I}, {nD,nI,F}, {nG,nE},{nG,nJ}, {E,J,G}, {nH,nF}, {nH,nK},{F,K,H},{nI,nG}, {nI,nK},
                        {G,K,I}, {nJ,nA}, {nJ,nC}, {A,C,J}, {nK,nD}, {nK,nF}, {D,F,K}, {nL,nB},{nL,nJ}, {B,J,L}]


class problem6a(problems):
    def __init__(self):
        problems.__init__(self)
        self.name = "problem6_a"
        self.chars = ["A", "B", "C", "D", "E", "F", "G", "H", "X", "Y", "Z", "W"]
        self.qs = ["X", "Y", "Z", "W"]
        self.init_models()

        self.kb = [pl_bid(A,X), pl_bid(B, pl_or(Y, Z)), pl_bid(C, pl_and(A,B)), pl_bid(D, pl_and(X, Y)),
                   pl_bid(E, pl_and(X,Z)), pl_bid(F, pl_or(D, E)), pl_bid(G, pl_imply(C,F)), pl_bid(H, pl_imply(pl_and(G,H), A))]

        self.kb_r = [{nA,X}, {nX, A}, {nB, Y, Z}, {nY, B}, {nZ, B}, {nC, A}, {nC, B}, {nB, nA, C},
                        {nD, X}, {nD, Y}, {nX, nY, D}, {nE, X}, {nE, Z}, {nX, nZ, E},{nF, D, E}, {nF, nE, nD}, {nD, E, F}, {D, nE, F},
                        {nG, nC, F}, {C, G}, {nF, G}, {G, H}, {H, nA}, {H}, {nG, nH, A},{X, Y, Z, W}]


class problem6b(problems):
    def __init__(self):
        problems.__init__(self)
        self.name = "problem6_b"
        self.chars = ["A", "B", "C", "D", "E", "F", "G", "H", "X", "Y", "Z", "W"]
        self.qs = ["X", "Y", "Z", "W"]
        self.init_models()
        all_or = pl_or(pl_or(pl_or(A,pl_or(B,X)),pl_or(C,pl_or(D,Y))), pl_or(pl_or(E,pl_or(F, Z)), pl_or(G,pl_or(H, W))))
        self.kb = [pl_bid(A,X), pl_bid(B, pl_or(Y, Z)), pl_bid(C, A), pl_bid(D, pl_and(X, Y)),
                   pl_bid(E, pl_and(X,Z)), pl_bid(F, pl_or(D, E)), pl_bid(G, all_or), pl_bid(H, pl_imply(pl_and(G,H), A))]

        self.kb_r = [{nA, X}, {nX, A}, {nB, Y, Z}, {nY, B}, {nZ, B}, {nC, A},
                        {nA, C}, {nD, X}, {nD, Y}, {nX, nY, D}, {nE, X}, {nE, Z}, {nX, nZ, E},
                        {nF, D, E}, {nF, nE, nD}, {nD, E, F}, {D, nE, F},{G, H}, {H, A}, {nG, nH, A}, {X, Y, Z, W},
                        {nG, A, B, C, D, E, F, G, H, X, Y, Z, W}, {nA, G}, {nB, G}, {nB, G}, {nD, G}, {nE, G}, {nF, G},
                        {nG, G}, {nH, G}, {nX, G}, {nY, G}, {nZ, G}, {nW, G}]


def elmnt_bid(sym):

    if sym.type == "atom":
        return sym
    for i in range(len(sym.params)):
        sym.params[i] = elmnt_bid(sym.params[i])
    if sym.type == "bid":
        sym1 = sym.params[0]
        sym2 = sym.params[1]
        return pl_and(pl_imply(sym1, sym2), pl_imply(sym2, sym1))
    return sym


def elmnt_imply(sym):
    if sym.type == "atom":
        return sym
    for i in range(len(sym.params)):
        sym.params[i] = elmnt_imply(sym.params[i])
    if sym.type == "imply":
        sym1 = sym.params[0]
        sym2 = sym.params[1]
        return pl_or(pl_not(sym1), sym2)
    return sym


def elmnt_neg(sym):
    if sym.type == "atom":
        return sym
    if sym.type == "not":
        child = sym.params[0]
        if child.type == "not":
            sym = child.params[0]
        elif child.type == "or":
            sym = pl_and(pl_not(child.params[0]),pl_not(child.params[1]))
        elif child.type == "and":
            sym = pl_or(pl_not(child.params[0]),pl_not(child.params[1]))
        elif child.type == "atom":
            sym = sym

    for i in range(len(sym.params)):
        sym.params[i] = elmnt_neg(sym.params[i])
    return sym


def distr_and(sym):
    if sym.type == "atom" or sym.type == "not":
        return sym

    if sym.type == "or":
        sym1 = sym.params[0]
        sym2 = sym.params[1]
        if sym1.type == "and":
            sym =  pl_and(pl_or(sym1.params[0], sym2), pl_or(sym1.params[1], sym2))
        elif sym2.type == "and":
            sym = pl_and(pl_or(sym2.params[0], sym1), pl_or(sym2.params[1], sym1))

    for i in range(len(sym.params)):
        sym.params[i] = distr_and(sym.params[i])
    return sym


def to_symbols(sym):
    symbols = []
    ss = set()
    if sym.type == "atom" or sym.type == "not":
        ss.add(sym)
        return ss
    if sym.type == "or":
        s1 = to_symbols(sym.params[0])
        s2 = to_symbols(sym.params[1])
        ss = s1 | s2
        return ss
    if sym.type == "and":
        s1 = to_symbols(sym.params[0])
        s2 = to_symbols(sym.params[1])
        if type(s1) == type(set()):
            symbols.append(s1)
        else:
            symbols += s1

        if type(s2) == type(set()):
            symbols.append(s2)
        else:
            symbols += s2
        return symbols


if __name__ == "__main__":
    a = symbol()
    b = symbol()
    c = symbol()
    d = symbol()
    ab = pl_imply(a, b)
    cd = pl_imply(c, d)
    abc = pl_imply(cd, ab)
    q = elmnt_imply(abc)
    q = elmnt_neg(q)
    q = distr_and(q)
    #print(q.params)
    print(to_symbols(q))
