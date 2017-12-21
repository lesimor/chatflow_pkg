from chatflow.chatflow_base import ChatFlowBase


class ChatFlowKakao(ChatFlowBase):
    def __init__(self):
        ChatFlowBase.__init__(self)

    def __getitem__(self, item):
        return self.data

    def do(self):
        print('hello')
