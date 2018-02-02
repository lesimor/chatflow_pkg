import json
import random

from .states import State

class ChatFlow(object):
    _states = {}

    def __init__(self, json_dict):
        """ __init__ method."""
        # TODO: state의 인스턴스화
        self.meta = json_dict.get('meta')
        self.set_states(json_dict.get('states'))
        self._check_meta()

    @classmethod
    def init_with_path(cls, path):
        with open(path, 'r') as f:
            json_dict = json.load(f)

        return cls(json_dict)

    @property
    def entry_id(self):
        return self.meta.get('entry')

    @property
    def exception_id(self):
        return self.meta.get('exception')

    @property
    def entry_state(self):
        entry_id = self.entry_id
        return self._states[entry_id]

    @property
    def exception_state(self):
        exception_id = self.exception_id
        return self._states[exception_id]

    def set_states(self, states):
        for id, state in states.items():
            self._states[id] = State(id, **state)

    def _check_meta(self):
        """ test method.
        Check necessary ingredients
        entry_id and exception_id are required.
        """
        if self.entry_id is None:
            raise Exception("Meta entry ID not in state")

        if self.exception_id is None:
            raise Exception("Meta exception ID not in state")

    def get_state(self, state_id):
        """
        transition method.
        get state by id

        Args:
            - state_id: Key id

        Return:
            - state
        """
        state = self._states.get(state_id)
        if state is None:
            print("State not exists with id {}. Return exception".format(state_id))
            return self.exception_state

        return state

    def run(self, current_state_id, message):
        """

        Args:
            - current_state_id: Reference id
            - message: Reference message

        Return:
            - next_state
        """
        next_state = None
        current_state = self.get_state(current_state_id)

        # TODO: current_state -> next_state 분기 로직 삽입
        next_state_id = random.choice(list(self._states.keys()))

        # TODO: state 내부에 적당한 값을 slot에 삽입하여 language generate
        next_state = self.get_state(next_state_id)

        return next_state