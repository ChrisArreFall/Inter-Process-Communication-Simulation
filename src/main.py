import sys
from ProcessWindow import ProcessWindow
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.num_processes = 0
        self.process_windows = []
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
        self.sync_type.addItems(['Blocking send with Blocking receive', 'Non-Blocking send with blocking receive', 'Non-blocking send with non blocking receive'])
        hbox_sync.addWidget(lbl_sync)
        hbox_sync.addWidget(self.sync_type)
        layout.addLayout(hbox_sync)

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
        try:
            num_processes = int(self.num_processes.text())
            print(f"Number of processes: {num_processes}")
            for i in range(num_processes):
                process_window = ProcessWindow(process_id=i, num_processes=num_processes)
                process_window.show()
                self.process_windows.append(process_window)
        except ValueError:
            print("Error: Number of processes needs to be a number.")   
        pass
    #Over ride close event
    def closeEvent(self, event):
        # Close all process windows
        for process_window in self.process_windows:
            process_window.close()
        event.accept()

def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
