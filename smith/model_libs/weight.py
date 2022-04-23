from __future__ import print_function
import pdb, re, json


REGEX = re.compile(r"""^\s*\"*(?P<text>[A-Za-z\.]+)""",re.X)


def reset_weight(model):
    for x in model.keys():
        model[x]['weight'] = 1
    return model


def weight(model):
    keys = list(model.keys())
    if type(keys) != type([]):
        keys = list(model.keys())
    keys.sort()

    for x in keys:
        print(x)
        for y in model[x]['definitions'].keys():
            line = (model[x]['definitions'][y]).split(' ')
            for z in line:
                t = REGEX.match(z)
                if t:
                    #print(t.group('text'))
                    if not (t.group('text')).lower() in model.keys():
                        print('Unknown Word: %s. Adding to model' % t.group('text'))
                        model[(t.group('text')).lower()] = {'word':(t.group('text')).lower(),'definitions':{},'weight':1}
                    else:
                        if not 'weight' in model[(t.group('text')).lower()].keys():
                            model[(t.group('text')).lower()]['weight'] = 1
                        else:
                            model[(t.group('text')).lower()]['weight'] += 1
    return model