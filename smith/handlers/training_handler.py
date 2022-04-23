from __future__ import print_function
from smith.handlers.handler import Handler
import pdb, re, sys


REGEX = re.compile(r"""^.*train.*yourself.*""",re.IGNORECASE)


class TrainingRequestHandler(Handler):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def handle(self, request):
        request = request.lower()
        if REGEX.match(request):
              self._train()
              return True
        else:
            return super(TrainingRequestHandler,self).handle(request)

    def _train(self):
        self._model.self_define()
        self._model.self_analyze()
        self._model.self_weight()
        self._model.write_memory()

