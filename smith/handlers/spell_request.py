from __future__ import print_function
from smith.handlers.handler import Handler
from smith.capabilities.search import search, straight_search
import pdb, re


REGEX = re.compile(r"""^.*spell\s+(?P<word>\S+)\s*.*""",re.IGNORECASE)


class SpellRequestHandler(Handler):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def handle(self, request):
        if 'spell' in request:
            t = REGEX.match(request)
            if t:
                word = t.group('word')
                self._view.print_spelling_entity(search(word,self._model.full_dict))
                return True
            else:
                return super(SpellRequestHandler, self).handle(request)

        else:
            return super(SpellRequestHandler,self).handle(request)