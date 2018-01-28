
class State():

    def __init__(self, id, name, message):
        self.__id = id
        self.__name = name
        self.__message = message

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
    def message(self, message):
        self.__message = message