class ChatFlowBase(object):
    def __init__(self):
        self.data = {}
        pass

    def __getitem__(self, item):
        raise NotImplementedError
