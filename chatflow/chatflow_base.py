import requests, json


class ChatFlowBase(object):
    def __init__(self, dev_id, conv_id):
        self.developer_id = dev_id
        self.conversation_id = conv_id

    def post(self, user_key, message):
        r = requests.post('http://chatflow.kr/api/v1/message',
                          data={'user_id': user_key,
                                'content': message,
                                'developer_id': self.developer_id,
                                'conversation_id': self.conversation_id})
        return json.loads(r.text)