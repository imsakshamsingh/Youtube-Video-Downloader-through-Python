# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ytD.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
       
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(398, 294)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(240, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(170, 130, 181, 91))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.r1 = QtWidgets.QRadioButton(self.groupBox)
        self.r1.setGeometry(QtCore.QRect(10, 30, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.r1.setFont(font)
        self.r1.setObjectName("r1")
        self.r2 = QtWidgets.QRadioButton(self.groupBox)
        self.r2.setGeometry(QtCore.QRect(10, 50, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.r2.setFont(font)
        self.r2.setObjectName("r2")
        self.r3 = QtWidgets.QRadioButton(self.groupBox)
        self.r3.setGeometry(QtCore.QRect(10, 70, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.r3.setFont(font)
        self.r3.setObjectName("r3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(0, -10, 401, 311))
        self.pushButton.setStyleSheet("background-color: rgb(158, 255, 174);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.download = QtWidgets.QPushButton(Dialog)
        self.download.setGeometry(QtCore.QRect(180, 250, 111, 23))
        self.download.setObjectName("download")
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.groupBox.raise_()
        self.download.raise_()
        self.download.clicked.connect(self.Dwnld)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Youtube Link Here:"))
        self.label_2.setText(_translate("Dialog", "Select Quality"))
        self.r1.setText(_translate("Dialog", "360p"))
        self.r2.setText(_translate("Dialog", "480p"))
        self.r3.setText(_translate("Dialog", "720p"))
        self.download.setText(_translate("Dialog", "Download"))

    def Dwnld(self):
        print("jingu")
        a = self.lineEdit.text()
        print(a)
        b =""
        if self.r1.isChecked():
            b="360p"
            print(b)
        elif self.r2.isChecked():
            b="480p"
            
            print(b)
        else:
            b="720p"
            
            print(b)
            
        yt = YouTube(a)
        yt = yt.streams.filter(res=b).first()
        print(yt)
        if yt:
            #just change the destination directory here
            yt.download('D:\Python Tweaks\Youtube View Dwnloader\downloads')
        else:
            print("link Doesn't Exist")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

