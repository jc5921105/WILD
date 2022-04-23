from __future__ import print_function
import pdb, os

class Test:
    def __init__(self,tests_location):
        self.loc = tests_location
        self._file_model = []
        self._get_files()
        pdb.set_trace()

    def _get_files(self):
        for x in os.listdir(self.loc):
            if '.json' in x: self._file_model.append(x)
        self._file_model.sort()




if __name__ == '__main__':
    app = Test('/workspace/dev/test_env/WILD/smith/tests/set1')