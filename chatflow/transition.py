class Transition(object):
    def __init__(self, cf_instance):
        self.chat_flow = cf_instance

    def get_state(self, id):
        return self.chat_flow.get_state(id)
