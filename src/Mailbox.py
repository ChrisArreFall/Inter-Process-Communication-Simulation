"""
Esto le faltaria un atributo para limitar la lista de mensajes para
cada processo a un numero definido al inicio en conjunto con el
numero de procesos.
"""
import Message
class Mailbox:
    def __init__(self, processes_count, queue_type="FIFO"):
        if not isinstance(processes_count, int):
            print("Error: processes_count must be an integer.")
            return None
        self.processes_count = processes_count if processes_count > 0 else 1
        self.queue_type = queue_type if isinstance(queue_type, str) else "FIFO"
        self.messages = [[] for _ in range(processes_count)]
    """
    This is for the inirect send option
    for now this is only 1 to 1
    """
    def send(self, process_index, message):
        if not isinstance(message, Message):
            print("Error: The message must be an instance of the Message class.")
            return None
        if 0 <= process_index < self.processes_count:
            self.messages[process_index].append(message)
            # This is for the priority option as we always
            # want them to be organized by priority
            if self.queue_type == "Priority":
                self.messages[process_index].sort(key=lambda msg: msg.priority, reverse=True)
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
        if 0 <= process_index < self.processes_count and self.messages[process_index]:
            # Here we use pop(0) as this works for both priority
            # and FIFO thanks to previously organizing the list
            # in a accending order in both cases we grab the
            # last element of the list and remove it.
            return self.messages[process_index].pop(0)
        else:
            return None
