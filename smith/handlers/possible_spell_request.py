from __future__ import print_function
from smith.handlers.handler import Handler
from smith.capabilities.search import search, straight_search, vague_search, vague_search_large
import pdb, re


REGEX = re.compile(r"""^.*possible\s+spelling.*\s+(.*\s+)?(?P<word>\S+)\s*.*""",re.IGNORECASE)


class PossibleSpellRequestHandler(Handler):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def handle(self, request):
        if 'spell' in request:
            t = REGEX.match(request)
            if t:
                word = t.group('word')
                self._view.print_possible_spellings(vague_search_large(word,self._model.full_dict),word)
                return True
            else:
                return super(PossibleSpellRequestHandler, self).handle(request)
        else:
            return super(PossibleSpellRequestHandler,self).handle(request)