import pdb, os
import json


from smith.capabilities import mw_web_lookup

def get_count(model):
    count = 0
    for x in model.keys():
        if len(model[x]['definitions']) == 0:
            count += 1
    return count


def self_define(model,fpath):
    count = 0
    for x in model.keys():
        if (len(model[x]['definitions'].keys())) == 0:
            try:
                model[x]['definitions'] = mw_web_lookup.get_definitions(x)
                count += 1
                if count % 10 == 0:
                    print('Writing Model Count: %s Current Word: %s ' % (count,x))
                    _write_mem(fpath,model)
            except:
                pass

    return model


def _write_mem(pth,model):
    with open(pth,'w') as fobj:
        json.dump(model,fobj,sort_keys=True,indent=4)
