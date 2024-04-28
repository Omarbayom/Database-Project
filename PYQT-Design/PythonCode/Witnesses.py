# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'Witnesses.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
curr_dir = os.path.dirname('systemdb\Classes\Witness.py')
parent_dir = os.path.dirname(curr_dir)
sys.path.insert(0, parent_dir)
from Classes.Witness import Witness


class Witnesses(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.Witnesses =  Witness.get_all()
        self.populate_table()

    def setupUi(self):
        self.setObjectName("Witnesses")
        self.resize(1007, 678)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.WitnessSearchField = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WitnessSearchField.sizePolicy().hasHeightForWidth())
        self.WitnessSearchField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.WitnessSearchField.setFont(font)
        self.WitnessSearchField.setObjectName("WitnessSearchField")
        self.horizontalLayout_2.addWidget(self.WitnessSearchField)
        self.WitnessSearchBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WitnessSearchBtn.sizePolicy().hasHeightForWidth())
        self.WitnessSearchBtn.setSizePolicy(sizePolicy)
        self.WitnessSearchBtn.clicked.connect(self.search_Witnesses)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.WitnessSearchBtn.setFont(font)
        self.WitnessSearchBtn.setObjectName("WitnessSearchBtn")
        self.horizontalLayout_2.addWidget(self.WitnessSearchBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.WitnessScrollArea = QtWidgets.QScrollArea(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WitnessScrollArea.sizePolicy().hasHeightForWidth())
        self.WitnessScrollArea.setSizePolicy(sizePolicy)
        self.WitnessScrollArea.setWidgetResizable(True)
        self.WitnessScrollArea.setObjectName("WitnessScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 893, 515))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.WitnessScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.WitnessScrollArea, 2, 0, 1, 1)

        self.WitnessTable = QtWidgets.QTableWidget(self)
        self.WitnessTable.setObjectName("WitnessTable")
        self.WitnessTable.setColumnCount(8) # Number of columns
        self.WitnessTable.setHorizontalHeaderLabels(['VictimID', 'First Name', 'Last Name', 'Date of Birht', 'Gender', 'Age', 'Address','Delete'])
        self.gridLayout.addWidget(self.WitnessTable, 2, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.AddWitnessBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddWitnessBtn.sizePolicy().hasHeightForWidth())
        self.AddWitnessBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AddWitnessBtn.setFont(font)
        self.AddWitnessBtn.setObjectName("AddWitnessBtn")
        self.horizontalLayout.addWidget(self.AddWitnessBtn)
        self.BackBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackBtn.sizePolicy().hasHeightForWidth())
        self.BackBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BackBtn.setFont(font)
        self.BackBtn.setObjectName("BackBtn")
        self.horizontalLayout.addWidget(self.BackBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.WitnessSearchBtn.setText(_translate("self", "Search"))
        self.label.setText(_translate("self", "Witnesses"))
        self.AddWitnessBtn.setText(_translate("self", "Add"))
        self.BackBtn.setText(_translate("self", "Back"))

    def populate_table(self):
        self.WitnessTable.setRowCount(len(self.Witnesses))
        for i, Witness in enumerate(self.Witnesses):
            for j, data in enumerate(Witness):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.WitnessTable.setItem(i, j, item)
            remove_button = QtWidgets.QPushButton("Remove")
            remove_button.clicked.connect(lambda _, Witness=Witness: self.remove_Witnesses(Witness))
            self.WitnessTable.setCellWidget(i, len(Witness), remove_button)

    def search_Witnesses(self):
        search_value = self.WitnessSearchField.text()
        self.WitnessSearchField.clear() 
        if search_value:
            self.Witnesses = Witness.search(search_value)
            if not self.Witnesses:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("No Witness found")
                msg.setWindowTitle("Search")
                msg.exec_()
            else:
                self.populate_table()
        else:
            self.Witnesses = Witness.get_all()
            self.populate_table()
    def remove_Witnesses(self, suspect_row):
        Witness.delete('WitnessID',suspect_row[0])
        self.Witnesses = Witness.get_all()
        self.populate_table()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QWidget()
#     ui = Ui_self()
#     ui.setupUi(self)
#     self.show()
#     sys.exit(app.exec_())
