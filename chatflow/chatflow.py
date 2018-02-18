import json

from .state import State
from .state_json_loader import StateJsonLoader


class ChatFlow(object):

    def __init__(self, json_dict, transition_cls):
        """ __init__ method."""
        StateJsonLoader.check_ingredients(json_dict)

        self.meta = json_dict.get(StateJsonLoader.META)

        self.states = {}
        states_from_json_dict = json_dict.get(StateJsonLoader.STATES, {})
        for key, state in states_from_json_dict.items():
            self.states.setdefault(key, State(key, state))

        self.transition = transition_cls(self)

    @classmethod
    def init_with_path(cls, path, transition_cls):
        with open(path, 'r') as f:
            json_dict = json.load(f)

        return cls(json_dict, transition_cls)

    @property
    def entry_state(self):
        entry_id = self.meta.get(StateJsonLoader.ENTRY_ID)
        return self.states.get(entry_id)

    @property
    def exception_state(self):
        exception_id = self.meta.get(StateJsonLoader.EXCEPTION_ID)
        return self.states.get(exception_id)

    def get_state(self, state_id):
        """
        getting state method.
        get state by id

        Args:
            - state_id: Key id

        Return:
            - state
        """
        state = self.states.get(state_id)
        if state is None:
            print("State not exists with id {}. Return exception".format(state_id))
            return self.exception_state

        return state

    def run(self, current_state_id, payload={}):
        """

        Args:
            - current_state_id: Reference id
            - message: Reference message

        Return:
            - next_state
        """
        current_state = self.get_state(current_state_id)

        func = getattr(self.transition, current_state.transition)

        next_state = func(payload)

        return next_state
