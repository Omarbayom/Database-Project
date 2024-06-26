# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'AddVictim.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Classes.Victim import Victim


class AddVictim(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("AddVictim")
        self.resize(1007, 678)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)
        self.BackBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BackBtn.setFont(font)
        self.BackBtn.setObjectName("BackBtn")
        self.gridLayout.addWidget(self.BackBtn, 12, 0, 1, 1)
        self.VictimLastNameField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.VictimLastNameField.setFont(font)
        self.VictimLastNameField.setObjectName("VictimLastNameField")
        self.gridLayout.addWidget(self.VictimLastNameField, 7, 2, 1, 1)
        self.VictimIDField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.VictimIDField.setFont(font)
        self.VictimIDField.setObjectName("VictimIDField")
        self.gridLayout.addWidget(self.VictimIDField, 3, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.AddVictimDataBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AddVictimDataBtn.setFont(font)
        self.AddVictimDataBtn.setObjectName("AddVictimDataBtn")
        self.gridLayout.addWidget(self.AddVictimDataBtn, 12, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.VictimFirstNameField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.VictimFirstNameField.setFont(font)
        self.VictimFirstNameField.setObjectName("VictimFirstNameField")
        self.gridLayout.addWidget(self.VictimFirstNameField, 6, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 3, 1, 1)
        self.VictimAddrField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.VictimAddrField.setFont(font)
        self.VictimAddrField.setObjectName("VictimAddrField")
        self.gridLayout.addWidget(self.VictimAddrField, 10, 2, 1, 1)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.VictimDOBField = QtWidgets.QDateEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.VictimDOBField.setFont(font)
        self.VictimDOBField.setObjectName("VictimDOBField")
        self.gridLayout.addWidget(self.VictimDOBField, 8, 2, 1, 1)
        self.VictimGenderFIeld = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.VictimGenderFIeld.setFont(font)
        self.VictimGenderFIeld.setObjectName("VictimGenderFIeld")
        self.gridLayout.addWidget(self.VictimGenderFIeld, 9, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 11, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 3, 3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 4, 1, 1, 1)

        self.AddVictimDataBtn.clicked.connect(self.add_victim)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_9.setText(_translate("self", "Gender"))
        self.label_2.setText(_translate("self", "Victim ID"))
        self.label_5.setText(_translate("self", "First Name"))
        self.label_4.setText(_translate("self", "Address"))
        self.label_3.setText(_translate("self", "DOB"))
        self.label_6.setText(_translate("self", "Last Name"))
        self.BackBtn.setText(_translate("self", "Back"))
        self.label.setText(_translate("self", "Add Victim"))
        self.AddVictimDataBtn.setText(_translate("self", "Add"))

    def add_victim(self):
        victim_id = self.VictimIDField.text()
        victim_fname = self.VictimFirstNameField.text()
        victim_lname = self.VictimLastNameField.text()
        victim_dob = self.VictimDOBField.text()
        victim_gender = self.VictimGenderFIeld.text()
        victim_addr = self.VictimAddrField.text()

        if victim_id == "" or victim_fname == "" or victim_lname == "" or victim_dob == ""  or victim_gender == "" or victim_addr == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Please fill all fields")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        
        tmp = Victim.get_all()
        tmp = [x[0] for x in tmp]
        
        try:
            victim_id = int(victim_id)
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Victim ID must be a number")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        
        if victim_id in tmp:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Victim ID already exists")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        
        victim = Victim(victim_id, victim_fname, victim_lname, victim_dob, victim_gender, victim_addr)
        victim.insert_into_database()
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Victim added successfully")
        msg.setWindowTitle("Success")
        msg.exec_()
        self.VictimIDField.clear()
        self.VictimFirstNameField.clear()
        self.VictimLastNameField.clear()
        self.VictimDOBField.clear()
        self.VictimGenderFIeld.clear()
        self.VictimAddrField.clear()


        

        

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QWidget()
#     ui = Ui_self()
#     ui.setupUi(self)
#     self.show()
#     sys.exit(app.exec_())
