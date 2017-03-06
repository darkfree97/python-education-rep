import sys
from MainWindow import *

app = QtGui.QApplication(sys.argv)
my_window = MainWindow()
my_window.show()
app.exec()
