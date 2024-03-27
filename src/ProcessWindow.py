from PyQt5.QtWidgets import QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton
from Process import Process
from PyQt5 import QtCore
import globals


class ProcessWindow(QWidget):
    def __init__(self, process_id):
        super().__init__()
        self.process_id = process_id if isinstance(process_id, int) else 0
        self.init_UI()
        self.init_timer()

    def init_UI(self):
        layout = QVBoxLayout()

        # Inbox
        lbl_inbox = QLabel('Inbox:')
        self.inbox_text = QTextEdit()
        self.inbox_text.setReadOnly(True)
        layout.addWidget(lbl_inbox)
        layout.addWidget(self.inbox_text)

        # Sent Messages
        lbl_sent = QLabel('Sent Messages:')
        self.sent_text = QTextEdit()
        self.sent_text.setReadOnly(True)
        layout.addWidget(lbl_sent)
        layout.addWidget(self.sent_text)

        # "To:"
        hbox_to = QHBoxLayout()
        lbl_to = QLabel('To:')
        self.recipient_dropdown = QComboBox()
        # dropdown
        for i in range(globals.num_processes):
            if i != self.process_id:
                self.recipient_dropdown.addItem(str(i))
        hbox_to.addWidget(lbl_to)
        hbox_to.addWidget(self.recipient_dropdown)
        layout.addLayout(hbox_to)

        # "Message:"
        hbox_message = QHBoxLayout()
        lbl_message = QLabel('Message:')
        self.message_input = QLineEdit()
        hbox_message.addWidget(lbl_message)
        hbox_message.addWidget(self.message_input)
        layout.addLayout(hbox_message)

        # "Priority:"
        hbox_priority = QHBoxLayout()
        lbl_priority = QLabel('Priority:')
        self.priority_input = QLineEdit()
        hbox_priority.addWidget(lbl_priority)
        hbox_priority.addWidget(self.priority_input)
        layout.addLayout(hbox_priority)

        # Send Button
        self.send_btn = QPushButton('Send')
        self.send_btn.clicked.connect(self.send_message)
        layout.addWidget(self.send_btn)


        self.setLayout(layout)
        self.setWindowTitle(f'Process {self.process_id}')

    def send_message(self):
        # This means mailbox was not created which means
        # this is one of the direct message types
        if globals.mailbox == None:
            globals.process_list[self.process_id].send_message(int(self.recipient_dropdown.currentText()), self.message_input.text())
        else:
            globals.mailbox.send(self.process_id, int(self.recipient_dropdown.currentText()), self.message_input.text())
        pass

    def init_timer(self):
        # Set up a timer to call the update_messages function periodically
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(500)  # Update every 1 second

    def update_messages(self):
        # Clears the current messages
        self.inbox_text.clear()
        # Iterates through all messages in the mailbox and displays them
        for process_messages in globals.mailbox.messages:
            for message in process_messages:
                self.inbox_text.append(f"From {message.sender} to {message.recipient}: {message.message}")
