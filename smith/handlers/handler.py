class Handler(object):
    def __init__(self):
        self._next_handler = None

    def handle(self,msg_obj):
        self._next_handler.handle(msg_obj)

    def set_next(self,handler):
        self._next_handler = handler

