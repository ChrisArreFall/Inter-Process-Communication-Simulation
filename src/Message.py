class Message:
    def __init__(self, sender=None, receiver=None, message="", priority=0):
        self.sender = sender if isinstance(sender, list) else []
        self.receiver = receiver if isinstance(receiver, list) else []
        self.message = message if isinstance(message, str) else ""
        self.priority = priority if isinstance(priority, int) else 0

    def get_sender(self):
        return self.sender

    def get_receiver(self):
        return self.receiver

    def get_message(self):
        return self.message

    def get_priority(self):
        return self.priority
