# -*- coding: utf-8 -*-

##  GUI应用程序主程序入口

import sys

from PyQt5.QtWidgets import  QApplication

from FullCode_PythonQt.chap12QtChart.Demo12_7FillArea.myMainWindow import QmyMainWindow
    
app = QApplication(sys.argv)    #创建GUI应用程序

mainform=QmyMainWindow()        #创建主窗体

mainform.show()                 #显示主窗体

sys.exit(app.exec_()) 