# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 642)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 40, 941, 561))
        self.tabWidget.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setEnabled(True)
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(450, 160, 67, 17))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 270, 881, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_Words = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_Words.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Words.setObjectName("horizontalLayout_Words")
        self.lineEdit_word = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_word.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(233, 185, 110);\n"
"\n"
"font: 57 11pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"\n"
"height: 25%")
        self.lineEdit_word.setText("")
        self.lineEdit_word.setObjectName("lineEdit_word")
        self.horizontalLayout_Words.addWidget(self.lineEdit_word)
        self.lineEdit_translation = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_translation.setStyleSheet("background-color: rgb(233, 185, 110);\n"
"color: rgb(85, 87, 83);\n"
"\n"
"font: 57 11pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"\n"
"height: 25%")
        self.lineEdit_translation.setText("")
        self.lineEdit_translation.setObjectName("lineEdit_translation")
        self.horizontalLayout_Words.addWidget(self.lineEdit_translation)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(740, 20, 171, 170))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_browse = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_browse.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_browse.setAccessibleDescription("")
        self.pushButton_browse.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"font: 57 12pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"color: rgb(136, 138, 133);\n"
"\n"
"QPushButton::hover {\n"
"    color: rgb(254, 0, 0);\n"
"}")
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.verticalLayout_3.addWidget(self.pushButton_browse)
        self.label_dirname = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_dirname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dirname.setObjectName("label_dirname")
        self.verticalLayout_3.addWidget(self.label_dirname)
        self.comboBox_ToLearn = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_ToLearn.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(233, 185, 110);\n"
"font: 50 12pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"")
        self.comboBox_ToLearn.setObjectName("comboBox_ToLearn")
        self.comboBox_ToLearn.addItem("")
        self.comboBox_ToLearn.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_ToLearn)
        self.label_words_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_words_number.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(186, 189, 182);")
        self.label_words_number.setObjectName("label_words_number")
        self.verticalLayout_3.addWidget(self.label_words_number)
        self.pushButton_apply = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_apply.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_apply.setAccessibleDescription("")
        self.pushButton_apply.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(233, 185, 110);\n"
"font: 57 15pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"\n"
"pushButton_get_word::hover {\n"
"    color: rgb(254, 0, 0);\n"
"}")
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.verticalLayout_3.addWidget(self.pushButton_apply)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setStyleSheet("width: 80%;")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.label_current_index = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_current_index.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_current_index.setAutoFillBackground(False)
        self.label_current_index.setStyleSheet("width: 50%;")
        self.label_current_index.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_index.setObjectName("label_current_index")
        self.horizontalLayout.addWidget(self.label_current_index)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 350, 881, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_get_translation = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_get_translation.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_get_translation.setAccessibleDescription("")
        self.pushButton_get_translation.setStyleSheet("background-color: rgb(252, 175, 62);\n"
"font: 50 13pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"color: ;\n"
"color: rgb(85, 87, 83);\n"
"\n"
"QPushButton::hover {\n"
"    color: rgb(254, 0, 0);\n"
"}")
        self.pushButton_get_translation.setObjectName("pushButton_get_translation")
        self.gridLayout.addWidget(self.pushButton_get_translation, 0, 1, 1, 1)
        self.pushButton_get_word = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_get_word.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_get_word.setAccessibleDescription("")
        self.pushButton_get_word.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(233, 185, 110);\n"
"font: 57 15pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"\n"
"pushButton_get_word::hover {\n"
"    color: rgb(254, 0, 0);\n"
"}")
        self.pushButton_get_word.setObjectName("pushButton_get_word")
        self.gridLayout.addWidget(self.pushButton_get_word, 0, 0, 1, 1)
        self.pushButton_clear_word = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_clear_word.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_clear_word.setAccessibleDescription("")
        self.pushButton_clear_word.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(233, 185, 110);\n"
