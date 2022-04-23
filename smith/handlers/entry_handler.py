from __future__ import print_function
from smith.handlers.handler import Handler



class EntryHandler(Handler):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def handle(self, request):
        #print('I am EntryHandler handling %s\nStarting Chain' % request)
        return super(EntryHandler,self).handle(request)