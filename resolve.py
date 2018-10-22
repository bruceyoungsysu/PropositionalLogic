from CNF import *


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


def proof(kb):
    resolve_all = []
    for i in range(len(kb)):
        knowledge = kb[i]
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


def proof1(kb, query):
    resolve_all = []
    for i in range(len(query)):
        knowledge = query[i]
        for j in range(i+1,len(query)):
            base = query[j]
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
            return changed, kb, []

        if r not in kb:
            changed = True
            kb.append(r)
    kb.sort(key=lambda i: len(i))
    return changed, kb, kb[:300]


def proof_by_resolution(kb):
    changed = True
    i = 0
    q = kb
    while True:
        if changed != False and len(kb) > 0:
            changed, kb, q = proof1(kb, q)
        else:
            break

    if not kb:
        return True
    if changed == False:
        return False


def output_modesl(kb, queries):
    for key in queries.keys():
        q = queries[key]
        new_kb = kb + [q]
        print(key + " : " + str(proof_by_resolution(new_kb)))


if __name__ == "__main__":

    problemSet = [problem1(),problem2(),problem3(), problem4a(), problem4b(),problem5(),problem6a(),problem6b()]
    for p in problemSet:
        print(p.name+": ")
        output_modesl(p.kb_r, p.a_r)
        print("*" * 20)