from copy import deepcopy
from propositional_logic import  *
from CNF import problems


class resolved:
    def __init__(self):
        self.symbols = set()
        self.entropy = 0
        self.hash = ""

    def copy(self):
        new = resolved()
        for sym in self.symbols:
            new.symbols.add(sym)
        return new


def complement(sym1, sym2):
    # find the compliment of sym
    if sym1.type == sym2.type:
        return False

    if sym1.type == "not" and sym1.params[0] == sym2:
        return True
    if sym2.type == "not" and sym2.params[0] == sym1:
        return True

    return False


def resolve(sym_set1, sym_set2):
    # resolve 2 sentences, return all the possible results in a list
    # resolve takes 2 set of symbols, each set comes from a sentence
    resolved = []
    for s1 in sym_set1:
        for s2 in sym_set2:
            if complement(s1, s2):
                s1_new, s2_new = sym_set1.copy(), sym_set2.copy()
                s1_new.remove(s1)
                s2_new.remove(s2)
                s = s1_new | s2_new

                if s not in resolved:
                    resolved.append(s)
    return resolved


def proof(kb):
    resolve_all = []
    for i in range(len(kb)):
        knowledge = kb[i]
        for j in range(i+1,len(kb)):
           base = kb[j]
           resolved = resolve(knowledge, base)
           resolve_all += resolved

    if resolve_all == []:
        return False
    changed = False
    for r in resolve_all:
        if r == set():
            kb = []
            return changed, kb
        if r not in kb:
            kb.append(r)
            changed = True
    return changed, kb


def proof_by_resolution(kb):
    changed = True
    while True:
        if changed != False and len(kb)>0:
            changed, kb = proof(kb)
        else:
            break
        print(changed)

    if not kb:
        print("The conclusion is True !")
        return

    if changed == False:
        print("The conclusion is false !")

        return


class p1(problems):
    def __init__(self):
        P = symbol()
        p.name = "P"
        Q = symbol()
        Q.name = "Q"
        s1 = set([P])
        s2 = set([pl_not(P),Q])
        s3 = set([pl_not(Q)])
        self.kb = [s1,s2,s3]


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
        np11 = pl_not(p11)
        nb11 = pl_not(b11)
        np12 = pl_not(p12)
        s1 = set([np11])
        s2 = set([nb11, p12, p21])
        s3 = set([np12, b11])
        s4 = set([pl_not(p21), b11])
        s5 = set([pl_not(b21),p11,p22,p31])
        s6 = set([np11,b21])
        s7 = set([pl_not(p22),b21])
        s8 = set([pl_not(p31),b21])
        s9 = set([nb11])
        s10 = set([b21])
        s11 = set([pl_not(p12)])
        self.kb = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11]

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
        n_mythical = pl_not(mythical)
        n_mammal = pl_not(mammal)
        n_horned = pl_not(horned)
        n_magical = pl_not(magical)

        s1 = set([n_mythical,immortal])
        s2 = set([mythical, mortal])
        s3 = set([mythical, mammal])
        s4 = set([mortal,horned])
        s5 = set([n_mammal,horned])
        s6 = set([n_horned, magical])
        s7 = set([n_horned])

        self.kb = [s1,s2,s3,s4,s5,s6,s7]


class p4a(problems):
    def __init__(self):
        A = symbol()
        A.name = "A"
        B = symbol()
        B.name = "B"
        C = symbol()
        C.name = "C"

        nA = pl_not(A)
        nB = pl_not(B)
        nC = pl_not(C)

        s1 = set([nA,nC,A])
        s2 = set([nA,A])
        s3 = set([nA, C])
        s4 = set([C,B])
        s5 = set([nC,nB])
        s6 = set([nB,C])
        s7 = set([C,A])
        s8 = set([nC,B,nA])
        s9 = set([nC])
        self.kb = [s1,s2,s3,s4,s5,s6,s7,s8,s9]


class p4b(problems):
    def __init__(self):
        pass

if __name__ == "__main__":
    p = symbol()
    p.name = "P"
    q = symbol()
    q.name = "Q"
    kb = set()
    s1 = set([p,pl_not(q)])
    s2 = set([q,pl_not(p)])
    kb = [s1,s2]

    p1 = p1()
    p2 = p2()
    p3 = p3()
    p4a = p4a()
    proof_by_resolution(p4a.kb)
    #print(proof(p2.kb))