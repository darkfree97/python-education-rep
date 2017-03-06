import sys, textProcessor
from PyQt4 import QtGui, uic

ui = uic.loadUiType("Les1.ui")[0]


class MainWindow(QtGui.QMainWindow, ui):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.go_to_work)
        self.pushButton_2.clicked.connect(self.setClear)
        self.open_file.triggered.connect(self.fileOpen)
        self.read_file.triggered.connect(self.file_read)

    def go_to_work(self):
        text = self.textEdit.toPlainText()
        textProcessor.textProcessor(text)
        self.statusbar.showMessage("Ваш текст оброблено", 1000)

    def setClear(self):
        self.textEdit.clear()
        self.statusbar.showMessage("Поле успішно очищено", 1000)
        self.textEdit.setReadOnly(False)

    def fileOpen(self):
        self.textEdit.clear()
        file = open("Files/names.txt", "r")
        for line in file:
            self.textEdit.append(line)
        file.close()
        file = open("Files/dates.txt", "r")
        for line in file:
            self.textEdit.append(line)
        file.close()
        file = open("Files/phones.txt", "r")
        for line in file:
            self.textEdit.append(line)
        file.close()
        file = open("Files/mails.txt", "r")
        for line in file:
            self.textEdit.append(line)
        file.close()
        self.textEdit.setReadOnly(True)

    def file_read(self):
        self.textEdit.clear()
        file = open("Files/start_file.txt", "r")
        self.textEdit.append(file.read())
