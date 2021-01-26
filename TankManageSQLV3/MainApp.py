import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QFileDialog, QTreeWidgetItem, QInputDialog,
                         QAbstractItemView,  QMessageBox,QDataWidgetMapper)
from PyQt5.QtCore import (pyqtSlot, Qt,QItemSelectionModel,
                         QModelIndex,QFile,QIODevice)
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRecord, QSqlQuery
from PyQt5.QtGui import QPixmap, QIcon
from TankManageSQLV3.mianwindows import Ui_MainWindow

class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        ##   tableView显示属性设置
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(40)
        self.ui.tableView.horizontalHeader().setDefaultSectionSize(80)
        self.fldNum = [{}, {}]

    ##  ==========由connectSlotsByName() 自动连接的槽函数==================
    @pyqtSlot()  ##选择数据库，打开数据表
    def on_btn_newDB_clicked(self):
        dbFilename, flt = QFileDialog.getSaveFileName(self, "选择数据库文件", "",
                                                      "SQL Lite数据库(*.db *.db3)")
        if (dbFilename == ''):
            return
        self.createDB(dbFilename)

    # 新建数据库
    def createDB(self,Filename):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        # 指定SQLite数据库的文件名
        self.db.setDatabaseName(Filename)
        if self.db.open():
            self.ui.label_Filename.setText(Filename)
            query = QSqlQuery()
            query.exec('create table TankInfo(TankID varchar(10) primary key,  Volume FLOAT, Diameter FLOAT, Date DATE)')
            query.exec('create table WallInfo(TankID varchar(10) primary key, Thickness FLOAT, Damage FLOAT, State varchar(10), isDamage INTEGER)')
            self.__openTable()  # 打开数据表
        else:
            QMessageBox.warning(self, "错误", "打开数据库失败")

    # 打开数据库表单
    def __openTable(self):
        # 创建数据模型指针

        # for i in range(2):
        self.tabModel = [QSqlTableModel(self, self.db),
                         QSqlTableModel(self, self.db)] # 数据模型
        # 设置数据表指针
        self.tabModel[0].setTable("TankInfo")  # 设置数据表1
        self.tabModel[1].setTable("WallInfo")  # 设置数据表2

        for i in range(2):
            self.tabModel[i].setEditStrategy(QSqlTableModel.OnManualSubmit)    #数据保存方式，OnManualSubmit , OnRowChange
            self.tabModel[i].setSort(self.tabModel[i].fieldIndex("TankID"), Qt.AscendingOrder)  # 排序
            if (self.tabModel[i].select() == False):  # 查询数据失败
                QMessageBox.critical(self, "错误信息",
                                     "打开数据表错误,错误信息\n" + self.tabModel[i].lastError().text())
                return

        # 获取字段名和序号
        for i in range(2):
            fieldNum = self.__getFieldNames(i)
            print(fieldNum)

        # 显示字段名字
        self.tabModel[0].setHeaderData(self.fldNum[0]["TankID"], Qt.Horizontal, "储罐编号")

        ##创建界面组件与数据模型的字段之间的数据映射
        self.mapper = [QDataWidgetMapper(), QDataWidgetMapper()]
        for i in range(2):
            self.mapper[i].setModel(self.tabModel[i])  # 设置数据模型
            self.mapper[i].setSubmitPolicy(QDataWidgetMapper.AutoSubmit)

        ##界面组件与tabModel的具体字段之间的联系
        self.mapper[0].addMapping(self.ui.LEidt_TankNo, self.fldNum[0]["TankID"])
        self.mapper[0].addMapping(self.ui.LEdit_Volume, self.fldNum[0]["Volume"])
        self.mapper[0].addMapping(self.ui.LEdit_Diameter, self.fldNum[0]["Diameter"])
        self.mapper[0].addMapping(self.ui.dateEdit, self.fldNum[0]["Date"])
        # self.mapper[1].addMapping(self.ui.LEidt_TankNoWall, self.fldNum[1]["TankID"])
        self.mapper[1].addMapping(self.ui.LEdit_Thickness, self.fldNum[1]["Thickness"])
        self.mapper[1].addMapping(self.ui.LEdit_Damage, self.fldNum[1]["Damage"])
        self.mapper[1].addMapping(self.ui.comboBox_state, self.fldNum[1]["State"])
        self.mapper[1].addMapping(self.ui.checkBox_isdamage, self.fldNum[1]["isDamage"])

        for i in range(2):
            self.mapper[i].toFirst()  # 移动到首记录

        # 选择模型
        self.selModel = [QItemSelectionModel(self.tabModel[0]),
                         QItemSelectionModel(self.tabModel[1])]
        for i in range(2):
            self.selModel[i].currentChanged.connect(self.do_currentChanged)  # 当前项变化时触发
            self.selModel[i].currentRowChanged.connect(self.do_currentRowChanged)  # 选择行变化时

        self.ui.tableView.setModel(self.tabModel[0])  # 设置数据模型
        self.ui.tableView.setSelectionModel(self.selModel[0])  # 设置选择模型

        self.ui.tableView.setColumnHidden(self.fldNum[0]["Volume"], True)  # 隐藏列
        self.ui.tableView.setColumnHidden(self.fldNum[0]["Diameter"], True)  # 隐藏列
        self.ui.tableView.setColumnHidden(self.fldNum[0]["Date"], True)  # 隐藏列

        self.ui.btn_openDB.setEnabled(False)

        self.ui.btn_add.setEnabled(True)
        self.ui.btn_insert.setEnabled(True)
        self.ui.btn_delete.setEnabled(True)

    # 打开数据库
    @pyqtSlot()
    def on_btn_openDB_clicked(self):
        dbFilename, flt = QFileDialog.getOpenFileName(self, "选择数据库文件", "",
                                                      "SQL Lite数据库(*.db *.db3)")
        if (dbFilename == ''):
            return

        # 打开数据库
        self.db = QSqlDatabase.addDatabase("QSQLITE")  # 添加 SQLITE数据库驱动
        self.db.setDatabaseName(dbFilename)  # 设置数据库名称

        if self.db.open():      # 打开数据库
            self.__openTable()  # 打开数据表
        else:
            QMessageBox.warning(self, "错误", "打开数据库失败")

    @pyqtSlot()
    def on_btn_nextRecord_clicked(self):
        for i in range(2):
            self.mapper[i].toNext()  # 移动到首记录

    # 保存到数据库
    @pyqtSlot()
    def on_btn_saveDB_clicked(self):
        for i in range(2):
            res = self.tabModel[i].submitAll()
            if (res == False):
                QMessageBox.information(self, "消息",
                                        "数据保存错误,错误信息\n" + self.tabModel[i].lastError().text())
            else:
                self.ui.btn_saveDB.setEnabled(False)
                self.ui.btn_Revert.setEnabled(False)

    ##取消修改
    @pyqtSlot()
    def on_actRevert_triggered(self):
        for i in range(2):
            self.tabModel[i].revertAll()
        self.ui.btn_saveDB.setEnabled(False)
        self.ui.btn_Revert.setEnabled(False)

    ##添加记录
    @pyqtSlot()
    def on_btn_add_clicked(self):
        for i in range(2):
            self.tabModel[i].insertRow(self.tabModel[i].rowCount(), QModelIndex())  # 在末尾添加一个记录
            curIndex = self.tabModel[i].index(self.tabModel[i].rowCount() - 1, 1)  # 创建最后一行的ModelIndex
            self.selModel[i].clearSelection()  # 清空选择项
            self.selModel[i].setCurrentIndex(curIndex, QItemSelectionModel.Select)  # 设置刚插入的行为当前选择行
            currow = curIndex.row()  # 获得当前行

    ##插入记录
    @pyqtSlot()
    def on_btn_insert_clicked(self):
        curIndex = self.ui.tableView.currentIndex()  # QModelIndex
        for i in range(2):
            self.tabModel[i].insertRow(curIndex.row(), QModelIndex())
            self.selModel[i].clearSelection()  # 清除已有选择
            self.selModel[i].setCurrentIndex(curIndex, QItemSelectionModel.Select)

    ##删除记录
    @pyqtSlot()
    def on_btn_delete_clicked(self):
        curIndex = self.selModel[0].currentIndex()  # 获取当前选择单元格的模型索引
        for i in range(2):
            self.tabModel[i].removeRow(curIndex.row())  # 删除当前行

    @pyqtSlot(str)
    def on_LEidt_TankNo_textChanged(self,text):
        print('currow')
        currow = self.ui.tableView.currentIndex().row()
        print("当前选中第 %d 行" %currow)
        self.tabModel[1].setData(self.tabModel[1].index(currow, self.fldNum[1]["TankID"]), text)


    # 获取所有字段名称
    def __getFieldNames(self, ith):
        emptyRec = self.tabModel[ith].record()  # 获取空记录，只有字段名
        self.fldNum[ith] = {}  # 字段名与序号的字典
        count = emptyRec.count()
        for i in range(emptyRec.count()):
            fieldName = emptyRec.fieldName(i)
            self.fldNum[ith].setdefault(fieldName)
            self.fldNum[ith][fieldName] = i
        print(self.fldNum[ith])

        return count # 返回数据条数

##  =============自定义槽函数===============================
    def do_currentChanged(self, current, previous):   ##更新actPost和actCancel 的状态
        edited = False
        for i in range(2):
            if self.tabModel[i].isDirty():
                edited = True
        self.ui.btn_saveDB.setEnabled(edited)    #有未保存修改时可用
        self.ui.btn_Revert.setEnabled(edited)

    def do_currentRowChanged(self, current, previous): #行切换时的状态控制
        for i in range(2):
            self.mapper[i].setCurrentIndex(current.row())  #更新数据映射的行号
        # curRec=self.tabModel.record(current.row())  #获取当前记录,QSqlRecord类型

##  ============窗体测试程序 ================================
if  __name__ == "__main__":        #用于当前窗体测试
    app = QApplication(sys.argv)    #创建GUI应用程序
    form = QmyMainWindow()            #创建窗体
    form.show()
    sys.exit(app.exec_())