from chatflow import ChatFlow

cf = ChatFlow('./state.json')

def main():
    msg = None

    while msg != 'q':
        msg = input("사용자: ")
        next_state = cf.run(cf.entry_id, msg)  # current state를 임의로 entry로 설정

        print("Bot: {}".format(next_state.get('message')))

if __name__ == '__main__':
    main()