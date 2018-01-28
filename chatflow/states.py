
class State():

    def __init__(self, id, name, message):
        self.__id = id
        self.__name = name
        self.message = message

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
