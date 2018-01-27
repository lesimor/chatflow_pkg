import sys
import os

sys.path.append(os.getcwd())
abs_path = os.path.dirname(os.path.abspath(__file__))

from chatflow import ChatFlow

file_name = 'state.json'
cf = ChatFlow(os.path.join(abs_path, file_name))


def main():
    msg = None

    while msg != 'q':
        msg = input("User: ")
        next_state = cf.run(cf.entry_id, msg)  # current state를 임의로 entry로 설정

        print("System: {}".format(next_state.get('message')))

if __name__ == '__main__':
    main()