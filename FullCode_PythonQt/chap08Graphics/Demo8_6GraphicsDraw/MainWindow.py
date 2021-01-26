# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 380)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 568, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setIconSize(QtCore.QSize(16, 16))
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actItem_Rect = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/RECTANGL.BMP"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actItem_Rect.setIcon(icon)
        self.actItem_Rect.setObjectName("actItem_Rect")
        self.actItem_Ellipse = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/ELLIPSE.BMP"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actItem_Ellipse.setIcon(icon1)
        self.actItem_Ellipse.setObjectName("actItem_Ellipse")
        self.actItem_Line = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/LINE.BMP"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actItem_Line.setIcon(icon2)
        self.actItem_Line.setObjectName("actItem_Line")
        self.actEdit_Delete = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/108.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actEdit_Delete.setIcon(icon3)
        self.actEdit_Delete.setObjectName("actEdit_Delete")
        self.actQuit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuit.setIcon(icon4)
        self.actQuit.setObjectName("actQuit")
        self.actItem_Pixmap = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/824.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actItem_Pixmap.setIcon(icon5)
        self.actItem_Pixmap.setObjectName("actItem_Pixmap")
        self.actItem_Text = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/800.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actItem_Text.setIcon(icon6)
        self.actItem_Text.setObjectName("actItem_Text")
        self.actEdit_Front = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/images/528.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actEdit_Front.setIcon(icon7)
        self.actEdit_Front.setObjectName("actEdit_Front")
        self.actEdit_Back = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/images/526.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actEdit_Back.setIcon(icon8)
        self.actEdit_Back.setObjectName("actEdit_Back")
        self.actItem_Polygon = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/images/FREEFORM.BMP"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actItem_Polygon.setIcon(icon9)
        self.actItem_Polygon.setObjectName("actItem_Polygon")
        self.actZoomIn = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/images/zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actZoomIn.setIcon(icon10)
        self.actZoomIn.setObjectName("actZoomIn")
        self.actZoomOut = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/images/zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actZoomOut.setIcon(icon11)
        self.actZoomOut.setObjectName("actZoomOut")
        self.actRotateLeft = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/images/rotateleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRotateLeft.setIcon(icon12)
        self.actRotateLeft.setObjectName("actRotateLeft")
        self.actRotateRight = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/images/rotateright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRotateRight.setIcon(icon13)
        self.actRotateRight.setObjectName("actRotateRight")
        self.actRestore = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/images/420.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRestore.setIcon(icon14)
        self.actRestore.setObjectName("actRestore")
        self.actGroup = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/images/UNGROUP.BMP"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actGroup.setIcon(icon15)
        self.actGroup.setObjectName("actGroup")
        self.actGroupBreak = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/images/128.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actGroupBreak.setIcon(icon16)
        self.actGroupBreak.setObjectName("actGroupBreak")
        self.actItem_Circle = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/images/08.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actItem_Circle.setIcon(icon17)
        self.actItem_Circle.setObjectName("actItem_Circle")
        self.actItem_Triangle = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/images/Icon1242.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actItem_Triangle.setIcon(icon18)
        self.actItem_Triangle.setObjectName("actItem_Triangle")
        self.mainToolBar.addAction(self.actZoomIn)
        self.mainToolBar.addAction(self.actZoomOut)
        self.mainToolBar.addAction(self.actRestore)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actRotateLeft)
        self.mainToolBar.addAction(self.actRotateRight)
        self.mainToolBar.addAction(self.actEdit_Front)
        self.mainToolBar.addAction(self.actEdit_Back)
        self.mainToolBar.addAction(self.actGroup)
        self.mainToolBar.addAction(self.actGroupBreak)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actEdit_Delete)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actQuit)
        self.toolBar.addAction(self.actItem_Rect)
        self.toolBar.addAction(self.actItem_Ellipse)
        self.toolBar.addAction(self.actItem_Circle)
        self.toolBar.addAction(self.actItem_Triangle)
        self.toolBar.addAction(self.actItem_Polygon)
        self.toolBar.addAction(self.actItem_Line)
        self.toolBar.addAction(self.actItem_Text)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo8_5, Graphics View绘图"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actItem_Rect.setText(_translate("MainWindow", "矩形"))
        self.actItem_Rect.setToolTip(_translate("MainWindow", "添加矩形"))
        self.actItem_Ellipse.setText(_translate("MainWindow", "椭圆"))
        self.actItem_Ellipse.setToolTip(_translate("MainWindow", "添加椭圆型"))
        self.actItem_Line.setText(_translate("MainWindow", "直线"))
        self.actItem_Line.setToolTip(_translate("MainWindow", "添加直线"))
        self.actEdit_Delete.setText(_translate("MainWindow", "删除"))
        self.actEdit_Delete.setToolTip(_translate("MainWindow", "删除选中的图元"))
        self.actQuit.setText(_translate("MainWindow", "退出"))
        self.actQuit.setToolTip(_translate("MainWindow", "退出本系统"))
        self.actItem_Pixmap.setText(_translate("MainWindow", "图片"))
        self.actItem_Pixmap.setToolTip(_translate("MainWindow", "添加图片"))
        self.actItem_Text.setText(_translate("MainWindow", "文字"))
        self.actItem_Text.setToolTip(_translate("MainWindow", "添加文字"))
        self.actEdit_Front.setText(_translate("MainWindow", "前置"))
        self.actEdit_Front.setToolTip(_translate("MainWindow", "居于最前面"))
        self.actEdit_Back.setText(_translate("MainWindow", "后置"))
        self.actEdit_Back.setToolTip(_translate("MainWindow", "居于最后面"))
        self.actItem_Polygon.setText(_translate("MainWindow", "梯形"))
        self.actItem_Polygon.setToolTip(_translate("MainWindow", "添加梯形"))
        self.actZoomIn.setText(_translate("MainWindow", "放大"))
        self.actZoomIn.setToolTip(_translate("MainWindow", "放大"))
        self.actZoomOut.setText(_translate("MainWindow", "缩小"))
        self.actZoomOut.setToolTip(_translate("MainWindow", "缩小"))
        self.actRotateLeft.setText(_translate("MainWindow", "左旋转"))
        self.actRotateLeft.setToolTip(_translate("MainWindow", "左旋转"))
        self.actRotateRight.setText(_translate("MainWindow", "右旋转"))
        self.actRotateRight.setToolTip(_translate("MainWindow", "右旋转"))
        self.actRestore.setText(_translate("MainWindow", "恢复"))
        self.actRestore.setToolTip(_translate("MainWindow", "恢复大小"))
        self.actGroup.setText(_translate("MainWindow", "组合"))
        self.actGroup.setToolTip(_translate("MainWindow", "组合"))
        self.actGroupBreak.setText(_translate("MainWindow", "打散"))
        self.actGroupBreak.setToolTip(_translate("MainWindow", "取消组合"))
        self.actItem_Circle.setText(_translate("MainWindow", "圆形"))
        self.actItem_Circle.setToolTip(_translate("MainWindow", "圆形"))
        self.actItem_Triangle.setText(_translate("MainWindow", "三角形"))
        self.actItem_Triangle.setToolTip(_translate("MainWindow", "三角形"))

import res_rc
