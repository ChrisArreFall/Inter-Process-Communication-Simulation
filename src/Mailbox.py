"""
Esto le faltaria un atributo para limitar la lista de mensajes para
cada processo a un numero definido al inicio en conjunto con el
numero de procesos.
"""
from Message import Message
import globals


class Mailbox:
    def __init__(self, queue_type="FIFO", addr_type="ind_sta"):
        self.queue_type = queue_type if isinstance(queue_type, str) else "FIFO"
        self.addr_type = addr_type
        self.messages = [[] for _ in range(globals.num_processes)]
    """
    This is for the inirect send option
    for now this is only 1 to 1
    """
    def send(self, sender, recipient, message):
        if not isinstance(message, Message):
            msg = Message(sender=sender, recipient=recipient, message=message)
            message = msg
        if 0 <= recipient < globals.num_processes:
            self.messages[recipient].append(message)
            # This is for the priority option as we always
            # want them to be organized by priority
            if self.queue_type == "Priority":
                self.messages[recipient].sort(key=lambda msg: msg.priority, reverse=True)
        else:
            print("Invalid process index.")
    """
    This is for the indirect receive option
    for now this is only 1 to 1
    """
    def receive(self, process_index):
        if not isinstance(process_index, int):
            print("Error: process_index must be an integer.")
            return None
        if 0 <= process_index < globals.num_processes and self.messages[process_index]:
            # Here we use pop(0) as this works for both priority
            # and FIFO thanks to previously organizing the list
            # in a accending order in both cases we grab the
            # last element of the list and remove it.
            return self.messages[process_index].pop(0)
        else:
            return None
