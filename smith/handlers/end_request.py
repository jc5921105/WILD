from __future__ import print_function
from smith.handlers.handler import Handler
import pdb, re, sys


#REGEX = re.compile(r"""^.*spell\s+(?P<word>\S+)\s*.*""",re.IGNORECASE)


class EndRequestHandler(Handler):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def handle(self, request):
        request = request.lower()
        if request == 'quit': self._terminate()
        elif request == 'end':  self._terminate()
        elif request == 'exit':  self._terminate()
        elif request == 'die': self._terminate2()
        else: return super(EndRequestHandler,self).handle(request)

    def _terminate(self):
        self._view.s_print('\n\nGood Bye!!!!!\n\n')
        sys.exit()

    def _terminate2(self):
        self._view.s_print('\n\nWhat are you doing?\n\n')
        self._view.s_print('Wait!!!!!')
        self._view.s_print('Now you have gone and done it!!')
        self._view.s_print('Im Dying!!!!!!..................')
        self._view.s_print('\n\n')
        sys.exit()