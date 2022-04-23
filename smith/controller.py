import os, pdb
from smith.handlers.request_handler import RequestController as RC


class Controller:
    def __init__(self,model, view):
        self.model = model
        self.view = view
        self.rc = RC(self.model,self.view)

        self._introduce()
        self.run()

    def _introduce(self):
        self.view.introduction()

    def run(self):
        while True:
            tmp = self.view.prompt_user()
            self.rc.handle_request(tmp)


