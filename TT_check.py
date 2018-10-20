from propositional_logic import *
from CNF import problems


symbols = []
chars = [] # ordered list, need a generator


def models_gen(chars):
    # generate symbols and all models from chars
    chars_index = {}
    models = []
    char_len = len(chars)
    for i in range(pow(2,char_len)):
        models.append(i)
    for i in range(char_len):
        chars_index[chars[i]] = pow(2,char_len-i-1)
    print(chars_index)
    return models, chars_index


def assert_kb(model, kb, chars_index):
    for knowldge in kb:
        if knowldge.assign(chars_index, model).value == False:
            return False
    return True


def entail(kb, a, chars):
    # assert whether kb entails a
    models, ch_ind = models_gen(chars)
    for model in models:
        if assert_kb(model, kb, ch_ind):
            print(bin(model))
            if not assert_kb(model, a, ch_ind):
                return False
    return True


class p2(problems):
    def __init__(self):
        p2 = problems()
        p11 = symbol()
        p11.name = "p11"
        np11 = pl_not(p11)
        p12 = symbol()
        p12.name = "p12"
        p21 = symbol()
        p21.name = "p21"
        p31 = symbol()
        p31.name = "p31"
        p22 = symbol()
        p22.name = "p22"
        b11 = symbol()
        b21 = symbol()
        b11.name = "b11"
        b21.name = "b21"

        self.kb = [pl_not(p11), pl_bid(b11, pl_or(p12, p21)), pl_bid(b21, pl_or(p11, pl_or(p22, p31))), pl_not(b11), b21]
        # p2.kb = [pl_bid(b11, pl_or(p12, p21)), pl_not(b11)]
        self.a = [pl_not(p12)]

class p3(problems):
    def __init__(self):
        mythical = symbol()
        mythical.name = "mythical"
        mortal = symbol()
        mortal.name = "mortal"
        mammal = symbol()
        mammal.name = "mammal"
        horned = symbol()
        horned.name = "horned"
        magical = symbol()
        magical.name = "magical"
        immortal = pl_not(mortal)
        self.kb = [pl_imply(mythical, immortal), pl_imply(pl_not(mythical), pl_and(mortal, mammal)),
                   pl_imply(pl_or(immortal, mammal), horned), pl_imply(horned, magical)]
        self.a = [horned]


class p4a(problems):
    def __init__(self):
        A = symbol()
        A.name = "A"
        B = symbol()
        B.name = "B"
        C = symbol()
        C.name = "C"
        self.kb = [pl_bid(A, pl_and(C,A)), pl_bid(B,pl_not(C)), pl_bid(C, pl_or(B, pl_not(A)))]
        self.a = []


class p4b(problems):
    def __init__(self):
        A = symbol()
        A.name = "A"
        B = symbol()
        B.name = "B"
        C = symbol()
        C.name = "C"
        self.kb = [pl_imply(A, pl_not(C)), pl_imply(B, pl_and(A,C)), pl_imply(C,B)]
        self.a = []

class p5(problems):
    def __init__(self):
        A = symbol()
        A.name = "A"
        B = symbol()
        B.name = "B"
        C = symbol()
        C.name = "C"
        D = symbol()
        D.name = "D"
        E = symbol()
        E.name = "E"
        F = symbol()
        F.name = "F"
        G = symbol()
        G.name = "G"
        H = symbol()
        H.name = "H"
        I = symbol()
        I.name = "I"
        J = symbol()
        J.name = "J"
        K = symbol()
        K.name = "K"
        L = symbol()
        L.name = "L"
        self.kb = [pl_bid(A,pl_and(H,I)), pl_bid(B, pl_and(A, L)), pl_bid(C, pl_and(B,G)), pl_bid(D, pl_and(E,L)),
                   pl_bid(E, pl_and(C,H)), pl_bid(F, pl_and(D, I)),pl_bid(G, pl_and(pl_not(E), pl_not(J))),
                   pl_bid(pl_or(F,K),pl_not(H)), pl_bid(pl_or(G,K), pl_not(I)), pl_bid(pl_or(A,C),pl_not(J)), pl_bid(pl_or(D,F), pl_not(K)),
                   pl_bid(pl_or(B,J),pl_not(L))]
        self.a = []


if __name__ == "__main__":
    models, ch_ind = models_gen(["P", "Q"])

    p = symbol()
    p.name = "P"
    q = symbol()
    q.name = "Q"

    p1 = problems()
    p1.kb = [pl_imply(p,q),p]
    p1.a = [q]

    #ind = {'mythical': 16, 'mortal': 8, 'mammal': 4, 'horned': 2, 'magical': 1}
    p2 = p2()
    p3 = p3()
    p4a = p4a()
    p4b = p4b()
    p5 = p5()
    print(entail(p5.kb, p5.a, ["A", "B", "C","D","E","F","G","H","I","J","K","L"]))
