from __future__ import print_function
import pdb
from smith.handlers.entry_handler import EntryHandler
from smith.handlers.define_request import DefineRequestHandler
from smith.handlers.spell_request import SpellRequestHandler
from smith.handlers.unknown_handler import UnkownHandler
from smith.handlers.end_request import EndRequestHandler
from smith.handlers.training_handler import TrainingRequestHandler
from smith.handlers.size_request import SizeRequestHandler
from smith.handlers.mem_request import MemRequestHandler
from smith.handlers.possible_spell_request import PossibleSpellRequestHandler
from smith.handlers.help_request import HelpRequestHandler
from smith.handlers.consumption_handler import ConsumptionHandler
from smith.handlers.test_handler import TestRequestHandler

class RequestController:
    def __init__(self,model,view):
        self._model = model
        self._view = view
        self._build_handlers()
        self._link_handlers()

    def _link_handlers(self):
        self._entry_handler.set_next(self._consumption_handler)
        self._consumption_handler.set_next(self._end_handler)
        self._end_handler.set_next(self._spell_request)
        self._spell_request.set_next(self._possible_spell_request)
        self._possible_spell_request.set_next(self._def_request)
        self._def_request.set_next(self._training_handler)
        self._training_handler.set_next(self._size_request)
        self._size_request.set_next(self._mem_request)
        self._mem_request.set_next(self._test_handler)
        self._test_handler.set_next(self._help_request)
        self._help_request.set_next(self._unk)

    def _build_handlers(self):
        self._entry_handler = EntryHandler(self._model, self._view)
        self._end_handler = EndRequestHandler(self._model,self._view)
        self._def_request = DefineRequestHandler(self._model, self._view)
        self._spell_request = SpellRequestHandler(self._model, self._view)
        self._possible_spell_request = PossibleSpellRequestHandler(self._model,self._view)
        self._training_handler = TrainingRequestHandler(self._model,self._view)
        self._size_request = SizeRequestHandler(self._model,self._view)
        self._mem_request = MemRequestHandler(self._model, self._view)
        self._help_request = HelpRequestHandler(self._model, self._view)
        self._consumption_handler = ConsumptionHandler(self._model,self._view)
        self._test_handler = TestRequestHandler(self._model,self._view)
        self._unk = UnkownHandler()

    def handle_request(self,request):
        return self._entry_handler.handle(request)






