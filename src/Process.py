
import threading
from Message import Message
import globals

class Process:
    def __init__(self, process_id, addr_type, queue_type):
        if not isinstance(process_id, int):
            print("Error: process_id must be an integer.")
            return None
        self.process_id = process_id if isinstance(queue_type, int) else 0
        self.log = []      # List of received messages
        self.sent = []     # List of sent messages
        self.inbox = []    # Inbox for received messages
        self.addr_type = addr_type if isinstance(addr_type, str) else "ind_sta" # Addressing type
        self.queue_type = queue_type if isinstance(queue_type, str) else "FIFO" # Queue type
        self.lock = threading.Lock()
    """
    This is for both Direct send options
    """
    def send_message(self, recipient, message):
        if not isinstance(message, Message):
            msg = Message(self.process_id, recipient=recipient, message=message)
            message = msg
        if not isinstance(recipient, Process):
            print("Error: recipient must be an instance of Process.")
            return
        self.sent.append(message)  # Store the sent message
        globals.process_list[recipient].receive_message(message)
    # This function is more for secutiry purposes 
    # as it is not recommended to directly access the
    # inbox of another process
    def receive_message(self, message):
        if not isinstance(message, Message):
            print("Error: message must be an instance of Message.")
            return
        with self.lock:
            self.inbox.append(message)
    '''
    This is for the Direct send, Direct Receive Explicit option
    '''
    def receive_from(self, sender_id):
        if not isinstance(sender_id, int):
            print("Error: sender_id must be an integer.")
            return None
        with self.lock:
            for message in self.inbox:
                if message.sender == sender_id:
                    self.inbox.remove(message)
                    self.log.append(message)  # Log the received message
                    return message
            return None
    '''
    This is for the Direct send, Direct Receive Implicit option
    '''
    def receive_any(self):
        with self.lock:
            if self.inbox:
                message = self.inbox.pop(0)
                self.log.append(message)  # Log the received message
                return message
            return None
