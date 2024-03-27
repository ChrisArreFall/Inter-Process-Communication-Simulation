import sys
from ProcessWindow import ProcessWindow
from Mailbox import Mailbox
from Process import Process
from MailboxWindow import MailboxWindow
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton
import globals

globals.init()

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.process_windows = []
        self.mailbox_window = None
        self.init_UI()

    def init_UI(self):
        layout = QVBoxLayout()

        # Number of Processes
        hbox_processes = QHBoxLayout()
        lbl_processes = QLabel('Amount of Process:')
        self.num_processes = QLineEdit()
        hbox_processes.addWidget(lbl_processes)
        hbox_processes.addWidget(self.num_processes)
        layout.addLayout(hbox_processes)

        # Type of Synchronization
        hbox_sync = QHBoxLayout()
        lbl_sync = QLabel('Type of Synchronization:')
        self.sync_type = QComboBox()
        self.sync_type.addItems(['Blocking send with Blocking receive', 
                                 'Non-Blocking send with blocking receive', 
                                 'Non-blocking send with non blocking receive'])
        hbox_sync.addWidget(lbl_sync)
        hbox_sync.addWidget(self.sync_type)
        layout.addLayout(hbox_sync)

        # Type of Addressing
        hbox_addr = QHBoxLayout()
        lbl_addr = QLabel('Type of Addressing:')
        self.addr_type = QComboBox()
        self.addr_type.addItems(['Direct Send, Direct Receive explicit', 
                                 'Direct Send, Direct Receive implicit', 
                                 'Indirect Static',
                                 'Indirect Dynamic'])
        hbox_addr.addWidget(lbl_addr)
        hbox_addr.addWidget(self.addr_type)
        layout.addLayout(hbox_addr)

        # Message Format
        hbox_msgfmt = QHBoxLayout()
        lbl_msgfmt = QLabel('Message Format:')
        self.msgfmt_type = QComboBox()
        self.msgfmt_type.addItems(['Fixed length', 
                                   'Variable Length',
                                   'File link'])
        hbox_msgfmt.addWidget(lbl_msgfmt)
        hbox_msgfmt.addWidget(self.msgfmt_type)
        layout.addLayout(hbox_msgfmt)

        # Type of Queue
        hbox_queue = QHBoxLayout()
        lbl_queue = QLabel('Type of Queue:')
        self.queue_type = QComboBox()
        self.queue_type.addItems(['FIFO', 'Priority'])
        hbox_queue.addWidget(lbl_queue)
        hbox_queue.addWidget(self.queue_type)
        layout.addLayout(hbox_queue)

        # Start Button
        self.start_btn = QPushButton('Start')
        self.start_btn.clicked.connect(self.start_simulation)
        layout.addWidget(self.start_btn)

        self.setLayout(layout)
        self.setWindowTitle('IPC Simulation')

    def start_simulation(self):
        #try:
        # Obtain parameters
        globals.num_processes = int(self.num_processes.text())

        match self.sync_type.currentIndex():
            case 0:
                sync_type = "blksnd_blkrcv"
            case 1:
                sync_type = "nblksnd_blkrcv"
            case 2:
                sync_type = "nblksnd_nblkrcv"
        
        match self.addr_type.currentIndex():
            case 0:
                addr_type = "dirsnd_dirrcvexp"
            case 1:
                addr_type = "dirsnd_dirrcvimp"
            case 2:
                addr_type = "ind_sta"
            case 3:
                addr_type = "ind_dyn"
        
        match self.msgfmt_type.currentIndex():
            case 0:
                msgfmt_type = "fix_len"
            case 1:
                msgfmt_type = "var_len"
            case 2:
                msgfmt_type = "file_link"
        print(addr_type)
        print(f"Number of processes: {globals.num_processes}")
        # We only need the mailbox for the indirect messages
        if addr_type == "ind_sta" or addr_type == "ind_dyn":
            # Assign value to global variable
            globals.mailbox = Mailbox(self.queue_type.currentText(), addr_type)
            self.mailbox_window = MailboxWindow()
            self.mailbox_window.show()

        for i in range(globals.num_processes):
            process = Process(i, addr_type, self.queue_type.currentText())
            # Add process to global variable
            globals.process_list.append(process)
            process_window = ProcessWindow(i)
            process_window.show()
            self.process_windows.append(process_window)
        #except ValueError:
        #    print("Error: Number of processes needs to be a number.")   
        pass
    #Override close event
    def closeEvent(self, event):
        # Close mailbox window
        if self.mailbox_window:
            self.mailbox_window.close()
        # Close all process windows
        for process_window in self.process_windows:
            process_window.close()
        event.accept()

def main():
    # Here we call the main window, we need to add an option
    # for the non-GUI version.
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
