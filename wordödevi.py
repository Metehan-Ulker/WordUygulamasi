from PyQt5.QtWidgets  import  QMessageBox, QFileDialog,QColorDialog
from PyQt5 import QtCore, QtGui, QtWidgets 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1047, 825)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 0, 531, 91))
        
        
        self.tabWidget.setObjectName("tabWidget")
        font = QtGui.QFont()
        font.setBold(True)
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton.clicked.connect(Dialog.close)
        
        
        
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 20, 75, 23))
        
        
        
        
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 0, 75, 23))
        self.pushButton_5.clicked.connect(self.saveTextToFile)
        
        
        
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 20, 101, 23))
        
        
        
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.checkBox = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox.setGeometry(QtCore.QRect(10, 0, 81, 17))
                       
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.updateTextFormat)
        
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 16, 101, 21))
         
      
        self.checkBox_2.setFont(font)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.updateTextFormat)
        
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 36, 101, 20))
              
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.stateChanged.connect(self.updateTextFormat)
        
        self.spinBox = QtWidgets.QSpinBox(self.tab_6)
        self.spinBox.setGeometry(QtCore.QRect(250, 10, 42, 22))
        self.spinBox.setMinimum(4)
        self.spinBox.setMaximum(60)
        self.spinBox.setSingleStep(2)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.valueChanged.connect(self.updateTextSize)
        
        self.label = QtWidgets.QLabel(self.tab_6)
        self.label.setGeometry(QtCore.QRect(150, 10, 91, 16))
        
    
        
       
        
        self.label_2 = QtWidgets.QLabel(self.tab_6)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 71, 16))
        
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.fontComboBox = QtWidgets.QFontComboBox(self.tab_6)
        self.fontComboBox.setGeometry(QtCore.QRect(310, 30, 188, 22))   
        self.fontComboBox.currentFontChanged.connect(self.changeFont)
        
        self.label_3 = QtWidgets.QLabel(self.tab_6)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 81, 16))
        
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        
        
        self.pushButton_3r = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_3r.setGeometry(QtCore.QRect(220, 30, 70, 20))
        self.pushButton_3r.setObjectName("pushButton_3")
        self.pushButton_3r.setText("Renk Seç")  # Örnek bir metin
        self.pushButton_3r.clicked.connect(self.openColorDialog)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 91, 23))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.clearText)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 181, 23))
        
        self.pushButton_4.setFont(font)
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_ileri = QtWidgets.QWidget()
        self.tab_ileri.setObjectName("tab_ileri")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_ileri)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 0, 75, 23))
        
        
        self.pushButton_7.setFont(font)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.redoAction)
        self.tabWidget.addTab(self.tab_ileri, "")
        self.tab_geri = QtWidgets.QWidget()
        self.tab_geri.setObjectName("tab_geri")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_geri)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 0, 75, 23))
        
        
        self.pushButton_8.setFont(font)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.undoAction)
        self.tabWidget.addTab(self.tab_geri, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 0, 75, 23))
        
        self.pushButton_10.setFont(font)
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(0, 20, 111, 23))
       
        self.pushButton_11.setFont(font)
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 0, 75, 23))
        
        self.pushButton_9.setFont(font)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_12.setGeometry(QtCore.QRect(0, 20, 75, 23))
        
        self.pushButton_12.setFont(font)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.tabWidget.addTab(self.tab_5, "")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(850, 790, 171, 21))
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(50, 790, 761, 21))
        self.horizontalScrollBar.setProperty("value", 0)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1030, 20, 21, 781))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(300, 760, 131, 31))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 1.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.tabWidget_2 = QtWidgets.QTabWidget(Dialog)
        self.tabWidget_2.setGeometry(QtCore.QRect(710, 0, 321, 211))
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setTabsClosable(True)
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_7)
        self.dateEdit.setGeometry(QtCore.QRect(0, 0, 321, 31))
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2025, 4, 16), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName("dateEdit")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.timeEdit = QtWidgets.QTimeEdit(self.tab_8)
        self.timeEdit.setGeometry(QtCore.QRect(0, 0, 321, 31))
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(14, 0, 0)))
        self.timeEdit.setObjectName("timeEdit")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_9)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 321, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tabWidget_2.addTab(self.tab_9, "")
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 90, 681, 671))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Kapat"))
        self.pushButton_2.setText(_translate("Dialog", "Yazdır"))
        self.pushButton_5.setText(_translate("Dialog", "Kaydet"))
        self.pushButton_6.setText(_translate("Dialog", "Farklı Kaydet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Dosya"))
        self.checkBox.setText(_translate("Dialog", "Altı çizili"))
        self.checkBox_2.setText(_translate("Dialog", "Yazı Kalınlığı"))
        self.checkBox_3.setText(_translate("Dialog", "Yazı Yatıklığı"))
        self.label.setText(_translate("Dialog", "Yazı Büyüklüğü"))
        
        self.label_2.setText(_translate("Dialog", "Yazı Rengi"))
        self.label_3.setText(_translate("Dialog", "Yazı Fontu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Dialog", "Giriş"))
        self.pushButton_3.setText(_translate("Dialog", "Yeni Sayfa aç"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Yeni"))
        self.pushButton_4.setText(_translate("Dialog", "Bilgisayarındaki Dosyayı Aç"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Aç"))
        self.pushButton_7.setText(_translate("Dialog", "İleriye Al"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ileri), _translate("Dialog", "İleri"))
        self.pushButton_8.setText(_translate("Dialog", "Geriye Al"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_geri), _translate("Dialog", "Geri "))
        self.pushButton_10.setText(_translate("Dialog", "Resim ekle"))
        self.pushButton_11.setText(_translate("Dialog", "Url Uzantısı ekle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Ekle"))
        self.pushButton_9.setText(_translate("Dialog", "Hizmetler"))
        self.pushButton_12.setText(_translate("Dialog", "Tercihler"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Yardım"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Dialog", "Tarihi Göster"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Dialog", "Saati Göster"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("Dialog", "Takvimi Göster"))
        
    def undoAction(self):
        self.plainTextEdit.undo()
    def redoAction(self):
        self.plainTextEdit.redo()    
    def updateTextFormat(self):
        # Şu anki seçime göre yazı stilini değiştiren fonksiyon
        font = self.plainTextEdit.font()

        # Altı çizili mi?
        if self.checkBox.isChecked():
            font.setUnderline(True)
        else:
            font.setUnderline(False)

        # Kalın mı?
        if self.checkBox_2.isChecked():
            font.setBold(True)
        else:
            font.setBold(False)

        # İtalik mi?
        if self.checkBox_3.isChecked():
            font.setItalic(True)
        else:
            font.setItalic(False)

        # Değişiklikleri uygulama
        self.plainTextEdit.setFont(font)
    def clearText(self):
    
     self.plainTextEdit.clear()
    def updateTextSize(self):
        # Yazı büyüklüğünü ayarlamaa
        font = self.plainTextEdit.font()
        font.setPointSize(self.spinBox.value())
        self.plainTextEdit.setFont(font)

    def openColorDialog(self):
    # Renk seçimi diyalogunu açan ve metin rengini değiştiren fonksiyon
     color = QColorDialog.getColor()
     if color.isValid():
        cursor = self.plainTextEdit.textCursor()
        cursor.setCharFormat(QtGui.QTextCharFormat())
        format = cursor.charFormat()
        format.setForeground(color)
        cursor.setCharFormat(format)
        self.plainTextEdit.mergeCurrentCharFormat(format)
            
    def changeFont(self, font):
        fmt = QtGui.QTextCharFormat()
        fmt.setFont(font)
        cursor = self.plainTextEdit.textCursor()
        cursor.mergeCharFormat(fmt)
        self.plainTextEdit.mergeCurrentCharFormat(fmt)
    

    def saveTextToFile(self):
        # Kaydetme işlemi
        file_name, _ = QFileDialog.getSaveFileName(None, "Dosya Kaydet", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, 'w') as file:
                text = self.plainTextEdit_2.toPlainText()
                file.write(text)
            QMessageBox.information(None, "Başarılı", "Metin başarıyla kaydedildi!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_()) 