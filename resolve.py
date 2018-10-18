


def resolve(s1, s2):
    # resolve 2 sentences, return all the possible results in a list
    # resolve takes 2 set of symbols, each set comes from a sentence
    o1 = set(operators(s1))
    o2 = set(operators(s2))
    #if o1 != set("or") or o2 != set("or"):
    #    return False

    syms1 = symbols(s1)
    syms2 = symbols(s2)
    resolvent = []
    for sym1 in syms1:
        sym2 = compliment(sym1)
        if sym2 != None and sym2 in syms2:
            new_symbls = syms1 + syms2
            new_symbls.remove(sym1)
            new_symbls.remove(sym2)
            resolvent.append()

    for sym2 in syms2:
        sym1 = compliment(sym2)
        if sym1 != None and  sym1 in syms1:
            new_symbls = syms1 + syms2
            new_symbls.remove(sym1)
            new_symbls.remove(sym2)
            resolvent.append()