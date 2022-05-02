from __future__ import print_function
import pdb, re, json, random
from smith.capabilities.lcs_calc import lcs_calc

SD_SIZE = 4 # Deviation Size
CUTOFF_WEIGHT = 9
MIN_POOL_SIZE = 1


def _get_word_pool(model,word):
    return {x:model.get(x) for x in model.keys() if (x[0] == word[0] and (len(word) - SD_SIZE) <= len(x) <= (len(word) + SD_SIZE))}


def _get_random_option(model):
    keys = model.keys()
    if not type(keys) == type([]): keys = list(keys)
    if len(keys) == 1:
        return model[keys[0]]
    i = random.randint(0,len(keys)-1)
    return model[keys[i]]


def lcs_search(word,model):
    #Longest Common Subsequence
    tmp = _get_word_pool(model,word)
    tmp = _calc_lcs(tmp,word)
    tmp = _get_options_lcs(tmp)
    opt = _get_random_option(tmp)
    return opt


def _calc_lcs(model,word):
    for x in model.keys():
        model[x]['lcs_edit_distance'] = lcs_calc(word,x)
    return model


def _get_options_lcs(model,pool_size = MIN_POOL_SIZE):
    tmp = model[list(model.keys())[-1]]
    for x in model:
        if model[x]['lcs_edit_distance'] > tmp['lcs_edit_distance']: tmp = model[x]
        sel_weight = tmp['lcs_edit_distance']
    while True:
        tt = {x:model.get(x) for x in model.keys() if model[x]['lcs_edit_distance'] >= sel_weight}
        if len(tt) < pool_size: sel_weight -= 1
        else: break
    return tt

