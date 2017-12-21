from chatflow.chatflow_base import ChatFlowBase


class Kakao(ChatFlowBase):
    def __init__(self, dev_id, conv_id):
        ChatFlowBase.__init__(self, dev_id, conv_id)

