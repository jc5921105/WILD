from __future__ import print_function
import pdb, re, json, random
from smith.capabilities.hd_calc import hd_calc

SD_SIZE = 4 # Deviation Size
CUTOFF_WEIGHT = 9
MIN_POOL_SIZE = 1


def _get_word_pool(model,word):
    return {x:model.get(x) for x in model.keys() if (x[0] == word[0] and (len(word) - SD_SIZE) <= len(x) <= (len(word) + SD_SIZE))}


def _get_random_option(model):
    keys = model.keys()
    if not type(keys) == type([]): keys = list(keys)
    if len(keys) == 1:
        #pdb.set_trace()
        return model[keys[0]]
    i = random.randint(0,len(keys)-1)
    return model[keys[i]]


def hd_search(word,model):
    #Hamming Distance Search
    tmp = _get_word_pool(model,word)
    tmp = _calc_hd(tmp,word)
    tmp = _get_options_hd(tmp)
    for x in tmp:
        if tmp[x]['hamming_distance'] == 0: return tmp[x]
    opt = _get_random_option(tmp)
    return opt


def _calc_hd(model,word):
    for x in model.keys():
        model[x]['hamming_distance'] = hd_calc(word,x)
    return model


def _get_options_hd(model,pool_size = MIN_POOL_SIZE):
    sel_weight = 0
    while True:
        #print('itter')
        tt = {x:model.get(x) for x in model.keys() if model[x]['hamming_distance'] <= sel_weight}
        if len(tt) < pool_size: sel_weight += 1
        elif sel_weight > CUTOFF_WEIGHT: return model
        else: break
    return tt

