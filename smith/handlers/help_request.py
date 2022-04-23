from __future__ import print_function
from smith.handlers.handler import Handler
import pdb, re, sys, os


#REGEX = re.compile(r"""^.*train.*yourself.*""",re.IGNORECASE)


class HelpRequestHandler(Handler):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def handle(self, request):
        request = request.lower()
        if request == 'help':
            self._view.s_print('\tYou can ask me to spell something. EX: \"Smith, how do I spell <word>\"')
            self._view.s_print('\tYou can ask me the possible spellings of a word. EX: \"Smith, what are the possible spellings of <word>\"')
            self._view.s_print('\tYou can ask me to define something. EX: \"Smith, difine <word>')
            self._view.s_print('\tYou can ask me how many words I know. EX: \"Smith, how many words do you know\"')
            self._view.s_print('\tYou can ask me the size of my code. EX: \"size\"')
            self._view.s_print('\tYou can ask me to train myself. EX: \"Smith, train yourself\"')
            self._view.s_print('\tYou can ask me to consume a text file for use in calculating word frequency: EX:\"Smith, consume <file_location>\"')
            self._view.s_print('\tYou can ask me to test myself. EX:\"test yourself\"')
            self._view.s_print('\tYou can also end me. EX: \"end|exit|quit|die\"')
        else:
            return super(HelpRequestHandler,self).handle(request)

