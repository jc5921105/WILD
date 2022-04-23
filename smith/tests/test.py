from __future__ import print_function
import pdb, os, json
from smith.capabilities.search import search, straight_search, vague_search

FACTOR_LARGE = 1000
FACTOR_MEDIUM = 100
FACTOR_SMALL = 1
FACTOR_VARIABLE = 2000

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
                data = data[::FACTOR_LARGE]
            self._model[x]['data'] = data

    def test(self):
        for x in self._model.keys():
            print('Processing %s' % self._model[x]['path'])
            search_correct_cout, s_search_correct_count, v_search_correct_count = 0, 0, 0
            fout = open(os.path.join(self._res_loc,self._model[x]['file'].replace('.json','.results')),'w')
            for y in self._model[x]['data']:
                word = y[0]
                t_word = y[1]
                print('Testing: %s <> %s' % (word, t_word))
                r_s, r_ss, skeys = self._get_search_values(t_word)
                if not type(skeys) == type([]): skeys = list(skeys)
                fout.write('Original Word= %s\nMisspelled Word= %s\n\tL.D. Result = %s\n\tW.I.L.D Result = %s\n\tW.I.L.D Vague Search Keys= %s\n\n' % (word,t_word,r_ss, r_s,str(skeys)))
                if word == r_s: search_correct_cout += 1
                if word == r_ss: s_search_correct_count += 1
                if word in skeys: v_search_correct_count += 1
            self._set_values(s_search_correct_count, search_correct_cout, v_search_correct_count, x)
            fout.close()

    def _get_search_values(self, t_word):
        r_s = (search(t_word, self._app_model.full_dict))['word']
        r_ss = (straight_search(t_word, self._app_model.full_dict))['word']
        skeys = (vague_search(t_word, self._app_model.full_dict)).keys()
        return r_s, r_ss, skeys

    def _set_values(self, s_search_correct_count, search_correct_cout, v_search_correct_count, x):
        self._model[x]['search_correct_cout'] = search_correct_cout
        self._model[x]['s_search_correct_count'] = s_search_correct_count
        self._model[x]['v_search_correct_count'] = v_search_correct_count
        self._model[x]['search_accuracy'] = (float(search_correct_cout) / len(self._model[x]['data'])) * 100
        self._model[x]['s_search_accuracy'] = (float(s_search_correct_count) / len(self._model[x]['data'])) * 100
        self._model[x]['v_search_accuracy'] = (float(v_search_correct_count) / len(self._model[x]['data'])) * 100

    def print_accuracy(self):
        fout = open(os.path.join(self._res_loc, 'results.txt'), 'w')
        keys = self._model.keys()
        if not type(keys) == type([]): keys = list(keys)
        keys.sort()
        self._view.s_print('\n\nTest Results')
        for x in keys:
            self._view.s_print('\tTest Set: %s' % self._model[x]['file'])
            fout.write('Test Set: %s\n' % self._model[x]['file'])
            self._view.s_print('\t\tStraight L.D. Search Accuracy: {:.4f}%'.format(self._model[x]['s_search_accuracy']))
            fout.write('\tStraight L.D. Search Accuracy: {:.4f}%\n'.format(self._model[x]['s_search_accuracy']))
            self._view.s_print('\t\tW.I.L.D. Search Accuracy: {:.4f}%'.format(self._model[x]['search_accuracy']))
            fout.write('\tW.I.L.D. Search Accuracy: {:.4f}%\n'.format(self._model[x]['search_accuracy']))
            self._view.s_print('\t\tW.I.L.D. Vague Search Accuracy: {:.4f}%'.format(self._model[x]['v_search_accuracy']))
            fout.write('\tW.I.L.D. Vague Search Accuracy: {:.4f}%\n\n'.format(self._model[x]['v_search_accuracy']))
        fout.close()









if __name__ == '__main__':
    app = Test('/workspace/dev/test_env/WILD/smith/tests/set1')
