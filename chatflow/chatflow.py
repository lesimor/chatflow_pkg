import json
import random


class ChatFlow(object):
    def __init__(self, path):

        with open(path, 'r') as f:
            json_dict = json.load(f)

        # TODO: state의 인스턴스화
        self.states = json_dict.get('states')
        self.meta = json_dict.get('meta')

        self.test()

    def entry_id(self):
        return self.meta.get('entry')

    def exception_id(self):
        return self.meta.get('exception')

    def get_state_by_id(self, state_id):
        state = self.states.get(state_id)

        if state is None:
            raise Exception("State not exists with id {}".format(state_id))

        return state

    def transition(self, state_id):
        state = self.get_state_by_id(state_id)

        if state is None:
            entry_id = self.entry_id()
            return self.states.get(entry_id)
        else:
            return state

    def test(self):
        # entry state existence check.
        if self.entry_id() not in self.states.keys():
            raise Exception("Meta entry ID not in state")

        # exception existence check.
        if self.exception_id() not in self.states.keys():
            raise Exception("Meta exception ID not in state")

    def run(self, current_state_id, message):
        current_state = self.get_state_by_id(current_state_id)

        # TODO: current_state -> next_state 분기 로직 삽입
        next_state_id = random.choice(list(self.states.keys()))

        # TODO: state 내부에 적당한 값을 slot에 삽입하여 language generate

        return self.transition(next_state_id)


if __name__ == '__main__':

    cf = ChatFlow('./state.json')
    msg = None

    while msg != 'q':
        msg = input("사용자: ")
        next_state = cf.run(cf.entry_id(), msg)  # current state를 임의로 entry로 설정

        print("Bot: {}".format(next_state.get('message')))



