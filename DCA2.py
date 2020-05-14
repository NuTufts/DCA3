# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dmishins/DAPHNEgui.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
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
        MainWindow.resize(364, 351)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_takespill = QtGui.QPushButton(self.centralwidget)
        self.btn_takespill.setGeometry(QtCore.QRect(10, 100, 88, 29))
        self.btn_takespill.setObjectName(_fromUtf8("btn_takespill"))
        self.btn_setdur = QtGui.QPushButton(self.centralwidget)
        self.btn_setdur.setGeometry(QtCore.QRect(10, 50, 111, 29))
        self.btn_setdur.setObjectName(_fromUtf8("btn_setdur"))
        self.btn_exp = QtGui.QPushButton(self.centralwidget)
        self.btn_exp.setGeometry(QtCore.QRect(10, 140, 88, 29))
        self.btn_exp.setObjectName(_fromUtf8("btn_exp"))
        self.spilldurr = QtGui.QSpinBox(self.centralwidget)
        self.spilldurr.setGeometry(QtCore.QRect(200, 50, 59, 29))
        self.spilldurr.setObjectName(_fromUtf8("spilldurr"))
        self.rootfilename = QtGui.QLineEdit(self.centralwidget)
        self.rootfilename.setGeometry(QtCore.QRect(200, 140, 113, 29))
        self.rootfilename.setObjectName(_fromUtf8("rootfilename"))
        self.label_root_filename = QtGui.QLabel(self.centralwidget)
        self.label_root_filename.setGeometry(QtCore.QRect(110, 150, 81, 17))
        self.label_root_filename.setObjectName(_fromUtf8("label_root_filename"))
        self.binfilename = QtGui.QLineEdit(self.centralwidget)
        self.binfilename.setGeometry(QtCore.QRect(200, 100, 113, 29))
        self.binfilename.setObjectName(_fromUtf8("binfilename"))
        self.label_bin_filename = QtGui.QLabel(self.centralwidget)
        self.label_bin_filename.setGeometry(QtCore.QRect(110, 110, 81, 17))
        self.label_bin_filename.setObjectName(_fromUtf8("label_bin_filename"))
        self.chk_2 = QtGui.QCheckBox(self.centralwidget)
        self.chk_2.setGeometry(QtCore.QRect(120, 230, 51, 22))
        self.chk_2.setObjectName(_fromUtf8("chk_2"))
        self.chk_3 = QtGui.QCheckBox(self.centralwidget)
        self.chk_3.setGeometry(QtCore.QRect(120, 250, 51, 22))
        self.chk_3.setObjectName(_fromUtf8("chk_3"))
        self.chk_4 = QtGui.QCheckBox(self.centralwidget)
        self.chk_4.setGeometry(QtCore.QRect(120, 270, 51, 22))
        self.chk_4.setObjectName(_fromUtf8("chk_4"))
        self.chk_super = QtGui.QCheckBox(self.centralwidget)
        self.chk_super.setGeometry(QtCore.QRect(190, 220, 141, 21))
        self.chk_super.setObjectName(_fromUtf8("chk_super"))
        self.chk_1 = QtGui.QCheckBox(self.centralwidget)
        self.chk_1.setGeometry(QtCore.QRect(120, 210, 51, 22))
        self.chk_1.setObjectName(_fromUtf8("chk_1"))
        self.btn_plt = QtGui.QPushButton(self.centralwidget)
        self.btn_plt.setGeometry(QtCore.QRect(10, 230, 101, 29))
        self.btn_plt.setObjectName(_fromUtf8("btn_plt"))
        self.chk_fft = QtGui.QCheckBox(self.centralwidget)
        self.chk_fft.setGeometry(QtCore.QRect(190, 240, 86, 22))
        self.chk_fft.setObjectName(_fromUtf8("chk_fft"))
        self.chk_maxadchist = QtGui.QCheckBox(self.centralwidget)
        self.chk_maxadchist.setGeometry(QtCore.QRect(190, 260, 141, 22))
        self.chk_maxadchist.setObjectName(_fromUtf8("chk_maxadchist"))
        self.chk_areahist = QtGui.QCheckBox(self.centralwidget)
        self.chk_areahist.setGeometry(QtCore.QRect(190, 280, 131, 22))
        self.chk_areahist.setObjectName(_fromUtf8("chk_areahist"))
        self.chk_plot = QtGui.QCheckBox(self.centralwidget)
        self.chk_plot.setGeometry(QtCore.QRect(190, 200, 86, 22))
        self.chk_plot.setObjectName(_fromUtf8("chk_plot"))
        self.btn_measurecur = QtGui.QPushButton(self.centralwidget)
        self.btn_measurecur.setGeometry(QtCore.QRect(10, 10, 111, 29))
        self.btn_measurecur.setObjectName(_fromUtf8("btn_measurecur"))
        self.current_channel = QtGui.QSpinBox(self.centralwidget)
        self.current_channel.setGeometry(QtCore.QRect(200, 10, 59, 29))
        self.current_channel.setObjectName(_fromUtf8("current_channel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 364, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.btn_setdur.clicked.connect(self.setspilllen)
        self.btn_measurecur.clicked.connect(self.getcurrent)
        self.btn_takespill.clicked.connect(self.takespill)
        self.btn_exp.clicked.connect(self.exportrootfile)
        self.btn_plt.clicked.connect(self.plot)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DAPHNE GUI", None))
        self.btn_takespill.setText(_translate("MainWindow", "Take Spill", None))
        self.btn_setdur.setText(_translate("MainWindow", "Set Spill Duration", None))
        self.btn_exp.setText(_translate("MainWindow", "export root file", None))
        self.label_root_filename.setText(_translate("MainWindow", "root Filename", None))
        self.label_bin_filename.setText(_translate("MainWindow", "Bin Filename", None))
        self.chk_2.setText(_translate("MainWindow", "ch2", None))
        self.chk_3.setText(_translate("MainWindow", "ch3", None))
        self.chk_4.setText(_translate("MainWindow", "ch4", None))
        self.chk_super.setText(_translate("MainWindow", "superimpose events", None))
        self.chk_1.setText(_translate("MainWindow", "ch1", None))
        self.btn_plt.setText(_translate("MainWindow", "Plot from bin file", None))
        self.chk_fft.setText(_translate("MainWindow", "fft", None))
        self.chk_maxadchist.setText(_translate("MainWindow", "MAX adc Histogram", None))
        self.chk_areahist.setText(_translate("MainWindow", "Area Histogram", None))
        self.chk_plot.setText(_translate("MainWindow", "Plot", None))
        self.btn_measurecur.setText(_translate("MainWindow", "Measure Current", None))

    def setspilllen(self):
        print "running script to set spill length"
        print "python takeBinaryData.py --spill_length " + str(self.spilldurr.value()) + " --command_stop"

        os.system("python takeBinaryData.py --spill_length " + str(self.spilldurr.value()) + " --command_stop")
    
    def getcurrent(self):
        print "running script to set spill length"
        print "python takeBinaryData.py --get_current " + str(self.current_channel.value()) + " --command_stop"

        os.system("python takeBinaryData.py --get_current " + str(self.current_channel.value()) + " --command_stop")

    def takespill(self):
        print "running take spill"
        print "python takeBinaryData.py -f " + str(self.binfilename.text())
        os.system("python takeBinaryData.py -f " + str(self.binfilename.text()))

    def exportrootfile(self):
        print "running script to export root file"     
        print "python takeandexportroot.py " + str(self.binfilename.text()) + " --root " + str(self.rootfilename.text())

        os.system("python takeandexportroot.py " + str(self.binfilename.text()) + " --root " + str(self.rootfilename.text()))
    def plot(self):
        print "running script to plot data from bin file"

        ch = ""
        super = ""
        fft = ""
        ahist = ""
        hist = ""
        plot = ""
        if self.chk_1.checkState():
            ch += "ch1 "
        if self.chk_2.checkState():
            ch += "ch2 "
        if self.chk_3.checkState():
            ch += "ch3 "
        if self.chk_4.checkState():
            ch += "ch4 "
        if self.chk_super.checkState():
            super = " --super "
        if self.chk_fft.checkState():
            fft = " --fft " + ch
        if self.chk_areahist.checkState():
            ahist = " --ahist " + ch
        if self.chk_maxadchist.checkState():
            hist = " --hist " + ch
        if self.chk_plot.checkState():
            plot  = " -p " + ch


        print "python takeandexportroot.py " + str(self.binfilename.text()) + plot + super + fft + ahist + hist + " --ignore_timestamp"

        os.system("python takeandexportroot.py " + str(self.binfilename.text()) + plot + super + fft + ahist + hist + " --ignore_timestamp")



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
