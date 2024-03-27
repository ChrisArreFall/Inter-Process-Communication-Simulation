
from PyQt5.QtWidgets import QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton
from PyQt5 import QtCore
from Mailbox import Mailbox
import globals

class MailboxWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.init_timer()

    def init_UI(self):
        layout = QVBoxLayout()

        # All Messages
        lbl_messages = QLabel('Messages:')
        self.messages_text = QTextEdit()
        self.messages_text.setReadOnly(True)
        layout.addWidget(lbl_messages)
        layout.addWidget(self.messages_text)

        self.setLayout(layout)
        self.setWindowTitle('Mailbox')

    def init_timer(self):
        # Set up a timer to call the update_messages function periodically
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(500)  # Update every 1 second

    def update_messages(self):
        # Clears the current messages
        self.messages_text.clear()
        # Iterates through all messages in the mailbox and displays them
        for process_messages in globals.mailbox.messages:
            for message in process_messages:
                self.messages_text.append(f"From {message.sender} to {message.recipient}: {message.message}")

