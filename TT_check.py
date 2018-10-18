
symbols = []
chars = [] # ordered list

def models_gen(chars):
    # generate symbols and all models from chars
    chars_index = {}
    models = []
    char_len = len(chars)
    for i in range(pow(2,char_len)):
        models.append(bin(i))
    for i in range(char_len):
        chars_index[chars[i]] = bin(char_len-i)
    return models


def assert_kb(model, kb):
    for knowldge in kb:
        if knowldge.name in model.keys:
            knowldge.value = model
    pass


if __name__ == "__main__":
    models_gen(["P","Q"])