from MainWindow import *


app = QtGui.QApplication(sys.argv)
my_window = MainWindow()
my_window.setWindowTitle("AVD Обробка тексту")
my_window.show()
app.exec()
