import globals
class Message:
    def __init__(self, sender=None, recipient=None, message="", priority=0, msg_fmt="var_len"):
        self.sender = sender if isinstance(sender, list) else []
        self.recipient = recipient if isinstance(recipient, list) else []
        self.message = message if isinstance(message, str) else ""
        self.priority = priority if isinstance(priority, int) else 0
        self.msg_fmt = msg_fmt if isinstance(msg_fmt, str) else "var_len"

    def get_sender(self):
        return self.sender

    def get_receiver(self):
        return self.recipient

    def get_message(self):
        return self.message

    def get_priority(self):
        return self.priority
