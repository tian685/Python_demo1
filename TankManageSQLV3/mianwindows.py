# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mianwindows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_newDB = QtWidgets.QPushButton(self.centralwidget)
        self.btn_newDB.setGeometry(QtCore.QRect(274, 32, 111, 31))
        self.btn_newDB.setObjectName("btn_newDB")
        self.btn_openDB = QtWidgets.QPushButton(self.centralwidget)
        self.btn_openDB.setGeometry(QtCore.QRect(400, 32, 121, 31))
        self.btn_openDB.setObjectName("btn_openDB")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(10, 482, 75, 31))
        self.btn_add.setObjectName("btn_add")
        self.btn_insert = QtWidgets.QPushButton(self.centralwidget)
        self.btn_insert.setGeometry(QtCore.QRect(100, 482, 75, 31))
        self.btn_insert.setObjectName("btn_insert")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(190, 482, 75, 31))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_saveDB = QtWidgets.QPushButton(self.centralwidget)
        self.btn_saveDB.setEnabled(False)
        self.btn_saveDB.setGeometry(QtCore.QRect(550, 32, 75, 31))
        self.btn_saveDB.setObjectName("btn_saveDB")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(290, 90, 215, 211))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LEdit_Volume = QtWidgets.QLineEdit(self.groupBox)
        self.LEdit_Volume.setObjectName("LEdit_Volume")
        self.gridLayout.addWidget(self.LEdit_Volume, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.LEdit_Diameter = QtWidgets.QLineEdit(self.groupBox)
        self.LEdit_Diameter.setObjectName("LEdit_Diameter")
        self.gridLayout.addWidget(self.LEdit_Diameter, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.LEidt_TankNo = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEidt_TankNo.sizePolicy().hasHeightForWidth())
        self.LEidt_TankNo.setSizePolicy(sizePolicy)
        self.LEidt_TankNo.setObjectName("LEidt_TankNo")
        self.gridLayout.addWidget(self.LEidt_TankNo, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(530, 90, 241, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LEdit_Damage = QtWidgets.QLineEdit(self.groupBox_2)
        self.LEdit_Damage.setObjectName("LEdit_Damage")
        self.gridLayout_3.addWidget(self.LEdit_Damage, 2, 1, 1, 1)
        self.LEidt_TankNoWall = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEidt_TankNoWall.sizePolicy().hasHeightForWidth())
        self.LEidt_TankNoWall.setSizePolicy(sizePolicy)
        self.LEidt_TankNoWall.setObjectName("LEidt_TankNoWall")
        self.gridLayout_3.addWidget(self.LEidt_TankNoWall, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.LEdit_Thickness = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEdit_Thickness.sizePolicy().hasHeightForWidth())
        self.LEdit_Thickness.setSizePolicy(sizePolicy)
        self.LEdit_Thickness.setObjectName("LEdit_Thickness")
        self.gridLayout_3.addWidget(self.LEdit_Thickness, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.comboBox_state = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_state.setObjectName("comboBox_state")
        self.comboBox_state.addItem("")
        self.comboBox_state.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_state, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)
        self.checkBox_isdamage = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_isdamage.setText("")
        self.checkBox_isdamage.setObjectName("checkBox_isdamage")
        self.gridLayout_3.addWidget(self.checkBox_isdamage, 4, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.label_Filename = QtWidgets.QLabel(self.centralwidget)
        self.label_Filename.setGeometry(QtCore.QRect(10, 10, 261, 16))
        self.label_Filename.setObjectName("label_Filename")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 40, 231, 411))
        self.tableView.setObjectName("tableView")
        self.btn_Revert = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Revert.setEnabled(False)
        self.btn_Revert.setGeometry(QtCore.QRect(650, 32, 75, 31))
        self.btn_Revert.setObjectName("btn_Revert")
        self.btn_nextRecord = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nextRecord.setGeometry(QtCore.QRect(290, 340, 121, 31))
        self.btn_nextRecord.setObjectName("btn_nextRecord")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_newDB.setText(_translate("MainWindow", "新建数据库"))
        self.btn_openDB.setText(_translate("MainWindow", "打开数据库"))
        self.btn_add.setText(_translate("MainWindow", "增加"))
        self.btn_insert.setText(_translate("MainWindow", "插入"))
        self.btn_delete.setText(_translate("MainWindow", "删除"))
        self.btn_saveDB.setText(_translate("MainWindow", "保存"))
        self.groupBox.setTitle(_translate("MainWindow", "储罐基本信息"))
        self.label_3.setText(_translate("MainWindow", "直径"))
        self.label.setText(_translate("MainWindow", "罐号"))
        self.label_2.setText(_translate("MainWindow", "体积"))
        self.label_7.setText(_translate("MainWindow", "时间"))
        self.groupBox_2.setTitle(_translate("MainWindow", "罐壁信息"))
        self.label_6.setText(_translate("MainWindow", "罐号"))
        self.label_5.setText(_translate("MainWindow", "损伤因子"))
        self.label_4.setText(_translate("MainWindow", "厚度"))
        self.label_8.setText(_translate("MainWindow", "状态"))
        self.comboBox_state.setItemText(0, _translate("MainWindow", "良好"))
        self.comboBox_state.setItemText(1, _translate("MainWindow", "不及格"))
        self.label_9.setText(_translate("MainWindow", "应力腐蚀"))
        self.label_Filename.setText(_translate("MainWindow", "TextLabel"))
        self.btn_Revert.setText(_translate("MainWindow", "取消"))
        self.btn_nextRecord.setText(_translate("MainWindow", "下一条数据"))

