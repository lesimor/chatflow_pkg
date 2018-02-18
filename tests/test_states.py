import unittest

from chatflow.state import State

class TestStates(unittest.TestCase):
    def test_state(self):
        json_dict = {
            "name": "테스트 노드",
            "message": "테스트 노드입니다."
        }
        state = State('test_id', **json_dict)
        self.assertEqual(state.id, "test_id")
        self.assertEqual(state.name, "테스트 노드")
        self.assertEqual(state.message, "테스트 노드입니다.")