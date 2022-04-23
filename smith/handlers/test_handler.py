from __future__ import print_function
from smith.handlers.handler import Handler
from smith.capabilities.search import search, straight_search
from smith.tests.test import Test
import pdb, re, os, datetime


REGEX = re.compile(r"""^.*test\s+yourself.*""",re.IGNORECASE)
TEST_SETS = ['set1','set2','set3']
TEST_SET_INDEX = 0

class TestRequestHandler(Handler):
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._get_location()

    def handle(self, request):
        t = REGEX.match(request)
        if t:
            tmp = self._create_results_location()
            self.t1 = Test(os.path.join(self._location,TEST_SETS[TEST_SET_INDEX]),self._model, self._view, tmp)
            self.t1.test()
            self.t1.print_accuracy()

            return True
        else:
            return super(TestRequestHandler, self).handle(request)


    def _get_location(self):
        self._location = os.path.join(os.getcwd(),'smith','tests')

    def _get_timestamp(self):
        dto = datetime.datetime.now()
        return dto.strftime("%y%m%d.%H%M.%S")

    def _create_results_location(self):
        tmp = os.path.join(self._location,'results',self._get_timestamp())
        if not os.path.isdir(tmp): os.mkdir(tmp,0o777)
        return tmp


