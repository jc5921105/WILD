from __future__ import print_function
import pdb, re, json, random
from smith.capabilities.cos_sim_calc import cos_sim_calc

SD_SIZE = 4 # Deviation Size
CUTOFF_WEIGHT = 9
MIN_POOL_SIZE = 1


def _get_word_pool(model,word):
    return {x:model.get(x) for x in model.keys() if (x[0] == word[0] and (len(word) - SD_SIZE) <= len(x) <= (len(word) + SD_SIZE))}


def cs_search(word,model):
    #Cosine Similarity Search
    tmp = _get_word_pool(model,word)
    tmp = _calc_cs(tmp,word)
    opt = _get_top_option(tmp)
    return opt


def _calc_cs(model,word):
    for x in model.keys():
        model[x]['cos_sim'] = cos_sim_calc(word,x)
    return model


def _get_top_option(model):
    tmp = model[list(model.keys())[-1]]
    for x in model:
        if model[x]['cos_sim'] > tmp['cos_sim']: tmp = model[x]
    return tmp




