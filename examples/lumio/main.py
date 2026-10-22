import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLabel, QComboBox, QSystemTrayIcon, QAction, QMenu
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Lumio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.agents = ["Claude Code", "Codex", "Cursor", "GitHub Copilot"]
        self.agent_commands = {
            "Claude Code": "echo 'Claude Code is running'",
            "Codex": "echo 'Codex is running'",
            "Cursor": "echo 'Cursor is running'",
            "GitHub Copilot": "echo 'GitHub Copilot is running'"
        }

    def initUI(self):
        self.setWindowTitle('Lumio')
        self.setGeometry(300, 300, 400, 300)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.agentLabel = QLabel('Select Agent:')
        self.layout.addWidget(self.agentLabel)

        self.agentComboBox = QComboBox()
        self.agentComboBox.addItems(self.agents)
        self.layout.addWidget(self.agentComboBox)

        self.runButton = QPushButton('Run')
        self.runButton.clicked.connect(self.runCommand)
        self.layout.addWidget(self.runButton)

        self.outputTextEdit = QTextEdit()
        self.layout.addWidget(self.outputTextEdit)

        self.trayIcon = QSystemTrayIcon(QIcon('icon.png'), self)
        self.trayIcon.show()

        self.trayIcon.activated.connect(self.iconActivated)

        self.show()

    def runCommand(self):
        agent = self.agentComboBox.currentText()
        command = self.agent_commands[agent]
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.outputTextEdit.append(f"{agent} output: {stdout.decode()}")
        if stderr:
            self.outputTextEdit.append(f"Error: {stderr.decode()}")

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.showNormal()
            self.activateWindow()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Lumio()
    sys.exit(app.exec_())