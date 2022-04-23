from __future__ import print_function
from smith.handlers.handler import Handler
import pdb, re, sys, os
from smith.capabilities.consume import consume


REGEX = re.compile(r"""^.*consume.*\s(?P<text>\S+).*""",re.X)


class ConsumptionHandler(Handler):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def handle(self, request):
        tmp = REGEX.match(request)
        if tmp:
            retval, msg_mdl = consume(self._model.full_model,tmp.group('text'))
            if not retval: self._view.s_print(msg_mdl)
            else:
                self._model.full_model = msg_mdl
                self._model.write_memory()
        else:
            return super(ConsumptionHandler, self).handle(request)
