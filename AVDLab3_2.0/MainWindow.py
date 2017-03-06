from PyQt4 import QtCore, QtGui, uic
import re


ui = uic.loadUiType("AVDLab3.ui")[0]


class MainWindow(QtGui.QMainWindow, ui):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fileOpen.triggered.connect(self.openFile)
        self.lineSearch.textChanged.connect(self.validate)
        self.findButton.clicked.connect(self.find_phone)
        self.reg_exp = ""
        self.file_name = ""

    def paintEvent(self, *args, **kwargs):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        gradient = QtGui.QConicalGradient(self.width()/2, self.height()/2, 0)
        gradient.setColorAt(0, QtCore.Qt.gray)
        gradient.setColorAt(0.2, QtCore.Qt.cyan)
        gradient.setColorAt(0.5, QtCore.Qt.white)
        gradient.setColorAt(0.8, QtCore.Qt.cyan)
        gradient.setColorAt(1, QtCore.Qt.gray)
        painter.setBrush(gradient)
        painter.drawRect(self.rect())

    def openFile(self):
        try:
            self.file_name = QtGui.QFileDialog.getOpenFileName(self, "Виберіть файл", "", "*.txt")
            file = open(self.file_name, "r")
            self.textEdit.setText(file.read())
            file.close()
        except FileNotFoundError:
            pass

    def validate(self):
        reg_exp = re.search("^\+380\d{9}$|^\+1\d{10}$", self.lineSearch.text(), flags=0)
        if reg_exp is not None:
            self.info.setText("<div style='color:green'>Хороша робота</div>")
        else:
            self.info.setText("<div style='color:red'>Введено невірні дані</div>")

    def find_phone(self):
        if self.lineSearch.text()=="":
            QtGui.QMessageBox.critical(None, "Повідомлення", "Поле пошуку номеру не заповнено!")
        elif self.textEdit.toPlainText()=="":
            QtGui.QMessageBox.critical(None, "Повідомлення", "Ви не вибрали телефонну книгу!\n"
                                                             "Виберіть телефонну книгу і повторіть пошук.")
        else:
            self.reg_exp = "\\"+self.lineSearch.text()
            self.lineShow.clear()
            try:
                file = open(self.file_name, "r")
                for line in file:
                    buf = line
                    regg = re.search(self.reg_exp, buf)
                    if regg is not None:
                        point = buf.find("-")
                        self.lineShow.setText(buf[(point + 2):-1])
                file.close()
            except FileNotFoundError:
                pass


