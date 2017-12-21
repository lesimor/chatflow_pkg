from chatflow.chatflow_base import ChatFlowBase


class Kakao(ChatFlowBase):
    def __init__(self, dev_id, conv_id):
        ChatFlowBase.__init__(self, dev_id, conv_id)
        self.template = {
            "message": {
                "text": "",
                "photo": None,
                "message_button": None
            },
            "keyboard": {
                "type": "text",
                "buttons": None
            }
        }

    def response(self, user_key, message):
        r = self.post(user_key, message)

        bot_message = r['message']['text']
        bot_image_url = r['message']['image']

        is_button = r['keyboard']['type'] == 'buttons'

        return {
            "message": {
                "text": bot_message,
                "photo": None,
                "message_button": None
            },
            "keyboard": None if r['keyboard']['type'] == 'text'
                        else {"type": "buttons", "buttons": r['keyboard']['buttons']}
        }
