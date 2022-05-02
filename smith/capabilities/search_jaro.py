from __future__ import print_function
import pdb, re, json, random
from smith.capabilities.jaro_calc import jaro_calc, jw_calc


SD_SIZE = 4 # Deviation Size
CUTOFF_WEIGHT = 9
MIN_POOL_SIZE = 1


def _get_word_pool(model,word):
    return {x:model.get(x) for x in model.keys() if (x[0] == word[0] and (len(word) - SD_SIZE) <= len(x) <= (len(word) + SD_SIZE))}


def _calc_jaro(model,word):
    for x in model.keys():
        model[x]['jaro_sim'] = jaro_calc(word,x)
    return model


def _calc_jw(model,word):
    for x in model.keys():
        model[x]['jaro_sim'] = jw_calc(word,x)
    return model


def _get_options_jaro(model,pool_size = MIN_POOL_SIZE):
    sel_weight = 1
    while True:
        #tt = {x:model.get(x) for x in model.keys() if model[x]['jaro_sim'] == sel_weight}
        tt = {}
        for x in model.keys():
            #print(x,model[x]['jaro_sim'])
            if model[x]['jaro_sim'] > .99:
                tt[x] = model.get(x)
                print(x, model[x]['jaro_sim'])
        if len(tt) < pool_size: sel_weight += 100
        elif sel_weight > CUTOFF_WEIGHT: return model
        else: break
    return tt


def _filter_options(model):
    tmp = model[list(model.keys())[-1]]
    for x in model:
        if model[x]['jaro_sim'] > tmp['jaro_sim']: tmp = model[x]
    tt = {x: model.get(x) for x in model.keys() if model[x]['jaro_sim'] == tmp['jaro_sim']}
    return tt


def _get_top_option(model):
    tmp = model[list(model.keys())[-1]]
    for x in model:
        if model[x]['jaro_sim'] > tmp['jaro_sim']: tmp = model[x]
    return tmp


def _get_random_option(model):
    keys = model.keys()
    if not type(keys) == type([]): keys = list(keys)
    if len(keys) == 1:
        return model[keys[0]]
    i = random.randint(0,len(keys)-1)
    return model[keys[i]]


def jaro_search(word,model):
    #Jaro Search
    tmp = _get_word_pool(model,word)
    tmp = _calc_jaro(tmp,word)
    #tmp = _get_options_jaro(tmp)
    tmp = _filter_options(tmp)
    if len(tmp) > 1: opt = _get_random_option(tmp)
    else: opt = _get_top_option(tmp)
    return opt


def jw_search(word,model):
    #Jaro Winkler Search
    tmp = _get_word_pool(model,word)
    tmp = _calc_jw(tmp,word)
    #tmp = _get_options_jaro(tmp)
    tmp = _filter_options(tmp)
    if len(tmp) > 1: opt = _get_random_option(tmp)
    else: opt = _get_top_option(tmp)
    return opt
