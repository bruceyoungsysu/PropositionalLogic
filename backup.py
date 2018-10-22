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
        #A = symbol()
        #A.name = "A"
        B = symbol()
        B.name = "B"
        C = symbol()
        C.name = "C"
        self.kb = [pl_imply(A, pl_not(C)), pl_imply(B, pl_and(A,C)), pl_imply(C,B)]
        self.a = []


class p5(problems):
    def __init__(self):
        self.chars = ["A", "B", "C","D","E","F","G","H","I","J","K","L"]
        for i in range(len(self.chars)):
            name = self.chars[i]
            globals()[self.chars[i]] = symbol()
            globals()[self.chars[i]].name = self.chars[i]
        print(A)
        self.kb = [pl_bid(A,pl_and(H,I)), pl_bid(B, pl_and(A, L)), pl_bid(C, pl_and(B,G)), pl_bid(D, pl_and(E,L)),
                   pl_bid(E, pl_and(C,H)), pl_bid(F, pl_and(D, I)),pl_bid(G, pl_and(pl_not(E), pl_not(J))),
                   pl_bid(pl_or(F,K),pl_not(H)), pl_bid(pl_or(G,K), pl_not(I)), pl_bid(pl_or(A,C),pl_not(J)), pl_bid(pl_or(D,F), pl_not(K)),
                   pl_bid(pl_or(B,J),pl_not(L))]
        self.a = []

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

def proof2(kb):
    resolve_all = []
    for i in range(len(kb)):
        knowledge = kb[i]
        if len(knowledge) >= 3:
            continue
        for j in range(i+1,len(kb)):
            base = kb[j]

            resolved = resolve(knowledge, base)
            for r in resolved:
                if r not in resolve_all:
                    resolve_all.append(r)

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