"font: 57 15pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"\n"
"pushButton_get_word::hover {\n"
"    color: rgb(254, 0, 0);\n"
"}")
        self.pushButton_clear_word.setObjectName("pushButton_clear_word")
        self.gridLayout.addWidget(self.pushButton_clear_word, 1, 0, 1, 1)
        self.pushButton_clear_translation = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_clear_translation.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_clear_translation.setAccessibleDescription("")
        self.pushButton_clear_translation.setStyleSheet("background-color: rgb(252, 175, 62);\n"
"font: 50 13pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"color: ;\n"
"color: rgb(85, 87, 83);\n"
"\n"
"QPushButton::hover {\n"
"    color: rgb(254, 0, 0);\n"
"}")
        self.pushButton_clear_translation.setObjectName("pushButton_clear_translation")
        self.gridLayout.addWidget(self.pushButton_clear_translation, 1, 1, 1, 1)
        self.label_Image = QtWidgets.QLabel(self.tab)
        self.label_Image.setGeometry(QtCore.QRect(50, 20, 401, 231))
        self.label_Image.setStyleSheet("border: 2px red solid;\n"
"")
        self.label_Image.setText("")
        self.label_Image.setPixmap(QtGui.QPixmap("../../../Загрузки/greedy.jpg"))
        self.label_Image.setScaledContents(True)
        self.label_Image.setObjectName("label_Image")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(490, 20, 231, 171))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_get_new_word = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_get_new_word.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_get_new_word.setAccessibleDescription("")
        self.pushButton_get_new_word.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"font: 57 14pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"color: rgb(136, 138, 133);\n"
"\n"
"QPushButton::hover {\n"
"    color: rgb(254, 0, 0);\n"
"}")
        self.pushButton_get_new_word.setObjectName("pushButton_get_new_word")
        self.verticalLayout_4.addWidget(self.pushButton_get_new_word)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_on_top = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_on_top.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_on_top.setAccessibleDescription("")
        self.pushButton_on_top.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(233, 185, 110);\n"
"font: 50 13pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"\n"
"pushButton_get_word::hover {\n"
"    color: rgb(254, 0, 0);\n"
"}")
        self.pushButton_on_top.setObjectName("pushButton_on_top")
        self.horizontalLayout_2.addWidget(self.pushButton_on_top)
        self.pushButton_save = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_save.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_save.setAccessibleDescription("")
        self.pushButton_save.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(233, 185, 110);\n"
"font: 50 13pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"\n"
"pushButton_get_word::hover {\n"
"    color: rgb(254, 0, 0);\n"
"}")
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_2.addWidget(self.pushButton_save)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.pushButton_prev_word = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_prev_word.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_prev_word.setAccessibleDescription("")
        self.pushButton_prev_word.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"font: 57 14pt \"Ubuntu\";\n"
