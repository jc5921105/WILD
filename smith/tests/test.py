from __future__ import print_function
import pdb, os, json
from smith.capabilities.search import search, straight_search, vague_search, get_temp_model
from smith.capabilities.search_lcs import lcs_search
from smith.capabilities.search_hd import hd_search
from smith.capabilities.search_cos import cs_search
from smith.capabilities.search_dld import dld_search
from smith.capabilities.search_jaro import jaro_search, jw_search

FACTOR_LARGE = 1000
FACTOR_MEDIUM = 100
FACTOR_SMALL = 1
FACTOR_VARIABLE = 3000


class Test:
    def __init__(self,tests_location, app_model, view, res_loc):
        self.loc = tests_location
        self._res_loc = res_loc
        self._app_model = app_model
        self._view = view
        self._model = {}
        self._get_files()
        self._build_test_lists()

    def _get_files(self):
        for x in os.listdir(self.loc):
            if '.json' in x: self._model[x] = {'file':x,'path': os.path.join(self.loc,x)}

    def _build_test_lists(self):
        for x in self._model.keys():
            with open(self._model[x]['path'],'r') as fobj:
                data = json.load(fobj)
                data = data[::FACTOR_SMALL]
            self._model[x]['data'] = data
            self._model[x]['results'] = {}

    def test(self):
        for x in self._model.keys():
            print('Processing %s' % self._model[x]['path'])
            search_correct_cout, s_search_correct_count, v_search_correct_count, dld_search_correct_count = 0, 0, 0, 0
            lcs_search_correct_count, hd_search_correct_count, cos_search_correct_count, jaro_search_correct_count, jw_search_correct_count = 0, 0, 0, 0, 0
            fout = open(os.path.join(self._res_loc,self._model[x]['file'].replace('.json','.results')),'w')
            for y in self._model[x]['data']:
                word = y[0]
                t_word = y[1]
                print('Testing: %s <> %s' % (word, t_word))
                r_s, r_ss, skeys, r_dld, r_lcs, r_hd, r_cs, r_jaro, r_jw = self._get_search_values(t_word)
                if not type(skeys) == type([]): skeys = list(skeys)
                fout.write('Original Word = %s'
                           '\nMisspelled Word = %s'
                           '\n\tL.D. Result =                            %s'
                           '\n\tW.I.L.D Result =                         %s'
                           '\n\tW.I.L.D Vague Search Keys=               %s'
                           '\n\tDamerau Levenshtein Result =             %s'
                           '\n\tLongest Common Subsequence Result =      %s'
                           '\n\tHamming Distance Search Result =         %s'
                           '\n\tCosine Similarity Search Results =       %s'
                           '\n\tJaro Similarity Search Results =         %s'
                           '\n\tJaro Winkler Similarity Search Results = %s'
                           '\n\n' % (word,t_word,r_ss, r_s,str(skeys),r_dld, r_lcs, r_hd, r_cs,r_jaro,r_jw))
                if word == r_s: search_correct_cout += 1
                if word == r_ss: s_search_correct_count += 1
                if word in skeys: v_search_correct_count += 1
                if word == r_dld: dld_search_correct_count += 1
                if word == r_lcs: lcs_search_correct_count += 1
                if word == r_hd: hd_search_correct_count += 1
                if word == r_cs: cos_search_correct_count += 1
                if word == r_jaro: jaro_search_correct_count += 1
                if word == r_jw: jw_search_correct_count += 1
                self._set_word_results(r_jw, r_jaro, r_cs, r_hd, r_lcs, r_dld, r_s, r_ss, skeys, x, word, t_word)
            self._set_values(s_search_correct_count, search_correct_cout, v_search_correct_count, x,
                             dld_search_correct_count, lcs_search_correct_count, hd_search_correct_count,
                             cos_search_correct_count, jaro_search_correct_count, jw_search_correct_count)
            fout.close()

    def _get_search_values(self, t_word):
        tmp = get_temp_model(t_word,self._app_model.full_dict)
        r_s = (search(t_word, tmp))['word']
        r_ss = (straight_search(t_word, tmp))['word']
        skeys = (vague_search(t_word, tmp)).keys()
        r_dld = (dld_search(t_word, tmp))['word']
        r_lcs = (lcs_search(t_word, tmp))['word']
        r_hd = (hd_search(t_word,tmp))['word']
        r_cs = (cs_search(t_word,tmp))['word']
        r_jaro = (jaro_search(t_word,tmp))['word']
        r_jw = (jw_search(t_word,tmp))['word']
        return r_s, r_ss, skeys, r_dld, r_lcs, r_hd, r_cs, r_jaro, r_jw

    def _set_word_results(self,r_jw, r_jaro, r_cs, r_hd, r_lcs, r_dld, r_s, r_ss, skeys, x,oword,tword):
        self._model[x]['results'][oword] = {}
        self._model[x]['results'][oword]['word'] = oword
        self._model[x]['results'][oword]['test_word'] = tword
        self._model[x]['results'][oword]['word_weight'] = self._app_model.full_dict[oword]['weight']
        self._model[x]['results'][oword]['wild_result'] = r_s
        self._model[x]['results'][oword]['ld_result'] = r_ss
        self._model[x]['results'][oword]['wild_v_result'] = skeys
        self._model[x]['results'][oword]['dld_result'] = r_dld
        self._model[x]['results'][oword]['lcs_result'] = r_lcs
        self._model[x]['results'][oword]['hd_result'] = r_hd
        self._model[x]['results'][oword]['cs_result'] = r_cs
        self._model[x]['results'][oword]['jaro_result'] = r_jaro
        self._model[x]['results'][oword]['jw_result'] = r_jw


    def _set_values(self, s_search_correct_count, search_correct_cout, v_search_correct_count, x,
                    dld_correct_count, lcs_search_correct_count, hd_search_correct_count, cos_search_correct_count,
                    jaro_search_correct_count, jw_search_correct_count):
        self._model[x]['search_correct_cout'] = search_correct_cout
        self._model[x]['s_search_correct_count'] = s_search_correct_count
        self._model[x]['v_search_correct_count'] = v_search_correct_count
        self._model[x]['dld_search_correct_count'] = dld_correct_count
        self._model[x]['lcs_search_correct_count'] = lcs_search_correct_count
        self._model[x]['hd_search_correct_count'] = hd_search_correct_count
        self._model[x]['cos_search_correct_count'] = cos_search_correct_count
        self._model[x]['jaro_search_correct_count'] = jaro_search_correct_count
        self._model[x]['jw_search_correct_count'] = jw_search_correct_count
        self._model[x]['search_accuracy'] = (float(search_correct_cout) / len(self._model[x]['data'])) * 100
        self._model[x]['s_search_accuracy'] = (float(s_search_correct_count) / len(self._model[x]['data'])) * 100
        self._model[x]['v_search_accuracy'] = (float(v_search_correct_count) / len(self._model[x]['data'])) * 100
        self._model[x]['dld_search_accuracy'] = (float(dld_correct_count) / len(self._model[x]['data'])) * 100
        self._model[x]['lcs_search_accuracy'] = (float(lcs_search_correct_count) / len(self._model[x]['data'])) * 100
        self._model[x]['hd_search_accuracy'] = (float(hd_search_correct_count) / len(self._model[x]['data'])) * 100
        self._model[x]['cs_search_accuracy'] = (float(cos_search_correct_count) / len(self._model[x]['data'])) * 100
        self._model[x]['jaro_search_accuracy'] = (float(jaro_search_correct_count) / len(self._model[x]['data'])) * 100
        self._model[x]['jw_search_accuracy'] = (float(jw_search_correct_count) / len(self._model[x]['data'])) * 100

    def print_accuracy(self):
        fout = open(os.path.join(self._res_loc, 'results.txt'), 'w')
        keys = self._model.keys()
        if not type(keys) == type([]): keys = list(keys)
        keys.sort()
        self._view.s_print('\n\nTest Results')
        for x in keys:
            fout.write('Test Set: %s\n' % self._model[x]['file'])
            fout.write('\tStraight L.D. Search Accuracy:              {:.4f}%\n'.format(self._model[x]['s_search_accuracy']))
            fout.write('\tW.I.L.D. Search Accuracy:                   {:.4f}%\n'.format(self._model[x]['search_accuracy']))
            fout.write('\tW.I.L.D. Vague Search Accuracy:             {:.4f}%\n'.format(self._model[x]['v_search_accuracy']))
            fout.write('\tDamerau Levenshtein Search Accuracy:        {:.4f}%\n'.format(self._model[x]['dld_search_accuracy']))
            fout.write('\tLongest Common Subsequence Search Accuracy: {:.4f}%\n'.format(self._model[x]['lcs_search_accuracy']))
            fout.write('\tHamming Distance Search Accuracy:           {:.4f}%\n'.format(self._model[x]['hd_search_accuracy']))
            fout.write('\tCosine Similarity Search Accuracy:          {:.4f}%\n'.format(self._model[x]['cs_search_accuracy']))
            fout.write('\tJaro Similarity Search Accuracy:            {:.4f}%\n'.format(self._model[x]['jaro_search_accuracy']))
            fout.write('\tJaro Winkler Similarity Search Accuracy:    {:.4f}%\n\n'.format(self._model[x]['jw_search_accuracy']))
            self._view.s_print('\tTest Set: %s' % self._model[x]['file'])
            self._view.s_print('\t\tStraight L.D. Search Accuracy:              {:.4f}%'.format(self._model[x]['s_search_accuracy']))
            self._view.s_print('\t\tW.I.L.D. Search Accuracy:                   {:.4f}%'.format(self._model[x]['search_accuracy']))
            self._view.s_print('\t\tW.I.L.D. Vague Search Accuracy:             {:.4f}%'.format(self._model[x]['v_search_accuracy']))
            self._view.s_print('\t\tDamerau Levenshtein Search Accuracy:        {:.4f}%'.format(self._model[x]['dld_search_accuracy']))
            self._view.s_print('\t\tLongest Common Subsequence Search Accuracy: {:.4f}%'.format(self._model[x]['lcs_search_accuracy']))
            self._view.s_print('\t\tHamming Distance Search Accuracy:           {:.4f}%'.format(self._model[x]['hd_search_accuracy']))
            self._view.s_print('\t\tCosine Similarity Search Accuracy:          {:.4f}%'.format(self._model[x]['cs_search_accuracy']))
            self._view.s_print('\t\tJaro Similarity Search Accuracy:            {:.4f}%'.format(self._model[x]['jaro_search_accuracy']))
            self._view.s_print('\t\tJaro Winkler Similarity Search Accuracy:    {:.4f}%'.format(self._model[x]['jw_search_accuracy']))

        fout.close()

    def dump_model(self):
        with open(os.path.join(self._res_loc, 'results.json'), 'w') as fobj:
            json.dump(self._model,fobj,sort_keys=True,indent=4)


if __name__ == '__main__':
    app = Test('/workspace/dev/test_env/WILD/smith/tests/set1')
