import json, pdb, os, sys
import smith.memory
from smith.model_libs import analyize
from smith.model_libs import define
from smith.model_libs import weight

FILE_NAME = 'dictionary.json'


class Model:
    def __init__(self):
        self._dict_path = self._get_dict_path()
        self._build_model()
        self._build_dictionaries()

    def _get_dict_path(self):
        dir = os.path.dirname(smith.memory.__file__)
        return os.path.join(dir,FILE_NAME)

    def _build_model(self):
        with open(self._dict_path,'r') as fobj:
            self.full_model = json.load(fobj)

    def write_memory(self):
        with open(self._dict_path,'w') as fobj:
            json.dump(self.full_model,fobj,sort_keys=True,indent=4)

    def get_size(self):
        return len(self.full_model.keys())

    def _build_dictionaries(self):
        self.a_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'a'}
        self.b_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'b'}
        self.c_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'c'}
        self.d_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'd'}
        self.e_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'e'}
        self.f_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'f'}
        self.g_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'g'}
        self.h_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'h'}
        self.i_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'i'}
        self.j_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'j'}
        self.k_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'k'}
        self.l_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'l'}
        self.m_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'm'}
        self.n_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'n'}
        self.o_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'o'}
        self.p_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'p'}
        self.q_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'q'}
        self.r_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'r'}
        self.s_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 's'}
        self.t_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 't'}
        self.u_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'u'}
        self.v_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'v'}
        self.w_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'w'}
        self.x_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'x'}
        self.y_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'y'}
        self.z_dict = {k: self.full_model.get(k) for k in self.full_model.keys() if k[0].lower() == 'z'}
        self.full_dict = self.full_model

    def self_analyze(self):
        self.full_model = analyize.self_analyze(self.full_model)

    def self_define(self):
        self.full_model = define.self_define(self.full_model,self._dict_path)

    def self_weight(self):
        self.full_model = weight.reset_weight(self.full_model)
        self.full_model = weight.weight(self.full_model)