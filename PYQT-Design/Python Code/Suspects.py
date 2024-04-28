import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

curr_dir = os.path.dirname('systemdb\Classes\Suspect.py')
parent_dir = os.path.dirname(curr_dir)
sys.path.insert(0, parent_dir)
from Classes.Suspect import Suspect


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1007, 678)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.SuspectSearchField = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SuspectSearchField.sizePolicy().hasHeightForWidth())
        self.SuspectSearchField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectSearchField.setFont(font)
        self.SuspectSearchField.setObjectName("SuspectSearchField")
        self.horizontalLayout_2.addWidget(self.SuspectSearchField)
        self.SuspectSearchBtn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SuspectSearchBtn.sizePolicy().hasHeightForWidth())
        self.SuspectSearchBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectSearchBtn.setFont(font)
        self.SuspectSearchBtn.setObjectName("SuspectSearchBtn")
        self.horizontalLayout_2.addWidget(self.SuspectSearchBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        
        # Table to display suspects
        self.SuspectTable = QtWidgets.QTableWidget(Form)
        self.SuspectTable.setObjectName("SuspectTable")
        self.SuspectTable.setColumnCount(10) # Number of columns
        self.SuspectTable.setHorizontalHeaderLabels(['SuspectID', 'First Name', 'Last Name', 'Gender', 'Date of Birth', 'Phone Record', ' Street', ' Government', ' ZIP', 'Criminal Record'])
        self.gridLayout.addWidget(self.SuspectTable, 2, 0, 1, 1)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.AddSuspectBtn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddSuspectBtn.sizePolicy().hasHeightForWidth())
        self.AddSuspectBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AddSuspectBtn.setFont(font)
        self.AddSuspectBtn.setObjectName("AddSuspectBtn")
        self.horizontalLayout.addWidget(self.AddSuspectBtn)
        self.BackBtn = QtWidgets.QPushButton(Form)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SuspectSearchBtn.setText(_translate("Form", "Search"))
        self.label.setText(_translate("Form", "Suspects"))
        self.AddSuspectBtn.setText(_translate("Form", "Add"))
        self.BackBtn.setText(_translate("Form", "Back"))
    
    def populate_table(self, suspects):
        self.SuspectTable.setRowCount(len(suspects))
        for i, suspect in enumerate(suspects):
            for j, data in enumerate(suspect):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.SuspectTable.setItem(i, j, item)

    def search_suspects(self):
        search_value = self.SuspectSearchField.text()
        if search_value:
            suspects = Suspect.search(search_value)
            self.populate_table(suspects)
        else:
            print("Please enter a search value.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    suspects = Suspect.get_all()  
    ui.populate_table(suspects)
    ui.SuspectSearchBtn.clicked.connect(ui.search_suspects) 
    Form.show()
    sys.exit(app.exec_())