from smith.handlers.handler import Handler


class UnkownHandler(Handler):
    def __init__(self):
        pass

    def handle(self, request):
        print('Unknown Request: %s' % request)
        return True