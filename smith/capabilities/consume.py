from __future__ import print_function
import pdb, re, json, os

REGEX = re.compile(r"""^\s*\"*(?P<text>[A-Za-z]+)""",re.X)


def consume(model,location):
    if not os.path.isfile(location): return (False,'Cannot Find File: %s' % location)
    data = _get_lines(location)
    for line in data:
        line = line.split(' ')
        for z in line:
            t = REGEX.match(z)
            if t:
                #print(t.group('text'))
                word = t.group('text')
                word = word.lower()
                if not word in model.keys():
                    print('Unknown Word: %s ->  Adding to model' % word)
                    model[word] = {'word':word,'definitions':{},'weight':1}
                else:
                    if not 'weight' in model[word].keys():
                        model[word]['weight'] = 1
                    else:
                        model[word]['weight'] += 1
    return (True,model)


def _get_lines(location):
    with open(location, 'r') as fobj:
        data = fobj.readlines()
    return data