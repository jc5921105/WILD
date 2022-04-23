import pdb, re, json


REGEX = re.compile(r"""^\s*\"*(?P<text>[A-Za-z]+)""",re.X)


def self_analyze(model):
    keys = model.keys()
    t_model = {}
    for x in keys:
        #print(x)
        for y in model[x]['definitions'].keys():
            line = (model[x]['definitions'][y]).split(' ')
            for z in line:
                t = REGEX.match(z)
                if t:
                    if not (t.group('text')).lower() in model.keys():
                        t_model[(t.group('text')).lower()]  = {'word': (t.group('text')).lower(), 'definitions': {}}
    model.update(t_model)
    return model

