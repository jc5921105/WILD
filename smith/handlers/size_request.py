from __future__ import print_function
from smith.handlers.handler import Handler
import pdb, re, sys, os


#REGEX = re.compile(r"""^.*train.*yourself.*""",re.IGNORECASE)


class SizeRequestHandler(Handler):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def handle(self, request):
        request = request.lower()
        if request == 'size':
            self.get_sloc()
        else:
            return super(SizeRequestHandler,self).handle(request)

    def get_sloc(self):
        pth = os.path.join(os.getcwd(),'smith')
        if os.path.isdir(pth):
            tmp = self.get_count(pth)
            self._view.s_print('\n\nCurrent SLOC Count is %s\n\n' % tmp)

    def get_count(self,path):
        count = 0
        for x in os.listdir(path):
            if os.path.isfile(os.path.join(path,x)):
                if os.path.join(path,x).endswith('.py'):
                    with open(os.path.join(path,x),'r') as fobj:
                        data = fobj.readlines()
                    count = count + len(data)
            elif os.path.isdir(os.path.join(path,x)):
                count = count + self.get_count(os.path.join(path,x))
            else:
                raise StandardError
        return count
