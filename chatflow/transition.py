from .state_json_loader import StateJsonLoader
from .state import State

class Transition(object):
    def __init__(self, json_dict):

        self.states = {}
        states_from_json_dict = json_dict.get(StateJsonLoader.STATES, {})
        for key, state in states_from_json_dict.items():
            self.states.setdefault(key, State(key, state))
