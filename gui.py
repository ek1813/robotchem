# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.12.2.dev1709221830
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(708, 531)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.graphicsView = QtGui.QGraphicsView(self.widget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.txtResult = QtGui.QLineEdit(self.widget)
        self.txtResult.setObjectName(_fromUtf8("txtResult"))
        self.horizontalLayout_2.addWidget(self.txtResult)
        self.verticalLayout.addWidget(self.widget)
        self.widget_6 = QtGui.QWidget(self.centralWidget)
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_6)
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.widget_9 = QtGui.QWidget(self.widget_6)
        self.widget_9.setObjectName(_fromUtf8("widget_9"))
        self.formLayout = QtGui.QFormLayout(self.widget_9)
        self.formLayout.setMargin(11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labInterval = QtGui.QLabel(self.widget_9)
        self.labInterval.setObjectName(_fromUtf8("labInterval"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labInterval)
        self.spinInterval = QtGui.QSpinBox(self.widget_9)
        self.spinInterval.setObjectName(_fromUtf8("spinInterval"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinInterval)
        self.labTime = QtGui.QLabel(self.widget_9)
        self.labTime.setObjectName(_fromUtf8("labTime"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labTime)
        self.spinTime = QtGui.QSpinBox(self.widget_9)
        self.spinTime.setObjectName(_fromUtf8("spinTime"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinTime)
        self.gridLayout_2.addWidget(self.widget_9, 0, 3, 1, 1)
        self.widget_7 = QtGui.QWidget(self.widget_6)
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_7)
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnTakePic = QtGui.QPushButton(self.widget_7)
        self.btnTakePic.setObjectName(_fromUtf8("btnTakePic"))
        self.verticalLayout_2.addWidget(self.btnTakePic)
        self.btnAutofocus = QtGui.QPushButton(self.widget_7)
        self.btnAutofocus.setObjectName(_fromUtf8("btnAutofocus"))
        self.verticalLayout_2.addWidget(self.btnAutofocus)
        self.gridLayout_2.addWidget(self.widget_7, 0, 0, 1, 1)
        self.widget_8 = QtGui.QWidget(self.widget_6)
        self.widget_8.setObjectName(_fromUtf8("widget_8"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_8)
        self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.btnMoveUp = QtGui.QPushButton(self.widget_8)
        self.btnMoveUp.setObjectName(_fromUtf8("btnMoveUp"))
        self.verticalLayout_3.addWidget(self.btnMoveUp)
        self.btnMoveDown = QtGui.QPushButton(self.widget_8)
        self.btnMoveDown.setObjectName(_fromUtf8("btnMoveDown"))
        self.verticalLayout_3.addWidget(self.btnMoveDown)
        self.gridLayout_2.addWidget(self.widget_8, 0, 1, 1, 1)
        self.widget_2 = QtGui.QWidget(self.widget_6)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setMargin(11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.btnStart = QtGui.QPushButton(self.widget_2)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.verticalLayout_4.addWidget(self.btnStart)
        self.btnStop = QtGui.QPushButton(self.widget_2)
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.verticalLayout_4.addWidget(self.btnStop)
        self.gridLayout_2.addWidget(self.widget_2, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget_6)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 708, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtGui.QToolBar(MainWindow)
        self.toolBar_3.setObjectName(_fromUtf8("toolBar_3"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labInterval.setText(_translate("MainWindow", "Set Interval", None))
        self.labTime.setText(_translate("MainWindow", "Set Time", None))
        self.btnTakePic.setText(_translate("MainWindow", "Take Picture", None))
        self.btnAutofocus.setText(_translate("MainWindow", "Autofocus", None))
        self.btnMoveUp.setText(_translate("MainWindow", "Move Up", None))
        self.btnMoveDown.setText(_translate("MainWindow", "Move Down", None))
        self.btnStart.setText(_translate("MainWindow", "Start", None))
        self.btnStop.setText(_translate("MainWindow", "Stop", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

