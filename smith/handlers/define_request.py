from __future__ import print_function
from smith.handlers.handler import Handler
import pdb, re

REGEX = re.compile(r"""^.*define\s+(?P<word>\S+)\s*.*""",re.IGNORECASE)

class DefineRequestHandler(Handler):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def handle(self, request):
        if 'define' in request.lower():
            t = REGEX.match(request)
            if t:
                word = t.group('word')
                if word in self._model.full_dict.keys():
                    if len(self._model.full_dict[word]['definitions']) == 0:
                        self._view.s_print("I know the word \"%s\",\nbut I don\'t have any definitions for the word." % t.group('word'))
                        return True
                    else:
                        self._view.print_entity(self._model.full_dict[word])
                        return True
                else:
                    self._view.s_print("I don't know the definition of the word: %s " % t.group('word'))
                    return True
            else: return super(DefineRequestHandler,self).handle(request)
        else: return super(DefineRequestHandler,self).handle(request)

    def _define(self):
        pass

    def _parse_request(self,request):
        pass
