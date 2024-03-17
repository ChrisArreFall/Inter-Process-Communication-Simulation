from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

def say_hello():
    label.setText("Hello, World!")

app = QApplication([])

window = QWidget()
window.setWindowTitle("Inter Process Comunication Simulation")

layout = QVBoxLayout()

label = QLabel("Click the button to say hello")
layout.addWidget(label)

button = QPushButton("Say Hello")
button.clicked.connect(say_hello)
layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec_()
