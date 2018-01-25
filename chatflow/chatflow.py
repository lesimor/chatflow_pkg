import json
import random

from .states import State


class ChatFlow(object):
    def __init__(self, path):
        """ __init__ method."""
        with open(path, 'r') as f:
            json_dict = json.load(f)

        # TODO: state의 인스턴스화
        self.states = json_dict.get('states')
        self.meta = json_dict.get('meta')
        self._check_ingredients()

    @property
    def entry_id(self):
        return self.meta.get('entry')

    @property
    def exception_id(self):
        return self.meta.get('exception')

    @property
    def entry_state(self):
        entry_id = self.entry_id
        return self.states[entry_id]

    @property
    def exception_state(self):
        exception_id = self.exception_id
        return self.states[exception_id]

    def _check_ingredients(self):
        """ test method.
        Check necessary ingredients
        entry_id and exception_id are required.
        """
        if self.entry_id is None:
            raise Exception("Meta entry ID not in state")

        if self.exception_id is None:
            raise Exception("Meta exception ID not in state")

    def get_state_by_id(self, state_id):
        """
        get state by id

        * Args:
            - state_id: Reference id

        * Return:
            - state
        """
        state = self.states.get(state_id)
        if state  is None:
            print("State not exists with id {}. Return exception".format(state_id))
            return self.exception_state
        return state

    def get_state(self, state_id):
        """
        transition method.
        get state by id

        Args:
            - state_id: Key id

        Return:
            - state
        """
        state = self.get_state_by_id(state_id)
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
        current_state = self.get_state_by_id(current_state_id)

        # TODO: current_state -> next_state 분기 로직 삽입
        next_state_id = random.choice(list(self.states.keys()))

        # TODO: state 내부에 적당한 값을 slot에 삽입하여 language generate
        next_state = self.get_state(next_state_id)

        return next_state