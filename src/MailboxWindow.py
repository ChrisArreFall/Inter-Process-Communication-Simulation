
from PyQt5.QtWidgets import QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton

class MailboxWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # All Messages
        lbl_messages = QLabel('Messages:')
        self.messages_text = QTextEdit()
        self.messages_text.setReadOnly(True)
        layout.addWidget(lbl_messages)
        layout.addWidget(self.messages_text)

        self.setLayout(layout)
        self.setWindowTitle('Mailbox')

