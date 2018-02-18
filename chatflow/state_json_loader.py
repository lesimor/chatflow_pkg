import os


class StateJsonLoader(object):
    STATES = 'states'
    ID = 'id'
    NAME = 'name'
    MESSAGE = 'message'

    META = 'meta'
    ENTRY_ID = 'entry_id'
    EXCEPTION_ID = 'exception_id'
    TRANSITION_MODULE_PATH = 'transition_module_path'

    @classmethod
    def check_ingredients(cls, json_dict):
        """
        test method.
        Check necessary ingredients
        entry_id and exception_id are required.
        """

        # State check
        states = json_dict.get('states', {})

        for key, state in states.items():
            if not key:
                raise Exception('ID cannot be empty')
            if not state.get(cls.NAME, ''):
                raise Exception('State name cannot be null')
            if not state.get(cls.MESSAGE, {}):
                raise Exception('State message cannot be null')

        # Meta check
        meta = json_dict.get(cls.META, {})
        entry_id = meta.get(cls.ENTRY_ID, '')
        exception_id = meta.get(cls.EXCEPTION_ID, '')

        if not entry_id:
            raise Exception("Meta entry ID is required")

        if entry_id not in states.keys():
            raise Exception("Meta entry ID is not valid")

        if not exception_id:
            raise Exception("Meta exception ID is required")

        if exception_id not in states.keys():
            raise Exception("Meta exception ID is not valid")

