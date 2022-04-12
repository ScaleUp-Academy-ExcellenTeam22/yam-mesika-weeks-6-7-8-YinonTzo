from typing import Generator
import message


class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_title, message_body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_title (str): The title of the message.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            >>> po_box = PostOffice(['a', 'b'])
            >>> message_id = po_box.send_message('a', 'b', 'Hello!')
            >>> len(po_box.boxes['b'])
            1
            >>> message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = message.Message(self.message_id, message_title, message_body, sender)

        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user_name: str, num_of_msg: int = None) -> Generator:
        """
        Read messages from user inbox.
        :param user_name: The user inbox wanted.
        :param num_of_msg: Num of messages wanted.
        :return: Generator that contains num of unread messages
        """
        if not num_of_msg:
            num_of_msg = len(self.boxes[user_name])

        count = 0
        for msg in self.boxes[user_name]:
            if count >= num_of_msg:
                break

            if not msg.read:
                msg.read = True
                count += 1
                yield msg

    def search_inbox(self, user_name: str, substring: str) -> list:
        """
        :param user_name: User inbox wanted.
        :param substring: Substring message wanted.
        :return: List that contains messages containing substring.
        """
        return [msg
                for msg in self.boxes[user_name]
                if substring in msg.title or substring in msg.body]


if __name__ == '__main__':
    po_box = PostOffice(['a', 'b'])
    po_box.send_message('a', 'b', 'Check', 'Hello!')
    po_box.send_message('a', 'b', 'Check', 'world')
    po_box.send_message('a', 'b', 'Check', 'from')
    po_box.send_message('a', 'b', 'Check', 'Yinon')
    po_box.send_message('a', 'b', 'Check', 'Tzomi!')

    messages1 = po_box.read_inbox('b')
    for msg1 in messages1:
        print(msg1)

    messages2 = po_box.read_inbox('b', 3)
    for msg1 in messages2:
        print(msg1)

    find_messages1 = po_box.search_inbox('b', 'Tz')
    print(find_messages1)

    find_messages2 = po_box.search_inbox('b', 'Ch')
    print(find_messages2)
