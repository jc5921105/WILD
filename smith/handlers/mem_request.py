from __future__ import print_function
from smith.handlers.handler import Handler
import pdb, re, sys, os


REGEX = re.compile(r"""^.*words.*know.*""",re.IGNORECASE)


class MemRequestHandler(Handler):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def handle(self, request):
        request = request.lower()
        if REGEX.match(request):
            self._view.s_print('\n\nThe Agency Currently Knows %s Words\n\n' % len(self._model.full_model.keys()))
        else:
            return super(MemRequestHandler,self).handle(request)

    def get_sloc(self):
        pth = os.path.join(os.getcwd(),'smith')
        if os.path.isdir(pth):
            tmp = self.get_count(pth)
            self._view.s_print('\n\nCurrent SLOC Count is %s\n\n' % tmp)


