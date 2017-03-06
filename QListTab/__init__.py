import sys
from PyQt4 import QtGui, QtCore, uic


class PaletteTableModel(QtCore.QAbstractTableModel):
    def __init__(self, colors=[[]], headers=[], parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._colors = colors
        self._headers = headers

    def rowCount(self, parent):
        return len(self._colors)

    def columnCount(self, parent):
        return len(self._colors)

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

    def data(self, index, role):
        row = index.row()
        column = index.column()
        if role == QtCore.Qt.EditRole:
            return self._colors[row][column].name()

        if role == QtCore.Qt.ToolTipRole:
            return "Hex code: "+self._colors[row][column].name()

        if role == QtCore.Qt.DecorationRole:
            value = self._colors[row][column]

            pixmap = QtGui.QPixmap(26, 26)
            pixmap.fill(value)

            image = QtGui.QImage(pixmap)
            return image

        if role == QtCore.Qt.DisplayRole:
            value = self._colors[row][column]
            return value.name()

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            color = QtGui.QColor(value)
            if color.isValid():
                self._colors[row][column] = color
                self.dataChanged.emit(index, index)
                return True
            return False

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._headers[section]
            else:
                return "Color - %d" % (section + 1)


class PaletteListModel(QtCore.QAbstractListModel):
    def __init__(self, colors=[], parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._colors = colors

    def data(self, index, role):
        if role == QtCore.Qt.EditRole:
            return self._colors[index.row()].name()

        if role == QtCore.Qt.ToolTipRole:
            return "Hex code: "+self._colors[index.row()].name()

        if role == QtCore.Qt.DecorationRole:
            row = index.row()
            value = self._colors[row]

            pixmap = QtGui.QPixmap(26, 26)
            pixmap.fill(value)

            image = QtGui.QImage(pixmap)
            return image

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self._colors[row]
            return value.name()

    def rowCount(self, parent):
        return len(self._colors)

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return "Palette"
            else:
                return "Color - %d" % (section+1)

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            color = QtGui.QColor(value)
            if color.isValid():
                self._colors[row] = color
                self.dataChanged.emit(index, index)
                return True
            return False

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginInsertRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i in range(rows):
            self._colors.insert(position, QtGui.QColor("black"))

        self.endInsertRows()
        return True

    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i in range(rows):
            value = self._colors[position]
            self._colors.remove(value)
        self.endRemoveRows()
        return True

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")

    # ///////////////Les 1////////////////

    # data = ["one", "two", "three", "four", "five"]

    # //no model use
    # listWigdet = QtGui.QListWidget()
    # listWigdet.addItems(data)
    # listWigdet.show()
    #
    # count = listWigdet.count()
    # for i in range(count):
    #     item = listWigdet.item(i)
    #     item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
    #
    # cbox = QtGui.QComboBox()
    # cbox.addItems(data)
    # cbox.show()

    # //modeluse
    # model = QtGui.QStringListModel(data)
    #
    # listView = QtGui.QListView()
    # listView.setModel(model)
    # listView.show()
    #
    # cbox = QtGui.QComboBox()
    # cbox.setModel(model)
    # cbox.show()

    # ////////////////Les 2 ///////////////////

    # listView = QtGui.QListView()
    # listView.show()
    #
    # treeView = QtGui.QTreeView()
    # treeView.show()
    #
    # comboBox = QtGui.QComboBox()
    # comboBox.show()
    #
    # tableView = QtGui.QTableView()
    # tableView.show()
    #
    # red = QtGui.QColor(255, 0, 0)
    # green = QtGui.QColor(0, 255, 0)
    # blue = QtGui.QColor(0, 0, 255)
    #
    # model = PaletteListModel([red, green, blue])
    #
    # listView.setModel(model)
    # treeView.setModel(model)
    # comboBox.setModel(model)
    # tableView.setModel(model)

    # //////////////////Les 3 //////////////////

    listView = QtGui.QListView()
    listView.show()

    treeView = QtGui.QTreeView()
    treeView.show()

    comboBox = QtGui.QComboBox()
    comboBox.show()

    tableView = QtGui.QTableView()
    tableView.show()

    red = QtGui.QColor("red")
    green = QtGui.QColor("green")
    blue = QtGui.QColor("blue")

    tableData = [
        [red, green, blue],
        [green, blue, red],
        [blue, red, green, green],
    ]
    model = PaletteTableModel(tableData, ["Pa", "le", "te"])

    # model = PaletteListModel([red, green, blue])

    listView.setModel(model)
    treeView.setModel(model)
    comboBox.setModel(model)
    tableView.setModel(model)



    # model.insertRows(0, 5)
    # model.removeRows(1, 5)

    sys.exit(app.exec_())
