from PyQt4 import QtCore, QtGui


class Item:
    def __init__(self, name, surname, birth, mail, phone):
        self.name = name
        self.surname = surname
        self.birth = birth
        self.mail = mail
        self.phone = phone

    def __str__(self):
        return "------------Item------------" \
               "\nName    - "+self.name + \
               "\nSurname - "+self.surname + \
               "\nBirth   - "+self.birth + \
               "\nMail    - "+self.mail + \
               "\nPhone   - "+self.phone + "\n" \
                                           "------------End-------------"

    def getList(self):
        return [self.name, self.surname, self.birth, self.mail, self.phone]

    def __len__(self):
        return 5


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, items=[], headers=[], parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._items = items
        self._headers = headers

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._items)

    def columnCount(self, parent=None, *args, **kwargs):
        return 5

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

    def data(self, index, role):
        row = index.row()
        column = index.column()
        if role == QtCore.Qt.EditRole:
            return self._items[row][column]

        if role == QtCore.Qt.ToolTipRole:
            return self._items[row][column]

        if role == QtCore.Qt.DisplayRole:
            value = self._items[row][column]
            return value

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            self._items[row][column] = value
            self.dataChanged.emit(index, index)
            return True

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._headers[section]
            else:
                return section + 1

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginInsertRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i in range(rows):
            self._items.insert(position, Item("Ihor", "Paliy", "1997-06-06", "darkfree97@gmail.com", "+380977456929").getList())
        self.endInsertRows()
        return True

    def removeRows(self, position, rows=-1, parent=QtCore.QModelIndex()):
        if rows == -1:
            rows = len(self._items)
        self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i in range(rows):
            value = self._items[position]
            self._items.remove(value)
        self.endRemoveRows()
        return True

    def insertRow(self, item=[], parent=None, *args, **kwargs):
        self.beginInsertRows(QtCore.QModelIndex(), 0, 0)
        self._items.insert(self.rowCount(), item)
        self.endInsertRows()
        return True
