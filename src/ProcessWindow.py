from PyQt5.QtWidgets import QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton


class ProcessWindow(QWidget):
    def __init__(self, process_id,num_processes):
        super().__init__()
        self.process_id = process_id
        self.num_processes = num_processes
        self.init_UI()

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
        for i in range(self.num_processes):
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
        pass
