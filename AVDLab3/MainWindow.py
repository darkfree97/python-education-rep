import sys, textProcessor
from PyQt4 import QtGui, uic
from Item import TableModel, Item
import query

ui = uic.loadUiType("AVDLab3.ui")[0]


class MainWindow(QtGui.QMainWindow, ui):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.model = TableModel([Item("Ihor", "Paliy", "1997-06-06", "darkfree97@gmail.com", "+380977456929").getList()], ['Name', 'Surname', "Birth date", "Mail", "Phone"])
        self.query = query.Query()
        self.fopen.triggered.connect(self.upload)
        self.clearArea.clicked.connect(self._clearArea)
        self.startall.clicked.connect(self.startAll)
        self.tableView.setModel(self.model)
        self._clearArea()

    def upload(self):
        try:
            file = open("files/file.txt", "r")
            self.textEdit.setText(file.read())
        except FileNotFoundError:
            self.textEdit.setPlainText("File not found!")

    def _clearArea(self):
        self.textEdit.clear()
        self.textEdit.setReadOnly(False)
        self.model.removeRows(0)

    def start(self, phones):
        if len(phones) == 0:
            return
        unknown = "Номери яких не має в базі даних:\n"
        items = self.query.search(phones)
        for item in items:
            self.model.insertRow(item.getList())
        for phone in phones:
            f = True
            for item in items:
                if item.getList()[4] == phone:
                    f = False
            if f:
                unknown += phone+"\n"
        QtGui.QMessageBox.information(self, "Невідомі номери", unknown)

    def startAll(self):
        text = self.textEdit.toPlainText()
        self.model.removeRows(0)
        arr = textProcessor.textProcessorR(str(text))
        try:
            file = open("files/phones.txt", "r")
            self.textEdit.setText(file.read())
        except FileNotFoundError:
            self.textEdit.setPlainText("")
        self.textEdit.setReadOnly(True)
        self.start(arr[3])