"font-weight: bold;\n"
"color: rgb(136, 138, 133);\n"
"\n"
"QPushButton::hover {\n"
"    color: rgb(254, 0, 0);\n"
"}")
        self.pushButton_prev_word.setObjectName("pushButton_prev_word")
        self.verticalLayout_4.addWidget(self.pushButton_prev_word)
        self.pushButton_exit = QtWidgets.QPushButton(self.tab)
        self.pushButton_exit.setGeometry(QtCore.QRect(780, 470, 131, 41))
        self.pushButton_exit.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 20px;")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_word_towrite = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_word_towrite.setEnabled(True)
        self.lineEdit_word_towrite.setGeometry(QtCore.QRect(90, 190, 121, 25))
        self.lineEdit_word_towrite.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);")
        self.lineEdit_word_towrite.setText("")
        self.lineEdit_word_towrite.setFrame(True)
        self.lineEdit_word_towrite.setObjectName("lineEdit_word_towrite")
        self.lineEdit_translation_towrite = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_translation_towrite.setGeometry(QtCore.QRect(270, 190, 113, 25))
        self.lineEdit_translation_towrite.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);")
        self.lineEdit_translation_towrite.setText("")
        self.lineEdit_translation_towrite.setObjectName("lineEdit_translation_towrite")
        self.pushButton_write = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_write.setGeometry(QtCore.QRect(100, 240, 171, 25))
        self.pushButton_write.setObjectName("pushButton_write")
        self.Text_towrite = QtWidgets.QPlainTextEdit(self.tab_2)
        self.Text_towrite.setGeometry(QtCore.QRect(90, 20, 291, 201))
        self.Text_towrite.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);")
        self.Text_towrite.setCenterOnScroll(True)
        self.Text_towrite.setPlaceholderText("")
        self.Text_towrite.setObjectName("Text_towrite")
        self.label_writeTip = QtWidgets.QLabel(self.tab_2)
        self.label_writeTip.setGeometry(QtCore.QRect(100, 280, 321, 21))
        self.label_writeTip.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(233, 185, 110);")
        self.label_writeTip.setObjectName("label_writeTip")
        self.label_wordTip = QtWidgets.QLabel(self.tab_2)
        self.label_wordTip.setGeometry(QtCore.QRect(90, 150, 121, 21))
        self.label_wordTip.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(233, 185, 110);")
        self.label_wordTip.setObjectName("label_wordTip")
        self.label_translationTip = QtWidgets.QLabel(self.tab_2)
        self.label_translationTip.setGeometry(QtCore.QRect(270, 150, 121, 21))
        self.label_translationTip.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(233, 185, 110);")
        self.label_translationTip.setObjectName("label_translationTip")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(400, 20, 160, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioOneWord_towrite = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioOneWord_towrite.setChecked(True)
        self.radioOneWord_towrite.setObjectName("radioOneWord_towrite")
        self.buttonGroup_writeMode = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_writeMode.setObjectName("buttonGroup_writeMode")
        self.buttonGroup_writeMode.addButton(self.radioOneWord_towrite)
        self.verticalLayout_2.addWidget(self.radioOneWord_towrite)
        self.radioText_towrite = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioText_towrite.setObjectName("radioText_towrite")
        self.buttonGroup_writeMode.addButton(self.radioText_towrite)
        self.verticalLayout_2.addWidget(self.radioText_towrite)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(450, 140, 321, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        self.lineEdit_translation_towrite.raise_()
        self.pushButton_write.raise_()
        self.lineEdit_word_towrite.raise_()
        self.Text_towrite.raise_()
        self.label_writeTip.raise_()
        self.label_wordTip.raise_()
        self.label_translationTip.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.tableWidget.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, -1, 160, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_Word = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_Word.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(211, 215, 207);\n"
"text-align: center;")
        self.checkBox_Word.setObjectName("checkBox_Word")
        self.verticalLayout.addWidget(self.checkBox_Word)
        self.checkBox_Translation = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_Translation.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(211, 215, 207);")
        self.checkBox_Translation.setCheckable(True)
        self.checkBox_Translation.setChecked(True)
        self.checkBox_Translation.setObjectName("checkBox_Translation")
        self.verticalLayout.addWidget(self.checkBox_Translation)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.radioOneWord_towrite.clicked.connect(self.label_writeTip.hide)
        self.radioOneWord_towrite.clicked.connect(self.label_wordTip.show)
        self.radioText_towrite.clicked.connect(self.label_wordTip.hide)
        self.radioText_towrite.clicked.connect(self.label_writeTip.show)
        self.radioText_towrite.clicked.connect(self.lineEdit_word_towrite.hide)
        self.radioOneWord_towrite.clicked.connect(self.label_translationTip.show)
        self.radioText_towrite.clicked.connect(self.label_translationTip.hide)
        self.radioOneWord_towrite.clicked.connect(self.lineEdit_translation_towrite.show)
        self.radioText_towrite.clicked.connect(self.Text_towrite.show)
        self.radioOneWord_towrite.clicked.connect(self.Text_towrite.hide)
        self.radioText_towrite.clicked.connect(self.lineEdit_translation_towrite.hide)
        self.radioOneWord_towrite.clicked.connect(self.lineEdit_word_towrite.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_browse.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_browse.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>lll</p></body></html>"))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse"))
        self.label_dirname.setText(_translate("MainWindow", "Directory"))
        self.comboBox_ToLearn.setItemText(0, _translate("MainWindow", "terms"))
        self.comboBox_ToLearn.setItemText(1, _translate("MainWindow", "dates"))
        self.label_words_number.setText(_translate("MainWindow", "0"))
        self.pushButton_apply.setText(_translate("MainWindow", "Apply"))
        self.label_current_index.setText(_translate("MainWindow", "0"))
        self.pushButton_get_translation.setText(_translate("MainWindow", "Get the translation"))
        self.pushButton_get_word.setText(_translate("MainWindow", "Get a word"))
        self.pushButton_clear_word.setText(_translate("MainWindow", "Clear a word"))
        self.pushButton_clear_translation.setText(_translate("MainWindow", "Clear the translation"))
        self.pushButton_get_new_word.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_get_new_word.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>lll</p></body></html>"))
        self.pushButton_get_new_word.setText(_translate("MainWindow", "Get a new word"))
        self.pushButton_on_top.setText(_translate("MainWindow", "On top"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_prev_word.setText(_translate("MainWindow", "Previous word"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "LEARN"))
        self.pushButton_write.setText(_translate("MainWindow", "Записать слово"))
        self.label_writeTip.setText(_translate("MainWindow", "Words are supposed to be : word-translation"))
        self.label_wordTip.setText(_translate("MainWindow", "Word"))
        self.label_translationTip.setText(_translate("MainWindow", "Translation"))
        self.radioOneWord_towrite.setText(_translate("MainWindow", "Одно слово"))
        self.radioText_towrite.setText(_translate("MainWindow", "Текст"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "word"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "separator"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "translation"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "hello"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "1"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "WRITE"))
        self.checkBox_Word.setText(_translate("MainWindow", "Word"))
        self.checkBox_Translation.setText(_translate("MainWindow", "Translation"))
