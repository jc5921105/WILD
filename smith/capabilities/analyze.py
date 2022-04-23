from __future__ import print_function
import pdb, re, json


REGEX = re.compile(r"""^\s*\"*(?P<text>[A-Za-z\.]+)""",re.X)


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


def reset_weight(model):
    for x in model.keys():
        model[x]['weight'] = 1


def weight(model):
    keys = model.keys()
    keys.sort()
    for x in keys:
        print(x)
        for y in model[x]['definitions'].keys():
            line = (model[x]['definitions'][y]).split(' ')
            for z in line:
                t = REGEX.match(z)
                if t:
                    #print(t.group('text'))
                    if not t.group('text') in model.keys():
                        print('Unknown Word: %s -> Adding to model' % t.group('text'))
                        model[t.group('text')] = {'word':t.group('text'),'definitions':{},'weight':1}
                    else:
                        if not 'weight' in model[t.group('text')].keys():
                            model[t.group('text')]['weight'] = 1
                        else:
                            model[t.group('text')]['weight'] += 1
    return model