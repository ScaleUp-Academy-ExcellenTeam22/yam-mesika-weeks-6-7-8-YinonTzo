class Message:
    """
    A message class.
    Manage print functions.

    Args:
        message_id: Message Id.
        message_title: Message title.
        message_body: Message body.
        sender: Who sent the message.

    Attributes:
        Like args and read member which tell us if this message is already read.
    """

    def __init__(self, message_id: int, message_title: str, message_body: str, sender: str):
        self.id = message_id
        self.title = message_title
        self.body = message_body
        self.sender = sender
        self.read = False

    def __str__(self):
        """
        :return: Str with title, body and sender.
        """
        return f' Title: {self.title}' \
               f' Message: {self.body}' \
               f' From: {self.sender}'

    def __repr__(self):
        """
        :return: Str with title, body and sender.
        """
        return self.__str__()

