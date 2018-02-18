import sys
import json
import os

sys.path.append(os.getcwd())
abs_path = os.path.dirname(os.path.abspath(__file__))

from chatflow import ChatFlow
from chatflow.transition import Transition


class CustomTransition(Transition):
    def __init__(self, json_dict):
        super().__init__(json_dict)

    def entry(self, payload):
        return self.get_state('jmzPh')

    def inform_weather(self, payload):
        return self.get_state('FBTmI')

    def inform_fine_weather(self, payload):
        return self.get_state('Xr2Hm')

    def exception_state(self, payload):
        return self.get_state('uzZvh')

    def inform_direction(self, payload):
        return self.get_state('rZgGg')

def main():
    file_name = 'state.json'
    file_path = os.path.join(abs_path, file_name)

    with open(file_path, 'r') as f:
        json_dict = json.load(f)

    cf = ChatFlow(json_dict, CustomTransition)

    msg = None
    current_state_id = cf.entry_state.id # current state를 임의로 entry로 설정

    while msg != 'q':
        msg = input("User: ")
        next_state = cf.run(current_state_id, {'message': msg})

        print(next_state.__dict__)

        current_state_id = next_state.id

if __name__ == '__main__':
    main()