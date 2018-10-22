from propositional_logic import *
from CNF import *


def models_gen(chars):
    # generate symbols and all models from chars
    chars_index = {}
    models = []
    char_len = len(chars)
    for i in range(pow(2,char_len)):
        models.append(i)
    for i in range(char_len):
        chars_index[chars[i]] = pow(2,char_len-i-1)
    return models, chars_index


def assert_kb(model, kb, chars_index):
    for knowldge in kb:
        if knowldge.assign(chars_index, model).value == False:
            return False
    return True


def entail(kb, a, chars):
    # assert whether kb entails alpha
    models, ch_ind = models_gen(chars)
    for model in models:
        if assert_kb(model, kb, ch_ind):
            if not assert_kb(model, a, ch_ind):
                return False
    return True


def output_result(prblm):
    kb = prblm.kb
    for key in prblm.a.keys():
        a = prblm.a[key]
        chars = prblm.chars
        print(key + " : " + str(entail(kb, [a], chars)))


if __name__ == "__main__":

    problemSet = [problem1(), problem2(), problem3(), problem4a(), problem4b(), problem5(), problem6a(), problem6b()]
    for p in problemSet:
        print(p.name + ": ")
        output_result(p)
        print("*" * 20)

