# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_missing_value.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.listWidget_var = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_var.setObjectName("listWidget_var")
        self.verticalLayout_2.addWidget(self.listWidget_var)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_add = QtWidgets.QPushButton(self.tab)
        self.pushButton_add.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pyqt/source/images/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_9.addWidget(self.pushButton_add)
        self.pushButton_delete = QtWidgets.QPushButton(self.tab)
        self.pushButton_delete.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pyqt/source/images/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon1)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout_9.addWidget(self.pushButton_delete)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.listWidget_selected = QtWidgets.QListWidget(self.tab)
        self.listWidget_selected.setObjectName("listWidget_selected")
        self.horizontalLayout_7.addWidget(self.listWidget_selected)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_selected_add = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_add.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_add.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pyqt/source/images/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_add.setIcon(icon2)
        self.pushButton_selected_add.setObjectName("pushButton_selected_add")
        self.verticalLayout_10.addWidget(self.pushButton_selected_add)
        self.pushButton_selected_up = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_up.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_up.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pyqt/source/images/up1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_up.setIcon(icon3)
        self.pushButton_selected_up.setObjectName("pushButton_selected_up")
        self.verticalLayout_10.addWidget(self.pushButton_selected_up)
        self.pushButton_selected_down = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_down.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_down.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pyqt/source/images/down1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_down.setIcon(icon4)
        self.pushButton_selected_down.setObjectName("pushButton_selected_down")
        self.verticalLayout_10.addWidget(self.pushButton_selected_down)
        self.pushButton_selected_del = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_del.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_del.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pyqt/source/images/lc_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_del.setIcon(icon5)
        self.pushButton_selected_del.setObjectName("pushButton_selected_del")
        self.verticalLayout_10.addWidget(self.pushButton_selected_del)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_6.addWidget(self.radioButton)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_missing_preview = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_missing_preview.setObjectName("pushButton_missing_preview")
        self.horizontalLayout_8.addWidget(self.pushButton_missing_preview)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.tableWidget_missing = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_missing.setObjectName("tableWidget_missing")
        self.tableWidget_missing.setColumnCount(0)
        self.tableWidget_missing.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tableWidget_missing)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tableWidget_dataset = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_dataset.setObjectName("tableWidget_dataset")
        self.tableWidget_dataset.setColumnCount(0)
        self.tableWidget_dataset.setRowCount(0)
        self.verticalLayout_8.addWidget(self.tableWidget_dataset)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_none = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_none.setChecked(True)
        self.radioButton_none.setObjectName("radioButton_none")
        self.verticalLayout_4.addWidget(self.radioButton_none)
        self.radioButton_mean = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_mean.setObjectName("radioButton_mean")
        self.verticalLayout_4.addWidget(self.radioButton_mean)
        self.radioButton_median = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_median.setObjectName("radioButton_median")
        self.verticalLayout_4.addWidget(self.radioButton_median)
        self.radioButton_mode = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_mode.setObjectName("radioButton_mode")
        self.verticalLayout_4.addWidget(self.radioButton_mode)
        self.radioButton_drop_col = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_drop_col.setObjectName("radioButton_drop_col")
        self.verticalLayout_4.addWidget(self.radioButton_drop_col)
        self.radioButton_drop = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_drop.setObjectName("radioButton_drop")
        self.verticalLayout_4.addWidget(self.radioButton_drop)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_replace = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_replace.setObjectName("radioButton_replace")
        self.horizontalLayout_5.addWidget(self.radioButton_replace)
        self.lineEdit_missing_replace = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_missing_replace.setObjectName("lineEdit_missing_replace")
        self.horizontalLayout_5.addWidget(self.lineEdit_missing_replace)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_drop_ratio = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_drop_ratio.setObjectName("radioButton_drop_ratio")
        self.horizontalLayout_6.addWidget(self.radioButton_drop_ratio)
        self.doubleSpinBox_missing_ratio = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_missing_ratio.setMaximum(1.0)
        self.doubleSpinBox_missing_ratio.setProperty("value", 0.5)
        self.doubleSpinBox_missing_ratio.setObjectName("doubleSpinBox_missing_ratio")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_missing_ratio)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.tableWidget_replace = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_replace.setObjectName("tableWidget_replace")
        self.tableWidget_replace.setColumnCount(0)
        self.tableWidget_replace.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget_replace)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_code = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_code.setObjectName("pushButton_code")
        self.horizontalLayout_3.addWidget(self.pushButton_code)
        self.pushButton_help = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_help.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/pyqt/source/images/lc_helpindex.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_help.setIcon(icon6)
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout_3.addWidget(self.pushButton_help)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.pushButton_ok = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_3.addWidget(self.pushButton_ok)
        self.pushButton_save = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_3.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_7.addWidget(self.widget_3)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据-缺失值处理"))
        self.label_3.setText(_translate("Form", "全部变量:"))
        self.label_5.setText(_translate("Form", "已选变量:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "变量"))
        self.radioButton.setText(_translate("Form", "默认"))
        self.radioButton_2.setText(_translate("Form", "自定义"))
        self.lineEdit_3.setText(_translate("Form", "-99999"))
        self.label_2.setText(_translate("Form", "多个值用分号隔开"))
        self.pushButton_missing_preview.setText(_translate("Form", "预览"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "缺失值"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "描述统计"))
        self.radioButton_none.setText(_translate("Form", "无"))
        self.radioButton_mean.setText(_translate("Form", "使用列均值替换"))
        self.radioButton_median.setText(_translate("Form", "使用列中位数替换"))
        self.radioButton_mode.setText(_translate("Form", "使用列众数替换"))
        self.radioButton_drop_col.setText(_translate("Form", "删除全部为缺失值的列"))
        self.radioButton_drop.setText(_translate("Form", "删除有缺失值的行"))
        self.radioButton_replace.setText(_translate("Form", "替换为"))
        self.lineEdit_missing_replace.setText(_translate("Form", "-99999"))
        self.radioButton_drop_ratio.setText(_translate("Form", "缺失值大于指定百分比时删除对应记录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "选项"))
        self.pushButton_code.setText(_translate("Form", "代码"))
        self.pushButton_ok.setText(_translate("Form", "确定"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
import pyqtsource_rc
