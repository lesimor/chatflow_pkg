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

    def rZgGg(self, payload):
        return self.states.get('jmzPh')

    def jmzPh(self, payload):
        return self.states.get('FBTmI')

    def FBTmI(self, payload):
        return self.states.get('Xr2Hm')

    def Xr2Hm(self, payload):
        return self.states.get('uzZvh')

    def uzZvh(self, payload):
        return self.states.get('rZgGg')

def main():
    file_name = 'state.json'
    file_path = os.path.join(abs_path, file_name)

    with open(file_path, 'r') as f:
        json_dict = json.load(f)

    cf = ChatFlow(json_dict, CustomTransition)

    msg = None
    current_state_id = cf.entry_state.id

    while msg != 'q':
        msg = input("User: ")
        next_state = cf.run(current_state_id, {'message': msg})  # current state를 임의로 entry로 설정

        print(next_state.__dict__)

        current_state_id = next_state.id

if __name__ == '__main__':
    main()