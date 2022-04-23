from __future__ import print_function
import pdb, re, json, random
from smith.capabilities.ld_calc import med_calc

SD_SIZE = 4 # Deviation Size
CUTOFF_WEIGHT = 9
MIN_POOL_SIZE = 1


def _get_data():
    with open('./temp_data.json','r') as fobj:
        data = json.load(fobj)
    return data


def _get_word_pool(model,word):
    return {x:model.get(x) for x in model.keys() if (x[0] == word[0] and (len(word) - SD_SIZE) <= len(x) <= (len(word) + SD_SIZE))}

def _get_large_word_pool(model,word):
    return {x:model.get(x) for x in model.keys() if (len(word) - SD_SIZE) <= len(x) <= (len(word) + SD_SIZE)}


def _get_options(model,pool_size = MIN_POOL_SIZE):
    sel_weight = 0
    while True:
        #print('itter')
        tt = {x:model.get(x) for x in model.keys() if model[x]['edit_distance'] <= sel_weight}
        if len(tt) < pool_size: sel_weight += 1
        elif sel_weight > CUTOFF_WEIGHT: return model
        else: break
    return tt


def _get_total_weight(model):
    tmp = 0
    for x in model: tmp = tmp + model[x]['weight']
    return tmp


def _weight_options(model,tw):
    for x in model:
        model[x]['probability'] = float(model[x]['weight']) / float(tw)
    return model


def _get_top_option(model):
    #pdb.set_trace()
    tmp = model[list(model.keys())[-1]]
    #pdb.set_trace()
    for x in model:
        if model[x]['probability'] > tmp['probability']: tmp = model[x]
    return tmp


def _get_random_option(model):
    keys = model.keys()
    if not type(keys) == type([]): keys = list(keys)
    if len(keys) == 1:
        #pdb.set_trace()
        return model[keys[0]]
    i = random.randint(0,len(keys)-1)
    return model[keys[i]]


def _calc_med(model,word):
    for x in model.keys():
        model[x]['edit_distance'] = med_calc(word,x)
    return model


def search(word,model):
    tmp = _get_word_pool(model,word)
    tmp = _calc_med(tmp,word)
    tmp = _get_options(tmp)
    tw  = _get_total_weight(tmp)
    tmp = _weight_options(tmp,tw)
    opt = _get_top_option(tmp)
    return opt


def deep_search(word,model):
    tmp = _get_large_word_pool(model,word)
    tmp = _calc_med(tmp,word)
    tmp = _get_options(tmp)
    tw  = _get_total_weight(tmp)
    tmp = _weight_options(tmp,tw)
    opt = _get_top_option(tmp)
    return opt


def vague_search(word,model):
    tmp = _get_word_pool(model,word)
    tmp = _calc_med(tmp,word)
    tmp = _get_options(tmp)
    tw  = _get_total_weight(tmp)
    tmp = _weight_options(tmp,tw)
    return tmp

def vague_search_large(word,model):
    tmp = _get_word_pool(model,word)
    tmp = _calc_med(tmp,word)
    tmp = _get_options(tmp, pool_size= 5)
    tw  = _get_total_weight(tmp)
    tmp = _weight_options(tmp,tw)
    return tmp

def deep_vague_search(word,model):
    tmp = _get_large_word_pool(model,word)
    tmp = _calc_med(tmp,word)
    tmp = _get_options(tmp)
    tw  = _get_total_weight(tmp)
    tmp = _weight_options(tmp,tw)
    return tmp


def straight_search(word,model):
    tmp = _get_word_pool(model,word)
    tmp = _calc_med(tmp,word)
    tmp = _get_options(tmp)
    for x in tmp:
        if tmp[x]['edit_distance'] == 0: return tmp[x]
    opt = _get_random_option(tmp)
    return opt

if __name__ == '__main__':

    data = _get_data()
    #while True:
    #    tmp = search(raw_input('Enter Word:'),data)
    #    print(tmp['word'])
    #    print(tmp)
    #    pdb.set_trace()
    tmp = straight_search('fluffie',data)

