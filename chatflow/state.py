from .state_json_loader import StateJsonLoader


class State(object):

    def __init__(self, id, state_dict):
        self.__id = id
        self.__name = state_dict.get(StateJsonLoader.NAME, '')
        self.message = state_dict.get(StateJsonLoader.MESSAGE, {})

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, val):
        self.__message = val

